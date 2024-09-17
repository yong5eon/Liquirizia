# -*- coding: utf-8 -*-

from ..Type import Type
from ..Model import Model

from collections.abc import MutableMapping

from copy import deepcopy

__all__ = (
	'Dictionary'
)


class Dictionary(Type, MutableMapping):
	"""Dictionary Data Type Object Class of Data Model Object"""

	# def __getattr__(self, name):
	#	 return self.__value__.__getattr__(name)

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__value__.__repr__()[1:-1]
		)

	def __str__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			self.__value__.__repr__()[1:-1]
		)

	def __contains__(self, key):
		return self.__value__.__contains__(key)
	
	def __len__(self):
		return self.__value__.__len__()

	def __iter__(self):
		return self.__value__.__iter__()
	
	def __getitem__(self, key):
		return Type.Create(
			self.__value__.__getitem__(key) if key in self.__value__.keys() else None,
			self.__attr__,
			self.__model__,
		)

	def __setitem__(self, key, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__setitem__(key, value)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__.__class__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def __delitem__(self, key):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__delitem__(key)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__.__object__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def __eq__(self, other: object) -> bool:
		if isinstance(other, Dictionary): return self.__value__.__eq__(other.__value__)
		if isinstance(other, Model): return self.__value__.__eq__(other.__object__)
		return self.__value__.__eq__(other)
	
	def __ne__(self, other: object) -> bool:
		if isinstance(other, Dictionary): return self.__value__.__ne__(other.__value__)
		if isinstance(other, Model): return self.__value__.__ne__(other.__object__)
		return self.__value__.__ne__(other)
	
	def keys(self):
		return self.__value__.keys()
	
	def items(self):
		return self.__value__.items()
	
	def values(self):
		return self.__value__.values()

	def clear(self) -> None:
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.clear()
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__.__object__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def update(self, other):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__attr__.__getitem__(self.__attr__.name))
			self.__value__.update(other)
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				self.__attr__.validator(self.__model__.__object__.__getitem__(self.__attr__.name))
			)
			if self.__attr__.callback:
				self.__attr__.callback(
					self.__model__.__class__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	