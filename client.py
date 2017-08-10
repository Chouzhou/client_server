#-*- coding: utf-8 -*-
__all__ = ['Client']


import go.logging
import go.rpc
import go.protobuf
import go.timer

from service_pb2 import Service
from message_pb2 import MessageResponse
from agent import Agent

import sys
if 'threading' in sys.modules:
    del sys.modules['threading']
import gevent
import gevent.socket
import gevent.monkey
gevent.monkey.patch_all()

@go.rpc.index_method
@go.rpc.impl
class ClientIml(Service):
    
    # def __init__(self):
    #     self(ClientIml, self).__init__()
    
    @go.rpc.ret
    def get_msg(self):
        request = MessageRequest()
        request.msg = 'hello world!'
        # response = request.msg
        return request


@go.logging.class_wrapper
class Client(go.rpc.ClientFactory):
    def __init__(self, agent):
        self._agent = agent
        service_repository = go.protobuf.ServiceRepository()
        service_repository.register_service(ClientIml())
        self.logger.debug('register client service')

        super(Client, self).__init__(service_repository)

    def on_start(self):
        db_addr = ('localhost', 8007)
        self.connect(db_addr)
        

    def on_stop(self):
        pass

    def connection_made(self, conn, channel, *args, **kwargs):
        conn = self.connect(('localhost', 8007))
        conn.factory = self
        service_proxy = go.rpc.ServiceProxy(conn,
                                    self.service_repository,
                                    factory=self)
        channel = service_proxy.channel
        super(Client, self).connection_made(conn, channel)
        conn.client_name = Client.__name__
        self.logger.info('connection to [data|%s] made', conn.getpeername())
        self._agent.connect(channel)
        msg = 'hello world!'
        self._agent.send_msg(msg)

    def connection_lost(self, conn, reason):
        self._data_agent.disconnect()

        if reason:
            self.logger.error('connection to [data|%s] lost with [reason|%s]', conn.getpeername(),
                              reason)  # pragma: no cover
        else:
            self.logger.info('connection to [data|%s] closed cleanly', conn.getpeername())
        super(Client, self).connection_lost(conn, reason)
        sys.exit(3)

    def connection_failed(self, remote_addr, reason):
        self.logger.error('connection to [data|%s] failed with [reason|%s]', remote_addr, reason)
        super(Client, self).connection_failed(remote_addr, reason)
        self.logger.error('failed to connect data server, just quit activity')
        sys.exit(1)

if __name__ == '__main__':
    client = Client(Agent)
    # client.create_connection('localhost:8007', 12, 24)
    client.on_start()
    # client.send()
