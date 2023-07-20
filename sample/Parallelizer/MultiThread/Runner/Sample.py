# -*- coding: utf-8 -*-

from Liquirizia.Parallelizer import Proxy
from Liquirizia.Parallelizer.MultiThread import Runner

from Liquirizia.System import Signal

from SampleHandler import SampleHandler
from SampleWork import SampleWork
from SampleRunner import SampleRunner


if __name__ == '__main__':

	# without handler
	worker = Runner()

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	signal = Signal(Signal.HUP, Signal.INT, Signal.QUIT, Signal.KILL, Signal.STOP, fn=stop)
	signal.attach(Signal.TERM, fn=shutdown)

	queue = Proxy.CreateQueue()
	lock = Proxy.CreateLock()

	for v in range(0, 100):
		queue.put(v)

	for i in range(0, 5):
		worker.add(SampleWork, lock, queue)

	worker.run()

	# with handler
	worker = Runner(SampleHandler())

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	signal = Signal(Signal.HUP, Signal.INT, Signal.QUIT, Signal.KILL, Signal.STOP, fn=stop)
	signal.attach(Signal.TERM, fn=shutdown)

	queue = Proxy.CreateQueue()
	lock = Proxy.CreateLock()

	for v in range(0, 100):
		queue.put(v)

	for i in range(0, 5):
		worker.add(SampleWork, lock, queue)

	worker.run()

	# with redefined runner and handler
	worker = SampleRunner()

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	signal = Signal(Signal.HUP, Signal.INT, Signal.QUIT, Signal.KILL, Signal.STOP, fn=stop)
	signal.attach(Signal.TERM, fn=shutdown)

	queue = Proxy.CreateQueue()
	lock = Proxy.CreateLock()

	for v in range(0, 100):
		queue.put(v)

	for i in range(0, 5):
		worker.add(SampleWork, lock, queue)

	worker.run()
