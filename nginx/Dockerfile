# ベースイメージを指定
FROM nginx:1.25

# Nginsの設定をカスタマイズしてる
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d