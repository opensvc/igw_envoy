The envoy L4-L7 auto-configuring ingress gateway to services hosted in a
OpenSVC cluster.

* Only the gateways need a public ip address, the services can use backend
  networks addresses.

* The gateway is central logging and auditing facility.

* The gateway can enforce permissions policy

* The gateway can be a TLS endpoint

* The gateway can redirect and rewrite paths

The setup of a envoy ingress gateway in a cluster is described at
https://github.com/opensvc/opensvc_templates/tree/main/igw_envoy
