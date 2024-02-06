# 10x National Address Database Collaboration Hub (NAD-CH)

## Local Development

Install [poetry](https://python-poetry.org/docs/#installation) so that you can
run tests and scripts locally.

Clone the repostiory:

```bash
git clone https://github.com/GSA-TTS/10x-nad-ch/
```

In order to set up a local development environment, you will need to download
[Docker](https://www.docker.com/).

To set the necessary environment variables, copy the `sample.env` file to a new
file named `.env` in the same directory:

```bash
cp sample.env .env
```

Update all settings defaulted to `<add_a_key_here>`.

Run the following command to build the app and start up its services:

```bash
docker compose up --build
```

To run database migrations:

```bash
docker exec nad-ch-dev-local poetry run alembic upgrade head
```

## Testing

Run the test suite as follows:

```bash
poetry run test
```
