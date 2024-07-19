# -*- coding: utf-8 -*-

from Liquirizia.Util import Duration, DurationTimer

from time import sleep


@Duration
def fn(seconds):
	sleep(seconds)
	return


class Sample(object):
	@Duration
	def __init__(self, seconds) -> None:
		sleep(seconds)
		return
	@Duration
	def fn(self, seconds) -> None:
		sleep(seconds)
		return


if __name__ == '__main__':
	fn(1)
	_ = Sample(2)
	_.fn(3)

	timer = DurationTimer()
	print(timer.table)