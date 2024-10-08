FROM python:3.10

RUN pip install --no-cache-dir --upgrade pip
RUN pip install poetry

WORKDIR /notes
COPY poetry.lock pyproject.toml /notes/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /notes
