# Makefile for Volume binds

all: run

run:
	docker container run -d --name volc --mount type=bind,\
source=`pwd`/data,target=/app alpine tail -f /dev/null

clean:
	docker stop volc
	docker container prune -f
	docker image prune -f
