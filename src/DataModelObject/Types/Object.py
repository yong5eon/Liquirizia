# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject

__all__ = (
	'Object'
)


class Object(DataTypeObject):
	"""Object Data Type Object Class of Data Model Object"""

	def __getattr__(self, key):
		def observe(o: DataTypeObject, fn: callable):
			def wrapper(*args, **kwargs):
				try:
					prev = self.__model__.__object__.__getitem__(self.__object__.name)
					res = fn(*args, **kwargs)
					self.__model__.__object__.__setitem__(
						self.__object__.name,
						self.__object__.validator(self.__model__.__object__.__getitem__(self.__object__.name))
					)
					if self.__object__.callback:
						self.__object__.callback(
							self.__model__, 
							self.__object__.name, 
							self.__model__.__object__.__getitem__(self.__object__.name),
							prev
						)
					return res
				except Exception as e:
					self.__model__.__object__.__setitem__(
						self.__object__.name,
						prev
					)
					raise e
			return wrapper
		attr = getattr(self.__value__, key)
		if key in (
			'append', 'extend', 'insert', 'remove', 'pop', 'sort', 'reverse',  # list
			'clear', 'pop', 'update',  # dict
		):
			return observe(self, attr)
		return attr

	def __setattr__(self, key, value):
		if key in ('__value__', '__object__', '__model__'):
			return super(Object, self).__setattr__(key, value)
		prev = self.__model__.__object__.__getitem__(self.__object__.name)
		setattr(self.__value__, key, value)
		if self.__object__.callback:
			self.__object__.callback(
				self.__model__, 
				self.__object__.name, 
				self.__model__.__object__.__getitem__(self.__object__.name),
				prev,
			)
		return 

