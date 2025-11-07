# Dockerfile for mygo image
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 golang
WORKDIR mydev
COPY echob.py echob.go ./
RUN chmod +x echob.py
ENTRYPOINT ["/usr/bin/go", "run", "echob.go"]
CMD ["one", "two", "three"]
#CMD ["/bin/bash"]
