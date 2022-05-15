FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir /etc/nginx/templates
COPY nginx.conf.template /etc/nginx/templates
RUN envsubst < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/nginx.conf