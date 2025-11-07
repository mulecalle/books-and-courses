# Dockerfile - Multi-stage build
FROM golang:alpine AS builder
COPY hello.go /app/
WORKDIR /app
ENV CGO_ENABLED=0
RUN go build hello.go
EXPOSE 8080

#FROM alpine:latest
FROM scratch
COPY --from=builder /app/hello .
CMD ["./hello"]
