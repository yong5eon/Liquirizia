# -*- coding: utf-8 -*-

from abc import (
	ABC,
	abstractmethod,
)

__all__ = (
	'Pattern'
)


class Pattern(ABC):
	"""
	Pattern Interface Class for Validator

	Sample:
	from operator import eq

	class SamplePattern(Pattern):
		def __init__(self, compare):
			super(SamplePattern, self).__init__(error)
			self.compare = compare
			return

		def __call__(self, parameter):
			if not eq(parameter, self.compare):
				raise ValueError('{} is not equal to {}'.format(parameter, self.condition))
			return parameter  # if true, return parameter
	"""
	@abstractmethod
	def __call__(self, parameter):
		pass

	def __repr__(self):
		return '{}()'.format(self.__class__.__name__)
