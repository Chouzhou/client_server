from service_pb2 import Service
from message_pb2 import MessageRequest
import go.protobuf
import go.rpc
import go.logging

@go.rpc.index_method
@go.rpc.impl
class ServiceImpl(Service):
    
    # def __init__(self):
    #     self(ServiceImpl, self).__init__()

    @go.rpc.ret    
    def get_msg(self, controller, request):
        request = Request()
        msg = request.msg
        print request.msg


@go.logging.class_wrapper
class Server(go.rpc.ServerFactory):
    def __init__(self):
        self.service_repository = go.protobuf.ServiceRepository()
        self.service_repository.register_service(ServiceImpl())
        self.logger.debug('register service')
        listen_addr = ('127.0.0.1', 8007)
        super(Server, self).__init__(listen_addr, self.service_repository)        

    def connection_made(self, conn, channel):
        super(Server, self).connection_made(conn, channel)

    def connection_lost(self, conn, reason):
        super(Server, self).connection_lost(conn, reason)

    def on_start(self):
        pass

    def on_stop(self):
        pass


Server().serve_forever()
