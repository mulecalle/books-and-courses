# Dockerfile for RUN instruction
FROM ubuntu
RUN mkdir /mydir
RUN echo "Here is line one." > /mydir/myfile
RUN ["/bin/chmod", "664", "/mydir/myfile"]
RUN ["/bin/bash", "-c", \
    "echo Here is line two. >> /mydir/myfile"]
WORKDIR /mydir
CMD ["/bin/bash"]
