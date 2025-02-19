# Database Data Dictionary

## Table: `alembic_version`

| Column Name | Data Type | Nullable | Default | Primary Key |
|------------|----------|----------|---------|-------------|
| version_num | VARCHAR(32) | No | None | Yes |

## Table: `data_producers`

| Column Name | Data Type | Nullable | Default | Primary Key |
|------------|----------|----------|---------|-------------|
| id | INTEGER | No | nextval('data_providers_id_seq'::regclass) | Yes |
| created_at | TIMESTAMP | No | now() | No |
| updated_at | TIMESTAMP | No | now() | No |
| name | VARCHAR | No | None | No |

## Table: `column_maps`

| Column Name | Data Type | Nullable | Default | Primary Key |
|------------|----------|----------|---------|-------------|
| data_producer_id | INTEGER | No | None | No |
| name | VARCHAR | No | None | No |
| mapping | JSON | No | None | No |
| version_id | INTEGER | No | None | No |
| id | INTEGER | No | nextval('column_maps_id_seq'::regclass) | Yes |
| created_at | TIMESTAMP | No | now() | No |
| updated_at | TIMESTAMP | No | now() | No |

## Table: `users`

| Column Name | Data Type | Nullable | Default | Primary Key |
|------------|----------|----------|---------|-------------|
| id | INTEGER | No | nextval('users_id_seq'::regclass) | Yes |
| created_at | TIMESTAMP | No | now() | No |
| updated_at | TIMESTAMP | No | now() | No |
| email | VARCHAR | Yes | None | No |
| login_provider | VARCHAR | Yes | None | No |
| logout_url | VARCHAR | Yes | None | No |
| activated | BOOLEAN | No | None | No |
| data_producer_id | INTEGER | Yes | None | No |

## Table: `data_submissions`

| Column Name | Data Type | Nullable | Default | Primary Key |
|------------|----------|----------|---------|-------------|
| id | INTEGER | No | nextval('data_submissions_id_seq'::regclass) | Yes |
| created_at | TIMESTAMP | No | now() | No |
| updated_at | TIMESTAMP | No | now() | No |
| file_path | VARCHAR | No | None | No |
| data_producer_id | INTEGER | No | None | No |
| report | JSON | Yes | None | No |
| column_map_id | INTEGER | No | None | No |
| status | VARCHAR(18) | No | 'PENDING_SUBMISSION'::data_submission_status | No |
| name | VARCHAR | No | None | No |

