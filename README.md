### Development

デフォルトのDjango開発サーバを使用します

1. .env.devファイルを追加します
2. イメージをビルドし、コンテナーを実行します

```sh
$ docker-compose up -d --build
```

[http://localhost:8000](http://localhost:8000)でテストしてください<br>
「app」ディレクトリがコンテナーにマウントされ、コードの変更が自動的に適用されます

### Production

GunicornとNginxを使用します

1. docker-compose.prod.yml、.env.prod、.env.prod.dbファイル内の環境変数を更新します
2. イメージをビルドし、コンテナーを実行します

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```

[http://localhost:1337](http://localhost:1337)でテストしてください<br>
マウントされたディレクトリはありません。変更を適用するには、イメージを再構築する必要があります