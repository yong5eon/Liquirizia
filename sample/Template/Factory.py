# -*- coding: utf-8 -*-

from Liquirizia.Template import Factory

from sys import stderr


class SampleObject(Factory):

	def __init__(self, v=None):
		self.v = v
		return

	@classmethod
	def CreateInstance(Object, v=None):
		obj = Object(v)
		return obj

	def __str__(self):
		return str(self.v)


if __name__ == '__main__':

	try:
		a = SampleObject(5)  # raise RuntimeError
	except NotImplementedError as e:
		print('NOT IMPLEMENTED ERROR : {}'.format(str(e)), file=stderr)
	except RuntimeError as e:
		print('RUNTIME ERROR         : {}'.format(str(e)), file=stderr)

	try:
		a = SampleObject.CreateInstance(3)
		print(a)
	except NotImplementedError as e:
		print('NOT IMPLEMENTED ERROR : {}'.format(str(e)), file=stderr)
	except RuntimeError as e:
		print('RUNTIME ERROR         : {}'.format(str(e)), file=stderr)
