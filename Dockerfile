FROM python:3.10.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt install --no-install-recommends --yes curl


WORKDIR /quiz_app

COPY ./pyproject.toml ./poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-dev

COPY ./app ./app

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host",  "0.0.0.0", "--reload"]

HEALTHCHECK --interval=12s --timeout=12s --start-period=30s \
            CMD curl -f http://localhost:8000/ || exit 1
