# -*- coding: utf-8 -*-

from abc import (
	ABC,
	abstractmethod,
)

__all__ = (
	'Error'
)


class Error(ABC):
	"""Error Interface Class for Validator"""
	"""
	Sample:
	class YourError(Error):
		def __call__(self, parameter):
			...
			return RuntimeError('{} is failure'.format(parameter))
	"""
	@abstractmethod
	def __call__(self, parameter, *args, **kwargs) -> BaseException:
		raise NotImplementedError('{} must be implemented __call__ and must return exception class based BaseException'.format(self.__class__.__name__))
