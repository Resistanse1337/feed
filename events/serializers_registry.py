from rest_framework import serializers
from rest_framework.serializers import SerializerMetaclass


class SerializersRegistry(SerializerMetaclass):
    SERIALIZERS = {}

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.SERIALIZERS[new_cls.__name__] = new_cls
        return new_cls
    
    @classmethod
    def get_serializer(cls, serializer_name) -> type[serializers.ModelSerializer]:
        return cls.SERIALIZERS[serializer_name]
