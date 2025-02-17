import os
import time
from sqlalchemy import create_engine, inspect

REQUIRED_ENV_VARS = ["POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB", "POSTGRES_HOST", "POSTGRES_PORT"]

if missing_vars := [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]:
    raise EnvironmentError(f"❌ Missing required environment variables: {', '.join(missing_vars)}")

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
    data_dict_content += "| Column Name | Data Type | Nullable | Default | Primary Key |\n"
    data_dict_content += "|------------|----------|----------|---------|-------------|\n"

    pk_constraint = inspector.get_pk_constraint(table_name)
    pk_columns = set(pk_constraint.get("constrained_columns", []))

    for column in inspector.get_columns(table_name):
        col_name = column["name"]
        col_type = str(column["type"])
        nullable = "Yes" if column["nullable"] else "No"
        default = column.get("default", "None")
        primary_key = "Yes" if col_name in pk_columns else "No"

        data_dict_content += f"| {col_name} | {col_type} | {nullable} | {default} | {primary_key} |\n"

    data_dict_content += "\n"

output_path = "./documentation/DATA_DICTIONARY.md"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as file:
    file.write(data_dict_content)

print(f"✅ Data dictionary generated at: {output_path}")
