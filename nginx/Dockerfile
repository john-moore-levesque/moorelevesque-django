FROM nginx:1.21-alpine

RUN apk add certbot certbot-nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

RUN certbot certonly --standalone --agree-tos -m "${CERTBOT_EMAIL}" -n -d "${DOMAIN_LIST}"
RUN echo "PATH=$PATH" > /etc/cron.d/certbot-renew
RUN echo "@monthly certbot renew --nginx >> /var/log/cron.log 2>&1" >> /etc/cron.d/certbot-renew
RUN crontab /etc/cron.d/certbot-renew