# -*- coding: utf-8 -*-

from socket import gethostname
from os import getpid
from threading import get_ident
from uuid import uuid4

from .Timer import SetTimer, Timeout

__all__ = (
	'GetHostName',
	'GetProcessId',
	'GetThreadId',
	'GenerateUUID',
	'SetTimer',
	'Timeout'
)


def GetHostName():
	return gethostname()


def GetProcessId():
	return getpid()


def GetThreadId():
	return get_ident()


def GenerateUUID():
	return str(uuid4()).lower().replace('-', '')
