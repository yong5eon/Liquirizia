# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'If',
	'And',
	'Any',
)


class If(Pattern):
	def __init__(self, *args, error=None) -> None:
		self.patterns = args
		self.error = error
		return
	
	def __call__(self, parameter):
		try:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		except Exception:
			return parameter
		
	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[p.__repr__() for p in self.patterns]
			)
		)


class And(Pattern):
	def __init__(self, *args, error=None) -> None:
		self.patterns = args
		self.error = error
		return
	
	def __call__(self, parameter):
		try:
			for pattern in self.patterns:
				parameter = pattern(parameter)
			return parameter
		except Exception as e:
			if self.error:
				raise self.error
			raise e
		
	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join(
				[p.__repr__() for p in self.patterns]
			)
		)


class Any(Pattern):
	def __init__(self, *args, error=None) -> None:
		self.patterns = args
		self.error = error
		return
	
	def __call__(self, parameter):
		for pattern in self.patterns:
			try:
				parameter = pattern(parameter)
				return parameter
			except Exception:
				pass
		if self.error:
			raise self.error
		raise ValueError('{} must be validated in {}'.format(
			parameter,
			', '.join([p.__repr__() for p in self.patterns])
		))

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join([p.__repr__() for p in self.patterns])
		)
