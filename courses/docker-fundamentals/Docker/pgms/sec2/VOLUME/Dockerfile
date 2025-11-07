# Dockerfile for VOLUME instruction
FROM alpine
RUN mkdir /myvol
RUN echo "this is some text" > /myvol/data
VOLUME /myvol
CMD ["/bin/sh"]
