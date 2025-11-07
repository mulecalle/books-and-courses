# Use ubuntu:latest as your base image.
FROM ubuntu:latest

# Use apt-get update and apt-get install to install python3 and golang in your image.
RUN apt-get update
RUN apt-get install python3 --yes
RUN apt-get install golang --yes

# Make mydev your working directory
WORKDIR /mydev

# Copy echob.py and echob.go in your exer/mygo directory to the mydev directory inside your container.

COPY echob.py /mydev
COPY echob.go /mydev

#• Use chmod +x to make echob.py executable.

RUN ["/bin/chmod", "+x", "echob.py"]


# • Use ENTRYPOINT with go run and echob.go. Replace CMD with the program’s arg’s.
ENTRYPOINT ["go", "run", "echob.go"]

#• Make /bin/bash your default command.
CMD ["one", "two", "three"]
