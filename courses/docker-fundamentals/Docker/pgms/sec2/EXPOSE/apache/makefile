# Makefile for Apache Web Server

all: image run

image:
	docker build -t apache .
run:
	docker run -d --name webserver -p 1234:80 apache
clean:
	docker stop webserver
	docker container prune -f
	docker image prune -f
