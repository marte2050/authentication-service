FROM python:3.12-slim

LABEL maintainer="Jonathan W."
LABEL description="Dockerfile for Python 3.12 with Poetry and Ruff"

RUN apt update
RUN apt install -y pipx

RUN useradd -m -s /bin/bash chameleon
USER chameleon

RUN pipx install poetry==2.2.1
ENV PATH="/home/chameleon/.local/bin:$PATH"

WORKDIR /app
USER chameleon
COPY --chown=chameleon:chameleon ./src ./
RUN mv .env.sample.production .env
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-interaction --no-ansi --without dev --no-root
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["gunicorn", "main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]
