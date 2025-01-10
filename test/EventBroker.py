# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.EventBroker import Helper
from Liquirizia.EventBroker import (
	Configuration as BaseConfiguration,
	Connection as BaseConnection,
	GetExchange,
	GetQueue,
	GetConsumer,
	Exchange as BaseExchange,
	Queue as BaseQueue,
	Gettable,
	Consumer as BaseConsumer,
	EventHandler,
)

from Liquirizia.System.Util import SetTimer

from queue import SimpleQueue, Empty


class Configuration(BaseConfiguration):
	def __init__(self):
		pass

class Connection(BaseConnection, GetExchange, GetQueue, GetConsumer):
	def __init__(self, conf: Configuration):
		self.con = conf
		self.e = {}
		self.q = {}
		return

	def connect(self):
		pass

	def exchange(self, exchange: str):
		if exchange not in self.e.keys():
			self.e[exchange] = set()
		return Exchange(self, exchange)

	def queue(self, queue: str):
		if queue not in self.q.keys():
			self.q[queue] = SimpleQueue()
		return Queue(self, queue)

	def consumer(self, handler: EventHandler):
		return Consumer(self, handler) 

	def close(self):
		pass


class Exchange(BaseExchange):
	def __init__(self, con: Connection, exchange: str):
		self.con = con
		self.exchange = exchange
		return

	def send(self, v: any):
		for queue in self.con.e[self.exchange]:
			self.con.q[queue].put(v)
		return


class Queue(BaseQueue, Gettable): 
	def __init__(self, con: Connection, queue: str):
		self.con = con
		self.queue = queue
		return

	def bind(self, exchange: str):
		if exchange not in self.con.e.keys():
			raise RuntimeError('No Exchange')
		self.con.e[exchange].add(self.queue)

	def send(self, v: any):
		self.con.q[self.queue].put(v)
		return

	def get(self, timeout: int = None):
		try:
			return self.con.q[self.queue].get(
				block=True,
				timeout=timeout / 1000 if timeout else None,
			)
		except Empty:
			return None


class Consumer(BaseConsumer):
	def __init__(self, con: Connection, handler: EventHandler):
		self.con = con
		self.handler = handler
		self.alive = True
		self.queue = None
		return

	def subs(self, queue: str):
		self.queue = queue
		return

	def run(self):
		q: SimpleQueue = self.con.q[self.queue]
		while self.alive:
			try:
				v = q.get(block=True, timeout=0)
				if v:
					self.handler(v)
			except Empty:
				if self.alive:
					continue
				break
		return

	def stop(self):
		self.alive = False
		return


class TestEventHandler(EventHandler):
	def __init__(self, q: SimpleQueue):
		self.q = q
		return
	def __call__(self, v):
		self.q.put(v)
		return


class TestEventBroker(Case):
	@classmethod
	def setUpClass(cls) -> None:
		Helper.Set(
			'Sample',
			Connection,
			Configuration()
		)
		con = Helper.Get('Sample')
		exchange = con.exchange('topic')
		queue = con.queue('queue')
		queue.bind('topic')
		return super().setUpClass()

	@Parameterized(
		{'i': True},
		{'i': 1},
		{'i': 1.0},
		{'i': 'abc'},
		{'i': b'abc'},
		{'i': (1,2,3)},
		{'i': [1,2,3]},
		{'i': {1,2,2}},
		{'i': {'a': True, 'b':1, 'c': 1.0, 'd': 'abc'}},
	)
	@Order(1)
	def testSendToQueueReceiveFromQueue(self, i):
		con = Helper.Get('Sample')

		queue = con.queue('queue')
		queue.send(i)

		reader = con.queue('queue')
		_ = reader.get()
		ASSERT_IS_EQUAL(i, _)

		queue.send(i)

		_ = SimpleQueue()
		consumer = con.consumer(TestEventHandler(_))
		consumer.subs('queue')

		def stop():
			consumer.stop()

		SetTimer(0.1, stop)

		consumer.run()

		ASSERT_IS_EQUAL(i, _.get())
		return

	@Parameterized(
		{'i': True},
		{'i': 1},
		{'i': 1.0},
		{'i': 'abc'},
		{'i': b'abc'},
		{'i': (1,2,3)},
		{'i': [1,2,3]},
		{'i': {1,2,2}},
		{'i': {'a': True, 'b':1, 'c': 1.0, 'd': 'abc'}},
	)
	@Order(2)
	def testSendToTopicReceiveFromQueue(self, i):
		con = Helper.Get('Sample')

		topic = con.exchange('topic')
		topic.send(i)

		reader = con.queue('queue')
		_ = reader.get()
		ASSERT_IS_EQUAL(i, _)

		topic.send(i)

		_ = SimpleQueue()
		consumer = con.consumer(TestEventHandler(_))
		consumer.subs('queue')

		def stop():
			consumer.stop()
		SetTimer(0.1, stop)

		consumer.run()

		ASSERT_IS_EQUAL(i, _.get())
		return

