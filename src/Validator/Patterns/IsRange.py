# -*- coding: utf-8 -*-

from ..Pattern import Pattern

__all__ = (
	'IsRange'
)


class IsRange(Pattern):
	def __init__(self, start, stop=None, step=None, error=None):
		self.range = [start]
		if stop:
			self.range.append(stop)
		if step:
			self.range.append(step)
		self.start = start
		self.stop = stop
		self.step = step
		self.error = error
		return

	def __call__(self, parameter):
		if parameter not in [v for v in range(*self.range)]:
			if self.error:
				raise self.error
			raise ValueError('{} must be in the range {}'.format(
				parameter,
				'between {} to {}{}'.format(
					self.start if self.stop else 0,
					self.stop if self.stop else self.start,
					', in increments of {}'.format(self.step) if self.step else ''
				),
			))
		return parameter

	def __repr__(self):
		return '{}(start={}, stop={}, step={})'.format(
			self.__class__.__name__,
			self.start,
			self.stop,
			self.step,
		)
