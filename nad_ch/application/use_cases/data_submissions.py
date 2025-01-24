import os
import shutil
import tempfile
import zipfile

from werkzeug.datastructures import FileStorage
from tempfile import NamedTemporaryFile
from typing import List, IO, Union
from nad_ch.application.dtos import DownloadResult
from nad_ch.application.exceptions import (
    InvalidDataSubmissionFileError,
    InvalidSchemaError,
)
from nad_ch.application.interfaces import ApplicationContext
from nad_ch.application.validation import FileValidator
from nad_ch.application.view_models import (
    get_view_model,
    DataSubmissionViewModel,
)
from nad_ch.core.entities import DataSubmissionStatus, DataSubmission, ColumnMap
from nad_ch.config import LANDING_ZONE


def get_data_submission(
    ctx: ApplicationContext, submission_id: int
) -> DataSubmissionViewModel:
    submission = ctx.submissions.get_by_id(submission_id)

    if submission is None:
        return None

    return get_view_model(submission)


def get_data_submissions_by_producer(
    ctx: ApplicationContext, producer_name: str
) -> List[DataSubmissionViewModel]:
    producer = ctx.producers.get_by_name(producer_name)
    if not producer:
        ctx.logger.error("Producer with that name does not exist")
        return

    submissions = ctx.submissions.get_by_producer(producer)
    ctx.logger.info(f"Data submissions for {producer.name}")
    for s in submissions:
        ctx.logger.info(f"{s.producer.name}: {s.name}")

    return get_view_model(submissions)


def validate_data_submission(
    ctx: ApplicationContext, file_path: str, column_map_name: str
):
    submission = ctx.submissions.get_by_file_path(file_path)
    if not submission:
        ctx.logger.error("Data submission with that filename does not exist")
        return

    download_result: DownloadResult = ctx.storage.download_temp(file_path)
    if not download_result:
        ctx.logger.error("Data extration error")
        return

    column_map = ctx.column_maps.get_by_name_and_version(column_map_name, 1)
    if column_map is None:
        ctx.logger.error("Column map not found")
        return

    # Using version 1 for column maps for now, may add feature for user to select
    # version later
    try:
        mapped_data_local_dir = submission.get_mapped_data_dir(
            download_result.extracted_dir, LANDING_ZONE
        )
        mapped_data_remote_dir = submission.get_mapped_data_dir(
            download_result.extracted_dir, LANDING_ZONE, True
        )
        report = ctx.task_queue.run_load_and_validate(
            ctx.submissions,
            submission.id,
            download_result.extracted_dir,
            column_map.mapping,
            mapped_data_local_dir,
        )
        _ = ctx.task_queue.run_copy_mapped_data_to_remote(
            mapped_data_local_dir,
            mapped_data_remote_dir,
        )

        ctx.logger.info(f"Total number of features: {report.overview.feature_count}")
    except Exception:
        raise
    finally:
        ctx.storage.cleanup_temp_dir(download_result.temp_dir)
        ctx.storage.cleanup_temp_dir(mapped_data_local_dir)


def validate_file_before_submission(
    ctx: ApplicationContext, file: IO[bytes], column_map_id: int
) -> bool:
    print("debug mapping starts------------")
    column_map = ctx.column_maps.get_by_id(column_map_id)
    if column_map is None:
        raise ValueError("Column map not found")

    _, file_extension = os.path.splitext(file.filename)
    if file_extension.lower() != ".zip":
        raise InvalidDataSubmissionFileError(
            "Invalid file format. Only ZIP files are accepted."
        )

    file_validator = FileValidator(file, file.filename)

    if not file_validator.validate_file():
        raise InvalidDataSubmissionFileError(
            "Invalid zipped file. Only Shapefiles and Geodatabase files are accepted."
        )

    print("debug mapping------------")

    if not file_validator.validate_schema(column_map.mapping):
        raise InvalidSchemaError(
            "Invalid schema. The schema of the file must align with the schema of the \
            selected mapping."
        )

    return True


def create_data_submission(
    ctx: ApplicationContext,
    user_id: int,
    column_map_id: int,
    submission_name: str,
    file: Union[FileStorage, IO[bytes]],
):
    user = ctx.users.get_by_id(user_id)
    if user is None:
        raise ValueError("User not found")

    producer = user.producer
    if producer is None:
        raise ValueError("Producer not found")

    column_map = ctx.column_maps.get_by_id(column_map_id)
    if column_map is None:
        raise ValueError("Column map not found")

    try:
        file_path = DataSubmission.generate_zipped_file_path(submission_name, producer)
        submission = DataSubmission(
            submission_name,
            file_path,
            DataSubmissionStatus.PENDING_SUBMISSION,
            producer,
            column_map,
        )
        saved_submission = ctx.submissions.add(submission)
        print("saved_submission", saved_submission)

        # Write the uploaded file to a temporary file
        with NamedTemporaryFile(delete=False, mode='wb', dir='/tmp') as temp_file:
            temp_file_path = temp_file.name
            print(f"Temporary file path: {temp_file_path}")

            # Save stream to the temp file
            with file.stream as fs:
                shutil.copyfileobj(fs, temp_file, length=16384)

        # Debug: Save a copy of the uploaded file for inspection
        debug_path = "/tmp/debug_uploaded_file.zip"
        shutil.copy(temp_file_path, debug_path)
        print(f"Debug file saved at {debug_path}")

        print(f"Temporary file written: {temp_file_path}")
        print(f"Temp file size: {os.stat(temp_file_path).st_size} bytes")

        print("Verify file access")
        if not os.access(temp_file_path, os.R_OK):
            print("File not readable")
            raise InvalidDataSubmissionFileError("Temporary file is not accessible.")

        print("Check if the file is a valid zip")
        if not zipfile.is_zipfile(temp_file_path):
            print("File not zipped")
            raise InvalidDataSubmissionFileError("The uploaded file is not a valid zip file.")

        # Log zip file contents
        with zipfile.ZipFile(temp_file_path, 'r') as zf:
            print("Zip file contents:")
            print(zf.namelist())

        # Test the zip file integrity
        try:
            with zipfile.ZipFile(temp_file_path, 'r') as zf:
                print("Testing zip file integrity...")
                corrupted_file = zf.testzip()
                if corrupted_file:
                    print(f"Corrupted file found in zip: {corrupted_file}")
                    raise InvalidDataSubmissionFileError(f"Corrupted file in zip: {corrupted_file}")
                print("Zip file is valid")
        except zipfile.BadZipFile as e:
            print(f"BadZipFile error: {e}")
            raise InvalidDataSubmissionFileError(f"Invalid zip file: {e}")
        except Exception as e:
            print(f"Unexpected error during zip validation: {e}")
            raise

        os.remove(temp_file_path)

        # No need to manually remove temp_zip_path because TemporaryDirectory handles cleanup
        ctx.logger.info(f"Submission added: {saved_submission.file_path}")
        return get_view_model(saved_submission)
    except Exception as e:
        ctx.storage.delete(file_path)
        ctx.logger.error(f"Failed to process submission: {e}")
