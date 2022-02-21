FROM alpine

LABEL maintainer="support@opensvc.com"

RUN apk update; apk upgrade; apk add py3-grpcio py3-requests py3-six py3-protobuf py3-googleapis-common-protos

COPY src /usr/share/igw_envoy

ENTRYPOINT ["/usr/share/igw_envoy/xds"]

