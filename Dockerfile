FROM tirz/alpine-python3-protobuf

LABEL maintainer="support@opensvc.com"

RUN apk update
RUN apk upgrade

RUN apk add --no-cache --virtual g++ libstdc++
RUN apk add --no-cache --virtual python3-dev

RUN pip3 install --no-cache-dir grpcio

RUN apk del python3-dev
RUN apk del g++

COPY src /usr/share/igw_envoy

ENTRYPOINT ["/usr/share/igw_envoy/xds"]

