# fetch the grpc lib
git clone https://github.com/ramananbalakrishnan/basic-grpc-python
cd basic-grpc-python
pip3 install -r requirements.txt

# clone the igw envoy
git clone https://github.com/opensvc/igw_envoy

# clone deps
git clone https://github.com/googleapis/googleapis
git clone https://github.com/lyft/protoc-gen-validate.git
git clone https://github.com/envoyproxy/envoy

# refresh the envoy proto files
mkdir xdsproto/
find envoy/api/envoy -name "*proto" -exec python3 -m grpc_tools.protoc -I envoy/api/ -I protoc-gen-validate/ -I googleapis/ --python_out=xdsproto/ --grpc_python_out=xdsproto/ {} \;
rm -rf igw_envoy/src/envoy/
cp xdsproto/envoy igw_envoy/src/

# test the xDS
GRPC_TRACE=server_channel GRPC_VERBOSITY=DEBUG ./xds
