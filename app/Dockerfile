FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libglib2.0-0 \
    libcairo2 \
    fonts-dejavu \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . /app
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.6.12 /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12

RUN --mount=type=cache,target=/root/.cache \
    set -ex \
    && uv venv /app/.venv

RUN --mount=type=cache,target=/root/.cache \
    set -ex \
    && uv sync --frozen --no-install-project

EXPOSE 8000
