# fetch the grpc lib
git clone https://github.com/ramananbalakrishnan/basic-grpc-python
cd basic-grpc-python
pip3 install -r requirements.txt

# compile the envoy proto files
find . -name "*proto" -exec python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. {} \;

# test the xDS
GRPC_TRACE=server_channel GRPC_VERBOSITY=DEBUG ./xds
