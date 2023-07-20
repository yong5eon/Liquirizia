# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from sys import stderr


class SampleObject(Singleton):

	def onInit(self, const=None):
		self.const = const if const else 0
		self.x = 0
		return

	def set(self, x):
		self.x = self.const + x

	def get(self):
		return self.x


if __name__ == '__main__':

	a = SampleObject(5)
	try:
		b = SampleObject(2)  # it is error
	except RuntimeError as e:
		print(str(e), file=stderr)

	x = SampleObject()
	x.set(2)
	print('{}.x is {}'.format('x', x.get()))

	y = SampleObject()
	y.set(3)
	print('{}.x is {}'.format('x', x.get()))
	print('{}.x is {}'.format('y', y.get()))
