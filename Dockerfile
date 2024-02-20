# Setup Python
FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Update and install packages
RUN apt-get update && apt-get install -y \
    curl \
    binutils \
    build-essential \
    gdal-bin \
    libgdal-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set GDAL environment variables
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal \
    GDAL_VERSION=3.6.2

# Install GDAL Python bindings with the specified version
RUN pip install GDAL==$GDAL_VERSION

# Install poetry in /opt/poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -
ENV PATH="${PATH}:/opt/poetry/bin"

# Add the current directory to the PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Create a non-root user to run the app
RUN useradd --create-home --shell /bin/bash appuser

# Install dependencies and start app
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
COPY . .
USER appuser
CMD ["/bin/sh", "./scripts/start_local.sh"]
