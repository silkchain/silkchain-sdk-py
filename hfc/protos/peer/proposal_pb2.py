# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/proposal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.peer import chaincode_pb2 as hfc_dot_protos_dot_peer_dot_chaincode__pb2
from hfc.protos.peer import proposal_response_pb2 as hfc_dot_protos_dot_peer_dot_proposal__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/proposal.proto',
  package='hfc.protos.peer',
  syntax='proto3',
  serialized_pb=_b('\n\x1ehfc/protos/peer/proposal.proto\x12\x0fhfc.protos.peer\x1a\x1fhfc/protos/peer/chaincode.proto\x1a\'hfc/protos/peer/proposal_response.proto\";\n\x0eSignedProposal\x12\x16\n\x0eproposal_bytes\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\">\n\x08Proposal\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x11\n\textension\x18\x03 \x01(\x0c\"j\n\x18\x43haincodeHeaderExtension\x12\x1a\n\x12payload_visibility\x18\x01 \x01(\x0c\x12\x32\n\x0c\x63haincode_id\x18\x02 \x01(\x0b\x32\x1c.hfc.protos.peer.ChaincodeID\"<\n\x18\x43haincodeProposalPayload\x12\r\n\x05input\x18\x01 \x01(\x0c\x12\x11\n\ttransient\x18\x02 \x01(\x0c\"_\n\x0f\x43haincodeAction\x12\x0f\n\x07results\x18\x01 \x01(\x0c\x12\x0e\n\x06\x65vents\x18\x02 \x01(\x0c\x12+\n\x08response\x18\x03 \x01(\x0b\x32\x19.hfc.protos.peer.ResponseB+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_peer_dot_chaincode__pb2.DESCRIPTOR,hfc_dot_protos_dot_peer_dot_proposal__response__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGNEDPROPOSAL = _descriptor.Descriptor(
  name='SignedProposal',
  full_name='hfc.protos.peer.SignedProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal_bytes', full_name='hfc.protos.peer.SignedProposal.proposal_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='hfc.protos.peer.SignedProposal.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=184,
)


_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='hfc.protos.peer.Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='hfc.protos.peer.Proposal.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='hfc.protos.peer.Proposal.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension', full_name='hfc.protos.peer.Proposal.extension', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=248,
)


_CHAINCODEHEADEREXTENSION = _descriptor.Descriptor(
  name='ChaincodeHeaderExtension',
  full_name='hfc.protos.peer.ChaincodeHeaderExtension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload_visibility', full_name='hfc.protos.peer.ChaincodeHeaderExtension.payload_visibility', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chaincode_id', full_name='hfc.protos.peer.ChaincodeHeaderExtension.chaincode_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=356,
)


_CHAINCODEPROPOSALPAYLOAD = _descriptor.Descriptor(
  name='ChaincodeProposalPayload',
  full_name='hfc.protos.peer.ChaincodeProposalPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='hfc.protos.peer.ChaincodeProposalPayload.input', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transient', full_name='hfc.protos.peer.ChaincodeProposalPayload.transient', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=418,
)


_CHAINCODEACTION = _descriptor.Descriptor(
  name='ChaincodeAction',
  full_name='hfc.protos.peer.ChaincodeAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='hfc.protos.peer.ChaincodeAction.results', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events', full_name='hfc.protos.peer.ChaincodeAction.events', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='hfc.protos.peer.ChaincodeAction.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=515,
)

_CHAINCODEHEADEREXTENSION.fields_by_name['chaincode_id'].message_type = hfc_dot_protos_dot_peer_dot_chaincode__pb2._CHAINCODEID
_CHAINCODEACTION.fields_by_name['response'].message_type = hfc_dot_protos_dot_peer_dot_proposal__response__pb2._RESPONSE
DESCRIPTOR.message_types_by_name['SignedProposal'] = _SIGNEDPROPOSAL
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL
DESCRIPTOR.message_types_by_name['ChaincodeHeaderExtension'] = _CHAINCODEHEADEREXTENSION
DESCRIPTOR.message_types_by_name['ChaincodeProposalPayload'] = _CHAINCODEPROPOSALPAYLOAD
DESCRIPTOR.message_types_by_name['ChaincodeAction'] = _CHAINCODEACTION

SignedProposal = _reflection.GeneratedProtocolMessageType('SignedProposal', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDPROPOSAL,
  __module__ = 'hfc.protos.peer.proposal_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.SignedProposal)
  ))
_sym_db.RegisterMessage(SignedProposal)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSAL,
  __module__ = 'hfc.protos.peer.proposal_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.Proposal)
  ))
_sym_db.RegisterMessage(Proposal)

ChaincodeHeaderExtension = _reflection.GeneratedProtocolMessageType('ChaincodeHeaderExtension', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEHEADEREXTENSION,
  __module__ = 'hfc.protos.peer.proposal_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeHeaderExtension)
  ))
_sym_db.RegisterMessage(ChaincodeHeaderExtension)

ChaincodeProposalPayload = _reflection.GeneratedProtocolMessageType('ChaincodeProposalPayload', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEPROPOSALPAYLOAD,
  __module__ = 'hfc.protos.peer.proposal_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeProposalPayload)
  ))
_sym_db.RegisterMessage(ChaincodeProposalPayload)

ChaincodeAction = _reflection.GeneratedProtocolMessageType('ChaincodeAction', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEACTION,
  __module__ = 'hfc.protos.peer.proposal_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.peer.ChaincodeAction)
  ))
_sym_db.RegisterMessage(ChaincodeAction)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)