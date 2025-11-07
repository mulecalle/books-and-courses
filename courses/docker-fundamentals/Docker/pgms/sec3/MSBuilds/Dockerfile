# Multi-stage build
#FROM ubuntu:latest
FROM ubuntu:latest AS compile-image
RUN apt-get update && apt-get install -y gcc
WORKDIR /root
COPY greeting.c .
RUN gcc greeting.c -o greeting
FROM ubuntu:latest AS runtime-image
COPY --from=compile-image /root/greeting .
CMD ["./greeting"]
