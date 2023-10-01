FROM golang:1.20.6-alpine3.17 AS build

WORKDIR /code
COPY ./go.mod ./go.sum ./
RUN go mod download

COPY backend_app backend_app
RUN go build -o backend backend_app/main.go

FROM alpine:3.17

WORKDIR /code
COPY --from=build /code/backend /code/backend
EXPOSE 8080

RUN adduser -D nonroot
USER nonroot

CMD ["/code/backend"]