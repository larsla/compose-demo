FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD vhost.conf /etc/nginx/conf.d/vhost.conf
ADD html /www

CMD ["nginx", "-q"]
