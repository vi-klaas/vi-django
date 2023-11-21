# Dockerfile
FROM python:3.11-slim-bullseye
LABEL authors="vi klaas"

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# poetry:
ENV POETRY_VERSION=1.6.1 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry'


# System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    ca-certificates \
    curl \
    gnupg \
    gettext \
    git \
    libpq-dev \
    wget \
    procps \
    netcat \
    ffmpeg \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION" && poetry --version


# Set work directory in the container
WORKDIR /code

# Copying dependencies
COPY pyproject.toml poetry.lock /code/

# Installing dependencies
# RUN poetry lock
RUN poetry install --with dev

# Copying in our source code
COPY . .

# Give execution rights to start script
RUN chmod +x entrypoint.sh
RUN chmod +x start-django.sh
RUN chmod +x start-celery-worker.sh
RUN chmod +x start-celery-beat.sh

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["bash", "/code/entrypoint.sh"]
