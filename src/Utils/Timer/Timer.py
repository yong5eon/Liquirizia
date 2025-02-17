# -*- coding: utf-8 -*-

from time import time

__all__ = (
	'Timer',
)


class Timer(object):
	'''Timer Class'''
	def __init__(self) -> None:
		self.ts = None
		self.te = None
		self.duration = None
		return

	def __repr__(self):
		return str(self.duration)

	def __str__(self):
		return str(self.duration)
	
	def __add__(self, other):
		return self.duration + other.duration
	
	def __lt__(self, other):
		return self.duration < other.duration

	def __gt__(self, other):
		return self.duration > other.duration

	def start(self):
		self.ts = time()
		return self.ts
	def end(self):
		self.te = time()
		self.duration = self.te - self.ts
		return self.te
