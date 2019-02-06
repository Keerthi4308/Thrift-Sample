from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.server import TServer
from thrift.protocol import TBinaryProtocol


from genpy.hello import helloSvc

class ExampleHandler:
    def __init__(self):
        self.log = {}

    def getMessage(self,msg):
        print(msg)
        return "Hello " +msg


handler = ExampleHandler()
processor = helloSvc.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")
