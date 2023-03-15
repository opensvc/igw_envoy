FROM alpine

LABEL maintainer="support@opensvc.com"
LABEL org.opencontainers.image.source="https://github.com/opensvc/igw_envoy"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.description="A container to stream configuration to a envoy proxy acting as a L4-L7 ingress gateway for a OpenSVC cluster."

RUN apk update; apk upgrade; apk add py3-grpcio py3-requests py3-six py3-protobuf py3-googleapis-common-protos

COPY src /usr/share/igw_envoy

ENTRYPOINT ["/usr/share/igw_envoy/xds"]

