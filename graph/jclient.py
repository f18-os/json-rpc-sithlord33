import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
    JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

result = server.swapper('Hello World!')

print(result)

print(server.nop({1:[2,3]}))

rpc.close()
