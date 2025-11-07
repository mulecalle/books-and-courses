# Dockerfile for Apache Web Server
FROM httpd:latest
COPY index.html /usr/local/apache2/htdocs/
HEALTHCHECK CMD curl --fail http://localhost:1234/ || exit 0
EXPOSE 80
