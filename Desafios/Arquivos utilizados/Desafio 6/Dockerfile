FROM golang:1.19 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY *.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o docker-gs-ping

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/docker-gs-ping .
EXPOSE 8080
CMD [ "/docker-gs-ping" ]
