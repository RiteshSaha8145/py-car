# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_files/unixfs.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto_files/unixfs.proto",
    package="",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x18proto_files/unixfs.proto"\xfa\x01\n\x04\x44\x61ta\x12\x1c\n\x04Type\x18\x01 \x02(\x0e\x32\x0e.Data.DataType\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\x12\x10\n\x08\x66ilesize\x18\x03 \x01(\x04\x12\x12\n\nblocksizes\x18\x04 \x03(\x04\x12\x10\n\x08hashType\x18\x05 \x01(\x04\x12\x0e\n\x06\x66\x61nout\x18\x06 \x01(\x04\x12\x0c\n\x04mode\x18\x07 \x01(\r\x12\x18\n\x05mtime\x18\x08 \x01(\x0b\x32\t.UnixTime"V\n\x08\x44\x61taType\x12\x07\n\x03Raw\x10\x00\x12\r\n\tDirectory\x10\x01\x12\x08\n\x04\x46ile\x10\x02\x12\x0c\n\x08Metadata\x10\x03\x12\x0b\n\x07Symlink\x10\x04\x12\r\n\tHAMTShard\x10\x05"\x1c\n\x08Metadata\x12\x10\n\x08MimeType\x18\x01 \x01(\t":\n\x08UnixTime\x12\x0f\n\x07Seconds\x18\x01 \x02(\x03\x12\x1d\n\x15\x46ractionalNanoseconds\x18\x02 \x01(\x07',
)


_DATA_DATATYPE = _descriptor.EnumDescriptor(
    name="DataType",
    full_name="Data.DataType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="Raw",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="Directory",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="File",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="Metadata",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="Symlink",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HAMTShard",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=193,
    serialized_end=279,
)
_sym_db.RegisterEnumDescriptor(_DATA_DATATYPE)


_DATA = _descriptor.Descriptor(
    name="Data",
    full_name="Data",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="Type",
            full_name="Data.Type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="Data",
            full_name="Data.Data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="filesize",
            full_name="Data.filesize",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="blocksizes",
            full_name="Data.blocksizes",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hashType",
            full_name="Data.hashType",
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fanout",
            full_name="Data.fanout",
            index=5,
            number=6,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="mode",
            full_name="Data.mode",
            index=6,
            number=7,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="mtime",
            full_name="Data.mtime",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _DATA_DATATYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=29,
    serialized_end=279,
)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="MimeType",
            full_name="Metadata.MimeType",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=281,
    serialized_end=309,
)


_UNIXTIME = _descriptor.Descriptor(
    name="UnixTime",
    full_name="UnixTime",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="Seconds",
            full_name="UnixTime.Seconds",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="FractionalNanoseconds",
            full_name="UnixTime.FractionalNanoseconds",
            index=1,
            number=2,
            type=7,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=311,
    serialized_end=369,
)

_DATA.fields_by_name["Type"].enum_type = _DATA_DATATYPE
_DATA.fields_by_name["mtime"].message_type = _UNIXTIME
_DATA_DATATYPE.containing_type = _DATA
DESCRIPTOR.message_types_by_name["Data"] = _DATA
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
DESCRIPTOR.message_types_by_name["UnixTime"] = _UNIXTIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType(
    "Data",
    (_message.Message,),
    {
        "DESCRIPTOR": _DATA,
        "__module__": "proto_files.unixfs_pb2"
        # @@protoc_insertion_point(class_scope:Data)
    },
)
_sym_db.RegisterMessage(Data)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    {
        "DESCRIPTOR": _METADATA,
        "__module__": "proto_files.unixfs_pb2"
        # @@protoc_insertion_point(class_scope:Metadata)
    },
)
_sym_db.RegisterMessage(Metadata)

UnixTime = _reflection.GeneratedProtocolMessageType(
    "UnixTime",
    (_message.Message,),
    {
        "DESCRIPTOR": _UNIXTIME,
        "__module__": "proto_files.unixfs_pb2"
        # @@protoc_insertion_point(class_scope:UnixTime)
    },
)
_sym_db.RegisterMessage(UnixTime)


# @@protoc_insertion_point(module_scope)
