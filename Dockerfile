FROM python:3-alpine

LABEL maintainer="support@opensvc.com"

RUN apk update
RUN apk upgrade

RUN apk add --no-cache libstdc++
RUN apk add --no-cache --virtual .build-deps g++ gcc musl-dev python3-dev linux-headers
RUN pip3 install --no-cache-dir protobuf grpcio requests

RUN apk del python3-dev .build-deps g++ gcc musl-dev python3-dev linux-headers

COPY src /usr/share/igw_envoy

ENTRYPOINT ["/usr/share/igw_envoy/xds"]

