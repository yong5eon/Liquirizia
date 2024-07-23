# -*- coding: utf-8 -*-

from operator import *

__all__ = (
	'DataTypeObject'
)



class DataTypeObject(object):
	"""Data Type Object of Data Model Object"""
	def __new__(
		cls,
		v,
		o,
		m,
	):
		n = object.__new__(cls)
		n.__value__= v
		n.__object__ = o
		n.__model__ = m
		return n

	def __getitem__(self, key):
		return DataTypeObject(self.__value__.__getitem__(key), self.__object__, self.__model__)

	def __setitem__(self, key, value):
		try:
			self.__value__.__setitem__(key, value)
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				self.__object__.validator(self.__model__.__object__.__getitem__(self.__object__.name))
			)
			if self.__object__.callback:
				self.__object__.callback(self.__model__, self.__object__.name, self.__model__.__object__.__getitem__(self.__object__.name))
		except Exception as e:
			self.__model__.__object__.__setitem__(
				self.__object__.name,
				self.__object__.value
			)
			raise e
		return

	def __getattr__(self, key):
		def observe(o: DataTypeObject, f: callable):
			def wrapper(*args, **kwargs):
				try:
					res = f(*args, **kwargs)
					self.__model__.__object__.__setitem__(
						self.__object__.name,
						self.__object__.validator(self.__model__.__object__.__getitem__(self.__object__.name))
					)
					if self.__object__.callback:
						self.__object__.callback(self.__model__, self.__object__.name, self.__model__.__object__.__getitem__(self.__object__.name))
					return res
				except Exception as e:
					self.__model__.__object__.__setitem__(
						self.__object__.name,
						self.__object__.value
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
			return super(DataTypeObject, self).__setattr__(key, value)
		setattr(self.__value__, key, value)
		if self.__object__.callback:
			self.__object__.callback(self.__model__, self.__object__.name, self.__model__.__object__.__getitem__(self.__object__.name))
		return 

	def __repr__(self):
		return self.__value__.__repr()

	# type casting
	def __bool__(self):
		return bool(self.__value__)

	def __int__(self):
		return int(self.__value__)

	def __float__(self):
		return float(self.__value__)

	def __str__(self):
		return self.__value__.__str__()

	# calculate operand
	def __abs__(self):
		return abs(self.__value__)

	def __add__(self, other):
		return add(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __sub__(self, other):
		return sub(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mul__(self, other):
		return mul(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __matmul__(self, other):
		return matmul(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __truediv__(self, other):
		return truediv(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __floordiv__(self, other):
		return floordiv(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __mod__(self, other):
		return mod(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __pow__(self, power, modulo=None):
		return pow(self.__value__, power, modulo=modulo)

	# operator magic
	def __neg__(self):
		return neg(self.__value__)

	def __pos__(self):
		return pos(self.__value__)

	def __invert__(self):
		return invert(self.__value__)

	# bit operand
	def __rshift__(self, other):
		return rshift(self.__value__, other)

	def __lshift__(self, other):
		return lshift(self.__value__, other)

	def __and__(self, other):
		return and_(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __or__(self, other):
		return or_(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __xor__(self, other):
		return xor(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	# compares
	def __lt__(self, other):
		return lt(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __le__(self, other):
		return le(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __eq__(self, other):
		return eq(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __ne__(self, other):
		return ne(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __ge__(self, other):
		return ge(self.__value__, other.v if isinstance(other, DataTypeObject) else other)

	def __gt__(self, other):
		return gt(self.__value__, other.v if isinstance(other, DataTypeObject) else other)
