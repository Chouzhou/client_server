# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  serialized_pb='\n\rmessage.proto\x12\x07message\"\x1d\n\x0eMessageRequest\x12\x0b\n\x03msg\x18\x01 \x01(\x05\" \n\x0fMessageResponse\x12\r\n\x05remsg\x18\x01 \x01(\x05')




_MESSAGEREQUEST = _descriptor.Descriptor(
  name='MessageRequest',
  full_name='message.MessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='message.MessageRequest.msg', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=26,
  serialized_end=55,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='message.MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remsg', full_name='message.MessageResponse.remsg', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=57,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['MessageRequest'] = _MESSAGEREQUEST
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE

class MessageRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGEREQUEST

  # @@protoc_insertion_point(class_scope:message.MessageRequest)

class MessageResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGERESPONSE

  # @@protoc_insertion_point(class_scope:message.MessageResponse)


# @@protoc_insertion_point(module_scope)
