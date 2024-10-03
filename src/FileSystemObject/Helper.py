# -*- coding: utf-8 -*-

from ..Template import Singleton

from .Connection import Connection
from .Configuration import Configuration

from .Errors import *

from typing import Type

__all__ = (
    'Helper'
)


class Helper(Singleton):
    """File System Object Helper Class"""
    """
    Sample:
        Helper.Set('Sample', YourFileSystemObject, YourConfiguration('/path/to'))
        fo = Helper.Get('Sample')
        with fo.open('/path/to') as f:
            print(f.read())
            f.close()
    """
    def __init__(self):
        self.objects = {}
        return

    @classmethod
    def Set(cls, key, o: Type[Connection], conf: Configuration):
        helper = cls()
        return helper.set(key, o, conf)

    def set(self, key, o: Type[Connection], conf: Configuration):
        if not isinstance(o, type):
            raise InvalidParametersError('o is not Connection')
        self.objects[key] = (o, conf)
        return

    @classmethod
    def Get(cls, key):
        helper = cls()
        return helper.get(key)

    def get(self, key):
        if key not in self.objects:
            return None
        o = self.objects[key][0](self.objects[key][1])
        o.connect()
        return o
