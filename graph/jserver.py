import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
    JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

@service_class
class ServerServices(object):

    @request
    def swapper(self, txt):
        return ''.join(reversed(list(txt)))

    @request
    def pop(self, txt):
        print(txt)
        return txt

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
    s, _ = ss.accept()
    JSONpc(s, ServerServices(),framing_cls_JSONFramingNone)
