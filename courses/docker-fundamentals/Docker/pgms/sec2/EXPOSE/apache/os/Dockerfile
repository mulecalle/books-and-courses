# Dockerfile for Apache Web Server
FROM ubuntu 
RUN apt update && apt upgrade -y 
RUN apt install -y apache2 apache2-utils 
RUN apt clean 
COPY index.html /var/www/html/
EXPOSE 80 
CMD apache2ctl -DFOREGROUND
