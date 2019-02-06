from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from genpy.hello import helloSvc




try:
    transport=TSocket.TSocket('localhost', 9090)
    transport=TTransport.TBufferedTransport(transport)
    protocol=TBinaryProtocol.TBinaryProtocol(transport)
    client=helloSvc.Client(protocol)
    transport.open()
    str=client.getMessage("keerthi")
    print ("[Python Client] received: " + str)
    transport.close()

except Thrift.TException as tx:
    print(tx.message)
