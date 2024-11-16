# -*- coding: utf-8 -*-

from Liquirizia.System.Util import SetTimer, Timeout

from time import sleep


def timeout():
	print('timeout')

def run(ms: int = None):
	if ms:
		sleep(ms / 1000)
	print('run')
	return 

if __name__ == '__main__':

	timer = SetTimer(100, timeout)
	run()
	timer.stop()

	timer = SetTimer(100, timeout)
	run(1000)
	timer.stop()

	@Timeout(100, timeout)
	def do(ms: int = None):
		if ms:
			sleep(ms / 1000)
		print('do')
		return
	do()
	do(1000)

