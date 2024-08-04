# -*- coding: utf-8 -*-

from ..Type import Type

from copy import deepcopy

__all__ = (
	'Object'
)


class Object(Type):
	"""Object Data Type Object Class of Data Model Object"""

	def __getattr__(self, key):
		if key in ('__value__', '__attr__', '__model__'):
			return super(Object, self).__getattr__(key)
		return Type.Create(
			self.__value__.__getattr__(key),
			self.__attr__,
			self.__model__,
		)

	def __setattr__(self, key, value):
		if key in ('__value__', '__attr__', '__model__'):
			return super(Object, self).__setattr__(key, value)
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
		try:
			setattr(self.__value__, key, value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__, 
					self.__attr__.name, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			setattr(self.__value__, key, pv)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return 

