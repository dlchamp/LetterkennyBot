FROM python:3.10.8-slim as os-base

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y nano

FROM os-base as poetry-base

RUN pip install -U pip setuptools wheel

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.2 python3 -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry config virtualenvs.create false
RUN apt-get remove -y curl

FROM poetry-base as app-base

RUN mkdir /app
WORKDIR /app
COPY shoresy ./shoresy
COPY pyproject.toml ./pyproject.toml
RUN poetry install --only main -vvv
RUN poetry update

FROM app-base as main

CMD tail -f /dev/null

CMD ["python", "-m", "shoresy"]
