# Use an official Python base image
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=false

WORKDIR /app

# Install git and curl
RUN apt update && apt-get install -y git curl

# Install Poetry
ENV POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -

# Configure Poetry's PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy project files (pyproject.toml and poetry.lock) from src directory
COPY pyproject.toml poetry.lock* ./

# Export requirements.txt using Poetry and install dependencies with pip
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

# Remove Poetry and the associated files
RUN rm -rf pyproject.toml poetry.lock requirements.txt \
    && pip uninstall -y poetry \
    && apt-get remove -y curl \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the content of the src directory to /app, but not the src directory itself
COPY . .

# Set the entry point
ENTRYPOINT ["python", "main.py"]
