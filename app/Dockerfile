# ベースイメージを指定
FROM python:3.11.4-slim-buster

# コンテナ内での作業ディレクトリを設定
WORKDIR /usr/src/app

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y netcat

# 依存関係をインストール
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# entrypoint.shを作業ディレクトリにコピー
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# appディレクトリ内の全てのファイルを作業ディレクトリにコピー
COPY . .

# コンテナが起動された際にシェルを実行する
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]