# -*- coding: utf-8 -*-

from ..Template import Singleton

from .Context import Context

from typing import Type, Optional, Any

__all__ = (
	'Helper'
)


class Helper(Singleton):
	def __init__(self):
		# TODO : contexts have to share in each threads and process with Proxy
		self.contexts = {}
		return
	
	def set(self, key: str, context: Type[Context], *args, **kwargs):
		self.contexts[key] = (context, args, kwargs, None)
		return
	
	@classmethod
	def Set(cls, key: str, context: Type[Context], *args, **kwargs):
		_ = cls()
		return _.set(key, context, *args, **kwargs)
	
	def get(self, key: str) -> Optional[Context]:
		if key not in self.contexts: return None
		O, args, kwargs, o = self.contexts[key]
		if not o:
			o = O(*args, **kwargs)
			self.contexts[key] = (O, args, kwargs, o)
		return o
	
	@classmethod
	def Get(cls, key: str) -> Optional[Context]:
		_ = cls()
		return _.get(key)
	
	def setValue(self, key: str, k: Any, v: Any, expires: int = None):
		context = self.get(key)
		if not context: return
		context.set(k, v, expires)
		return
	
	@classmethod
	def SetValue(cls, key: str, k: Any, v: Any, expires: int = None):
		_ = cls()
		return _.setValue(key, k, v, expires)

	def getValue(self, key: str, k: Any) -> Optional[Any]:
		context = self.get(key)
		if not context: return None
		return context.get(k)
	
	@classmethod
	def GetValue(cls, key: str, k: Any) -> Optional[Any]:
		_ = cls()
		return _.getValue(key, k)
