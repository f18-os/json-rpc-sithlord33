import socket
import localDemo
import node

from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)

@service_class
class ServerServices(object):

  @request
  def increment(self, txt):
    root = localDemo.buildJson(txt)
    root.show()
    node.increment(root)
    root.show()
    txt = localDemo.Jstring(root)
    return txt
    
  @request
  def nop(self, txt):
    print(txt)
    return txt

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
