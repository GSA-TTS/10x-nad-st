import os
import time
from sqlalchemy import create_engine, inspect

# Check required environment variables
REQUIRED_ENV_VARS = [
    "POSTGRES_USER",
    "POSTGRES_PASSWORD",
    "POSTGRES_DB",
    "POSTGRES_HOST",
    "POSTGRES_PORT",
]

if missing_vars := [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]:
    raise EnvironmentError(
        f"❌ Missing required environment variables: {', '.join(missing_vars)}"
    )

# Get database connection details from environment variables
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def wait_for_db():
    while True:
        try:
            engine = create_engine(DATABASE_URL)
            with engine.connect():
                print(f"✅ Connected to PostgreSQL at {DB_HOST}:{DB_PORT}")
                return
        except Exception as e:
            print(f"⏳ Waiting for database... {str(e)}")
            time.sleep(5)


wait_for_db()

engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

data_dict_content = "# Database Data Dictionary\n\n"

for table_name in inspector.get_table_names():
    data_dict_content += f"## Table: `{table_name}`\n\n"
    data_dict_content += (
        "| Column Name | Data Type | Nullable | Default | Primary Key |\n"
    )
    data_dict_content += (
        "|------------|----------|----------|---------|-------------|\n"
    )

    pk_constraint = inspector.get_pk_constraint(table_name)
    pk_columns = set(pk_constraint.get("constrained_columns", []))

    for column in inspector.get_columns(table_name):
        col_name = column["name"]
        col_type = str(column["type"])
        nullable = "Yes" if column["nullable"] else "No"
        default = column.get("default", "None")
        primary_key = "Yes" if col_name in pk_columns else "No"

        data_dict_content += (
            f"| {col_name} | {col_type} | {nullable} | {default} | {primary_key} |\n"
        )

    data_dict_content += "\n"

# Get the directory where the script is being executed from
current_dir = os.path.abspath(os.getcwd())
print(f"Current working directory: {current_dir}")

# Get the parent directory (10x-nad-st) - go up to the correct project root
# If script is running from scripts/ folder, need to go up one level
if os.path.basename(current_dir) == "scripts":
    project_root = os.path.dirname(current_dir)
else:
    # Assume we need to find the project root from current location
    project_root = current_dir
    # Go up in the path until we find the 10x-nad-st directory or reach filesystem root
    while os.path.basename(project_root) != "10x-nad-st" and project_root != os.path.dirname(project_root):
        project_root = os.path.dirname(project_root)

print(f"Identified project root: {project_root}")

# Place the file in the documentation directory at the project root
documentation_dir = os.path.join(project_root, "documentation")
output_path = os.path.join(documentation_dir, "data_dictionary.md")
# Ensure the documentation directory exists
os.makedirs(documentation_dir, exist_ok=True)
print(f"Output path set to: {output_path}")

with open(output_path, "w", encoding="utf-8") as file:
    file.write(data_dict_content)

print(f"✅ Data dictionary generated at: {output_path}")
