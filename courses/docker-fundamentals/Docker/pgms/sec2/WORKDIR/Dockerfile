# Dockerfile for WORKDIR instruction 
FROM busybox
WORKDIR /usr/paul/music
WORKDIR jazz
WORKDIR rock
ENV SRC_DIR=/usr/paul/myfiles
WORKDIR $SRC_DIR
COPY data $SRC_DIR
CMD ["/bin/sh"]
