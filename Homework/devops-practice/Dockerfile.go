FROM golang:1.24 AS builder
WORKDIR /src
COPY main.go .
RUN go mod init demo && CGO_ENABLED=0 go build -o /server main.go

FROM gcr.io/distroless/static-debian12
COPY --from=builder /server /server
ENTRYPOINT ["/server"]
