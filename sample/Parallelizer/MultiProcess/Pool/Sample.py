# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer.MultiProcess import Pool

from SampleWork import SampleWork
from SampleHandler import SampleHandler
from SamplePool import SamplePool

from random import randint


if __name__ == '__main__':

	# without handler
	worker = Pool()

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	for i in range(0, 100):
		worker.add(SampleWork, randint(1, 100), randint(1, 100))

	worker.stop()

	# with handler
	worker = Pool(handler=SampleHandler())

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	for i in range(0, 100):
		worker.add(SampleWork, randint(1, 100), randint(1, 100))

	worker.stop()

	# with redefined pool and handler
	worker = SamplePool()

	def stop(sig):
		worker.stop()
		return


	def shutdown(sig):
		worker.stop()
		return


	for i in range(0, 100):
		worker.add(SampleWork, randint(1, 100), randint(1, 100))

	worker.stop()
