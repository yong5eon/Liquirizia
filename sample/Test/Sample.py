# -*- coding: utf-8 -*-

from imp import ImportModule

ImportModule('Liquirizia', 'Liquirizia/src')

from Liquirizia.Test import (
	Runner,
	Case,
	Fixture,
	ASSERT,
)
from Liquirizia.Test.Patterns import *


class Sample(Case):
	def __init__(self, a, b):
		self.a = a
		self.b = b 
		return
	def __call__(self):
		return self.a / self.b
	def __str__(self):
		return '{} / {}'.format(self.a, self.b)


if __name__ == '__main__':

	test = Runner()

	ASSERT(Sample(2, 1), IsEqualTo(2))
	ASSERT(Sample(2, 1), IsAll(IsTypeOf(float), IsEqualTo(2.0)))
	ASSERT(Sample(2, 1), IsAll(IsTypeOf(float), IsEqualTo(3)))
	ASSERT(Sample(2, 1), IsAll(IsTypeOf(int), IsEqualTo(3)))
	ASSERT(Sample(6, 2), IsEqualTo(2))
	ASSERT(Sample(3, 0), IsEqualTo(3))

	test.add(Sample(3, 1), IsEqualTo(3))
	test.add(Sample(2, 2), IsEqualTo(2))
	test.add(Sample(4, 0), IsEqualTo(4))
	test.run()