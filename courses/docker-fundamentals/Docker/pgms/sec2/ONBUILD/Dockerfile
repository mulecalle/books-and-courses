# Dockerfile for ONBUILD instruction
FROM ubuntu
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ONBUILD COPY package.json .
ONBUILD COPY install.sh .
ONBUILD RUN ./install.sh > log
CMD ["/bin/bash"]
