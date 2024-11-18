# -*- coding: utf-8 -*-

from ..Type import Type

from collections.abc import MutableMapping

from copy import deepcopy

__all__ = (
	'Dictionary'
)

class Dictionary(Type, MutableMapping):
	"""Dictionary Data Type Object Class of Data Model Object"""

	def __contains__(self, key):
		return self.__value__.__contains__(key)
	
	def __len__(self):
		return self.__value__.__len__()

	def __iter__(self):
		return self.__value__.__iter__()
	
	def __getitem__(self, key):
		return Type.Create(
			self.__value__.__getitem__(key) if key in self.__value__.keys() else None,
			self.__model__,
			self.__descriptor__,
		)

	def __setitem__(self, key, value):
		pv = deepcopy(self.__value__.__getitem__(key)) if key in self.__value__.keys() else None
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__setitem__(key, value)
			if self.__descriptor__.validator:
				self.__model__.__properties__.__setitem__(
					self.__descriptor__.name,
					self.__descriptor__.validator(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
				)
			if self.__descriptor__.callback:
				self.__descriptor__.callback(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			if self.__model__.__callback__:
				self.__model__.__callback__(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			return v
		except Exception as e:
			self.__value__.__setitem__(key, pv)
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def __delitem__(self, key):
		pv = deepcopy(self.__value__.__getitem__(key)) if key in self.__value__.keys() else None
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.__delitem__(key)
			if self.__descriptor__.validator:
				self.__model__.__properties__.__setitem__(
					self.__descriptor__.name,
					self.__descriptor__.validator(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
				)
			if self.__descriptor__.callback:
				self.__descriptor__.callback(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			if self.__model__.__callback__:
				self.__model__.__callback__(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			return v
		except Exception as e:
			self.__value__.__setitem__(key, pv)
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def __eq__(self, other: object) -> bool:
		return self.__value__.__eq__(other)
	
	def __ne__(self, other: object) -> bool:
		return self.__value__.__ne__(other)
	
	def keys(self):
		return self.__value__.keys()
	
	def items(self):
		return self.__value__.items()
	
	def values(self):
		return self.__value__.values()

	def clear(self) -> None:
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.clear()
			if self.__descriptor__.validator:
				self.__model__.__properties__.__setitem__(
					self.__descriptor__.name,
					self.__descriptor__.validator(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
				)
			if self.__descriptor__.callback:
				self.__descriptor__.callback(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			if self.__model__.__callback__:
				self.__model__.__callback__(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			return v
		except Exception as e:
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	
	def update(self, other):
		pv = deepcopy(self.__value__) 
		po = deepcopy(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
		try:
			v = self.__value__.update(other)
			if self.__descriptor__.validator:
				self.__model__.__properties__.__setitem__(
					self.__descriptor__.name,
					self.__descriptor__.validator(self.__model__.__properties__.__getitem__(self.__descriptor__.name))
				)
			if self.__descriptor__.callback:
				self.__descriptor__.callback(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			if self.__model__.__callback__:
				self.__model__.__callback__(
					self.__model__,
					self.__descriptor__,
					self.__model__.__properties__.__getitem__(self.__descriptor__.name),
					po
				)
			return v
		except Exception as e:
			self.__value__ = pv
			self.__model__.__properties__.__setitem__(
				self.__descriptor__.name,
				po,
			)
			raise e
	