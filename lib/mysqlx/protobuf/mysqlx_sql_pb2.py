# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_sql.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mysqlx.protobuf import mysqlx_datatypes_pb2 as mysqlx__datatypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_sql.proto',
  package='Mysqlx.Sql',
  syntax='proto2',
  serialized_pb=_b('\n\x10mysqlx_sql.proto\x12\nMysqlx.Sql\x1a\x16mysqlx_datatypes.proto\"y\n\x0bStmtExecute\x12\x16\n\tnamespace\x18\x03 \x01(\t:\x03sql\x12\x0c\n\x04stmt\x18\x01 \x02(\x0c\x12#\n\x04\x61rgs\x18\x02 \x03(\x0b\x32\x15.Mysqlx.Datatypes.Any\x12\x1f\n\x10\x63ompact_metadata\x18\x04 \x01(\x08:\x05\x66\x61lse\"\x0f\n\rStmtExecuteOkB\x1e\n\x1c\x63om.mysql.cj.mysqlx.protobuf')
  ,
  dependencies=[mysqlx__datatypes__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STMTEXECUTE = _descriptor.Descriptor(
  name='StmtExecute',
  full_name='Mysqlx.Sql.StmtExecute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='Mysqlx.Sql.StmtExecute.namespace', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("sql").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmt', full_name='Mysqlx.Sql.StmtExecute.stmt', index=1,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='Mysqlx.Sql.StmtExecute.args', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compact_metadata', full_name='Mysqlx.Sql.StmtExecute.compact_metadata', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=177,
)


_STMTEXECUTEOK = _descriptor.Descriptor(
  name='StmtExecuteOk',
  full_name='Mysqlx.Sql.StmtExecuteOk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=194,
)

_STMTEXECUTE.fields_by_name['args'].message_type = mysqlx__datatypes__pb2._ANY
DESCRIPTOR.message_types_by_name['StmtExecute'] = _STMTEXECUTE
DESCRIPTOR.message_types_by_name['StmtExecuteOk'] = _STMTEXECUTEOK

StmtExecute = _reflection.GeneratedProtocolMessageType('StmtExecute', (_message.Message,), dict(
  DESCRIPTOR = _STMTEXECUTE,
  __module__ = 'mysqlx_sql_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Sql.StmtExecute)
  ))
_sym_db.RegisterMessage(StmtExecute)

StmtExecuteOk = _reflection.GeneratedProtocolMessageType('StmtExecuteOk', (_message.Message,), dict(
  DESCRIPTOR = _STMTEXECUTEOK,
  __module__ = 'mysqlx_sql_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Sql.StmtExecuteOk)
  ))
_sym_db.RegisterMessage(StmtExecuteOk)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.mysql.cj.mysqlx.protobuf'))
# @@protoc_insertion_point(module_scope)