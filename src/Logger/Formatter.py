# -*- coding: utf-8 -*-

from enum import Enum
from abc import ABCMeta, abstractmethod
from typing import Union

__all__ = (
	'Formatter'
	'Token',
)

class Formatter(metaclass=ABCMeta):
	"""Log Formatter Interface"""
	@abstractmethod
	def __call__(self, record) -> str:
		raise NotImplemented('{} must be implemented __call__'.format(self.__class__.__name__))


class Token(str, Enum):
	Time = 'asctime'
	Level = 'levelname'
	Name = 'name'
	File = 'filename'
	Line = 'lineno'
	FileInfo = 'fileinfo'
	Function = 'funcName'
	Module = 'module'
	Process = 'process'
	ProcessName = 'processName'
	Thread = 'thread'
	ThreadName = 'threadName'
	Message = 'message'
	def __str__(self): return self.value

	@classmethod
	def FormatStr(cls, token: Union[str, 'Token'], size: int = None, align: str = None) -> str:
		"""Format string for log record"""
		if size and size > 0:
			return '%({}){}{}s'.format(str(token), align if align else '', size)
		else:
			return '%({})s'.format(str(token))
