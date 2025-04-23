# browser-useの素振り

intel mac(x86_64)だとLLM系パッケージのサポートが厳しいためdockerを利用(具体的にはpytorch)  
alpineイメージもnvidia関連パッケージがサポートしていないため利用できなかった。

## Usage

```
$ cp example.env .env
# => .envにAPI_KEYを入力

$ docker compose build
# Dockerfile更新時
$ docker compose build --no-cache
$ docker compose up -d
$ docker compose exec app sh

$ apt-get install nodejs
$ apt-get install npm
$ npm i
$ npx playwright install-deps

$ poetry install
$ poetry run python main.py
```

## Refs
- https://qiita.com/Syoitu/items/5aa84b5d8c6047c4d41b
- https://zenn.dev/gunjo/articles/2f6898b846d371
