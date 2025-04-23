FROM python:3.13.3

# Pythonの出力表示をDocker用に設定
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

