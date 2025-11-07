# Dockerfile - Single Stage
FROM golang:alpine as base

COPY hello.go /app/
ENV CGO_ENABLED=0
WORKDIR /app
RUN go build hello.go

FROM scratch as run
EXPOSE 8080
COPY --from=base /app/hello ./hello

CMD ["./hello"]
