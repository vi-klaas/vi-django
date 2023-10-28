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
    # ffmpeg \
  # Install Node.js: \
  #&& mkdir -p /etc/apt/keyrings \
  #&& curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
  #&& NODE_MAJOR=20 \
  #&& echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list \
  #&& curl -sL https://deb.nodesource.com/setup_20.x | bash - \
  && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
  && VERSION=node_20.x \
  && DISTRO="bullseye" \
  && echo "deb https://deb.nodesource.com/$VERSION $DISTRO main" | tee /etc/apt/sources.list.d/nodesource.list \
  && echo "deb-src https://deb.nodesource.com/$VERSION $DISTRO main" | tee -a /etc/apt/sources.list.d/nodesource.list \
  && apt-get update && apt-get install -y nodejs \
  && npm install -g npm@latest \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION" && poetry --version

# Navigate to where your package.json is located
WORKDIR /code/theme/static_src/

# Copy package.json and package-lock.json
COPY theme/static_src/package*.json ./

# Install dependencies
RUN npm install
#RUN npx update-browserslist-db@latest

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
