# -*- coding: utf-8 -*-

from ..Expr import Expr

from ..Type import Type
from ..Function import Function

from typing import Union, Any

__all__ = (
	'IsEqualTo',
	'IsNotEqualTo',
	'IsGreaterThan',
	'IsGreaterEqualTo',
	'IsLessEqualTo',
	'IsLessThan',
)


class IsEqualTo(Expr):
	"""Is Equal Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} = {}'.format(str(self.col), self.other)


class IsNotEqualTo(Expr):
	"""Is Not Equal Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} != {}'.format(str(self.col), self.other)


class IsGreaterEqualTo(Expr):
	"""Is Greater Equal Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} >= {}'.format(str(self.col), self.other)


class IsGreaterThan(Expr):
	"""Is Greater Than Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} > {}'.format(str(self.col), self.other)


class IsLessEqualTo(Expr):
	"""Is Less Equal Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} > {}'.format(str(self.col), self.other)
	

class IsLessThan(Expr):
	"""Is Less Than Filter Class"""

	def __init__(
		self,
		col: Union[str, Type, Function],
		other: Union[Any, Type, Function],
	) -> None:
		self.col = col
		self.other = other
		if isinstance(self.other, Type):
			self.other = str(self.other)
		elif isinstance(self.other, Function):
			self.other = str(self.other)
		else:
			self.other = self.encode(self.other)
		return

	def __str__(self):
		return '{} < {}'.format(str(self.col), self.other)
