FROM python:3.13.3

# Pythonの出力表示をDocker用に設定
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./
RUN poetry install --no-root

RUN apt-get install nodejs
RUN apt-get install npm

COPY package.json* package-lock.json* ./
RUN npm i
RUN npx playwright install
