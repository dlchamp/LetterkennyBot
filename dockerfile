# Use an official Python base image
FROM python:3.11-slim

ENV PIP_NO_CACHE_DIR=false

WORKDIR /app

RUN apt update && apt-get install -y git

# Install Poetry
RUN pip install -U pip wheel setuptools
RUN pip install poetry==1.7.1

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .

ENTRYPOINT ["python", "main.py" ]
