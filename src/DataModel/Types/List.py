# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableSequence

from copy import deepcopy

__all__ = (
	'List'
)


class List(Type, MutableSequence):
	"""List Data Type Object Class of Data Model Object"""

	# def __getattr__(self, name):
	#	 return self.__value__.__getattr__(name)
 
	def __iter__(self):
		return self.__value__.__iter__()
	
	def __reserved__(self):
		return self.__value__.__reserved__()
	
	def __len__(self):
		return self.__value__.__len__()
	
	def __contains__(self, value):
		return self.__value__.__contains__(value)

	def __getitem__(self, key):
		return Type.Create(
			self.__value__.__getitem__(key) if key < len(self.__value__) else None,
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
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
					self.__model__.__class__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def __iadd__(self, values):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.__iadd__(values)
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def index(self, value: any, start: int = 0, stop: int = ...) -> int:
		return self.__value__.index(value, start, stop)
	
	def count(self, value: any) -> int:
		return self.__value__.count(value)

	def insert(self, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.insert(value)
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self

	def append(self, value):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.append(value)
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def clear(self):
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
					self.__model__.__class__, 
					self.__model__,
					self.__attr__, 
					self.__model__.__object__.__getitem__(self.__attr__.name),
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def reverse(self):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.reverse()
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return self
	
	def extend(self, values):
		try:
			pv = deepcopy(self.__value__)
			po = deepcopy(self.__model__.__object__.__getitem__(self.__attr__.name))
			self.__value__.extend(values)
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def remove(self, value):
		pv = deepcopy(self.__value__)
		po = deepcopy(self.__attr__.__getitem__(self.__attr__.name))
		try:
			self.__value__.remove(value)
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
					po,
				)
		except Exception as e:
			self.__value__ = pv
			self.__model__.__object__.__setitem__(
				self.__attr__.name,
				po
			)
			raise e
		return
	
	def pop(self, key: int = -1):
		return Type.Create(
			self.__value__.pop(key),
			self.__attr__,
			self.__model__,
		)

	def __eq__(self, other: any) -> bool:
		if isinstance(other, List): return self.__value__.__eq__(other.__value__)
		return self.__value__.__eq__(other)
	
	def __ne__(self, other: any) -> bool:
		if isinstance(other, List): return self.__value__.__ne__(other.__value__)
		return self.__value__.__ne__(other)