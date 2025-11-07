# Dockerfile for COPY instruction
FROM ubuntu
COPY testfile* /
COPY mydir /images
COPY --chown=10:20 mycert /
CMD ["/bin/bash"]
