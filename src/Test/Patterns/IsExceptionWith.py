# -*- coding: utf-8 -*-

from ..Pattern import Pattern
from ..Case import Case

from operator import eq

__all__ = (
	'IsExceptionWith'
)


class IsExceptionWith(Pattern):
	def __init__(self, condition: type(BaseException)):
		self.condition = condition
		self.error = None
		return
	def __call__(self, case):
		try:
			case()
		except self.condition as e:
			self.error = e
			return True
		except Exception as e:
			print(e)
			return False
		else:
			return False	
	def __str__(self):
		return 'is exception with {}({})'.format(
			self.error.__class__.__name__, 
			str(self.error) if self.error else self.condition.__name__
		)
