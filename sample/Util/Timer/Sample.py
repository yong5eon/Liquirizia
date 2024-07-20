# -*- coding: utf-8 -*-

from Liquirizia.Util.Timer import Duration, DurationTimer

from time import sleep
from random import randrange


def cb(name, seconds):
	print('duration of {} : {}'.format(name, seconds))
	return


@Duration(callback=cb)
def fn(seconds):
	sleep(seconds)
	return

class Sample(object):
	@Duration(callback=cb)
	def __init__(self, seconds):
		self.seconds = seconds
		sleep(seconds)
		return
	@Duration(callback=cb)
	def fnm(self, seconds):
		sleep(seconds)
		return
	@Duration(callback=cb)
	@classmethod
	def fnc(cls, seconds):
		sleep(seconds)
		return
	@Duration(callback=cb)
	@staticmethod
	def fns(seconds):
		sleep(seconds)
		return
	@Duration(callback=cb)
	@property
	def fnp(self):
		sleep(self.seconds)
		return self.seconds

if __name__ == '__main__':

	for __ in range(0, randrange(1, 5)):
		fn(randrange(1, 5))
		_ = Sample(randrange(1, 5))
		_.fnm(randrange(1, 5))
		_.fnc(randrange(1, 5))
		_.fns(randrange(1, 5))
		_.fnp

	timer = DurationTimer()
	for k in timer.keys():
		print('{} : count({}), min({}), max({}), sum({}), avg({})'.format(
			k,
			timer.count(k),
			timer.min(k),
			timer.max(k),
			timer.sum(k),
			timer.avg(k),
		))
	print('Total : count({}), min({}), max({}), sum({}), avg({})'.format(
		timer.count(),
		timer.min(),
		timer.max(),
		timer.sum(),
		timer.avg(),
	))