from datetime import datetime
from typing import Optional
from nad_ch.application.dtos import DownloadResult
from nad_ch.domain.entities import DataProducer, DataSubmission, User
from nad_ch.domain.repositories import (
    DataProducerRepository,
    DataSubmissionRepository,
    UserRepository,
)


class FakeDataProducerRepository(DataProducerRepository):
    def __init__(self) -> None:
        self._producers = set()
        self._next_id = 1

    def add(self, producer: DataProducer) -> DataProducer:
        producer.id = self._next_id
        producer.set_created_at(datetime.now())
        self._producers.add(producer)
        self._next_id += 1
        return producer

    def get_by_name(self, name: str) -> Optional[DataProducer]:
        return next((p for p in self._producers if p.name == name), None)

    def get_all(self):
        return sorted(list(self._producers), key=lambda producer: producer.id)


class FakeDataSubmissionRepository(DataSubmissionRepository):
    def __init__(self) -> None:
        self._submissions = set()
        self._next_id = 1

    def add(self, submission: DataSubmission) -> DataSubmission:
        submission.id = self._next_id
        submission.set_created_at(datetime.now())
        self._submissions.add(submission)
        self._next_id += 1
        return submission

    def get_by_id(self, id: int) -> Optional[DataSubmission]:
        return next((s for s in self._submissions if s.id == id), None)

    def get_by_producer(self, producer: DataProducer) -> Optional[DataSubmission]:
        return [s for s in self._submissions if s.producer.name == producer.name]

    def get_by_filename(self, filename: str) -> Optional[DataSubmission]:
        return next((s for s in self._submissions if s.filename == filename), None)

    def update_report(self, submission_id: int, report) -> None:
        return None


class FakeUserRepository(UserRepository):
    def __init__(self) -> None:
        self._users = set()
        self._next_id = 1

    def add(self, user: User) -> User:
        user.id = self._next_id
        user.set_created_at(datetime.now())
        self._users.add(user)
        self._next_id += 1
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self._users if u.email == email), None)

    def get_by_id(self, id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == id), None)


class FakeStorage:
    def __init__(self):
        self._files = set()

    def upload(self, source: str, destination: str) -> bool:
        self._files.add(destination)
        return True

    def download_temp(self, filename: str) -> Optional[DownloadResult]:
        return DownloadResult(temp_dir=filename, extracted_dir=f"{filename}.gdb")

    def cleanup_temp_dir(self, temp_dir: str):
        pass


class MockCeleryTask:
    def __init__(self, result=None):
        self.result = result
        self.called = False

    def delay(self, *args, **kwargs):
        self.called = True
        return self

    def get(self, timeout=None, propagate=True, **kwargs):
        if self.result is None:
            raise Exception("No result has been set for the mock task")
        return self.result


class FakeAuth:
    def __init__(
        self, providers: dict, allowed_domains: list, callback_url_scheme: str
    ):
        self._providers = providers
        self._allowed_domains = allowed_domains
        self._callback_url_scheme = callback_url_scheme

    def fetch_oauth2_token(self, provider_name: str, code: str) -> str | None:
        pass

    def fetch_user_email_from_login_provider(
        self, provider_name: str, oauth2_token: str
    ) -> str | list[str] | None:
        pass

    def get_logout_url(self, provider_name: str) -> str:
        pass

    def make_login_url(self, provider_name: str, state_token: str) -> str | None:
        pass

    def make_logout_url(self, provider_name: str) -> str | None:
        pass

    def user_email_address_has_permitted_domain(self, email: str | list[str]) -> bool:
        def is_domain_allowed(email_address: str) -> bool:
            domain = email_address.split("@")[1]
            return domain in self._allowed_domains

        if isinstance(email, list):
            for email_address in email:
                if is_domain_allowed(email_address):
                    return True
        else:
            if is_domain_allowed(email):
                return True

        return False
