import socket
import json
import localDemo

from node import *
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])
print("graph before increment")
root.show()

result = localDemo.Jstring(root)
result = server.increment(result)

root = localDemo.buildJson(result)
print("graph after increment")
root.show()

print(server.nop({1:[2,3]}))

rpc.close() # Closes the socket 's' also
