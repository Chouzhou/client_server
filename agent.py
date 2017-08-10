__all__ = ['AbstractDataAgent', 'DataAgent']

import collections

import go.util
import go.logging

from service_pb2 import Service_Stub
from message_pb2 import MessageRequest


# @aop.trace_service_stub
@go.logging.class_wrapper
class Service_Stub(Service_Stub):
    pass

class AbstractDataAgent(object):
    pass


@go.logging.class_wrapper
class Agent(AbstractDataAgent):
    
    def __init__(self, fishing_id, room_manager, player_agent_manager, pool_agent_manager):
        self._msg = msg
        self._connected = False        
        self._pending_requests = 0
        self._object_mapper = go.util.ObjectMapper()
        self.unbind_channel()

    @property
    def msg(self):
        return self.msg

    @property
    def pending_requests(self):
        return self._pending_requests

    def bind_channel(self, channel):
        self._proxy = go.protobuf.Proxy(Service_Stub(channel))

    def unbind_channel(self):
        self._proxy = go.protobuf.NullProxy()

    def connect(self, channel):
        self.logger.info('[fishing|%d] connected to data server', self._fishing_id)
        assert not self._connected
        self.bind_channel(channel)
        self._connected = True

    def disconnect(self):
        self.logger.info('[fishing|%d] disconnected to data server', self._fishing_id)
        assert self._connected
        self.unbind_channel() 
        self._connected = False

    @property
    def connected(self):
        return self._connected

    def send_msg(self, msg):
        request = Request()
        request.msg = msg        
        self._proxy.get_msg(request)   
