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
		self.t = {}
		self.q = {}
		return
	def connect(self):
		pass
	def exchange(self, exchange: str = None):
		return Exchange(self, exchange)

	def queue(self, queue: str = None):
		return Queue(self, queue)

	def consumer(self, queue: str, handler: EventHandler = None, timeout: float = None):
		return Consumer(self, queue, handler, timeout)

	def close(self):
		pass

class Exchange(BaseExchange):
	def __init__(self, con: Connection, exchange: str = None):
		self.con = con
		if exchange:
			self.create(exchange)
		self.exchange = exchange
		return
	
	def __str__(self): return self.exchange

	def create(self, exchange):
		if exchange in self.con.t.keys():
			return
		self.con.t[exchange] = set()
		return

	def bind(self, exchange):
		pass

	def send(self, v: any):
		for queue in self.con.t[self.exchange]:
			self.con.q[queue].put(v)
		return

	def unbind(self, exchange):
		pass

	def remove(self):
		del self.con.t[self.exchange]
		return


class Queue(BaseQueue): 
	def __init__(self, con: Connection, queue:str = None):
		self.con = con
		if queue:
			self.create(queue)
			self.queue = queue
		return

	def __str__(self): return self.queue

	def create(self, queue):
		self.con.q[queue] = SimpleQueue()
		return

	def bind(self, exchange):
		self.con.t[exchange].add(self.queue)
		return

	def send(self, v: any):
		o = SimpleQueue()
		self.con.q[self.queue].put(v)
		return

	def unbind(self, exchange):
		self.con.t[exchange].remove(self.queue)
		return

	def remove(self):
		del self.con.q[self.queue]
		return


class Consumer(BaseConsumer):
	def __init__(self, con: Connection, queue: str, handler: EventHandler, timeout: float = None):
		self.con = con
		self.queue = queue
		self.handler = handler
		self.alive = True
		self.timeout = timeout
		return
	
	def read(self, timeout: float = None):
		q: SimpleQueue = self.con.q[self.queue]
		try:
			return q.get(block=True, timeout=timeout)
		except Empty:
			return None

	def run(self):
		q: SimpleQueue = self.con.q[self.queue]
		while self.alive:
			try:
				v = q.get(block=True, timeout=self.timeout)
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
		queue.bind(str(exchange))
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
		reader = con.consumer('queue')
		_ = reader.read()
		ASSERT_IS_EQUAL(i, _)
		queue.send(i)
		_ = SimpleQueue()
		consumer = con.consumer('queue', TestEventHandler(_), timeout=0.1)
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
		reader = con.consumer('queue')
		_ = reader.read()
		ASSERT_IS_EQUAL(i, _)
		topic.send(i)
		_ = SimpleQueue()
		consumer = con.consumer('queue', TestEventHandler(_), timeout=0.1)
		def stop():
			consumer.stop()
		SetTimer(0.1, stop)
		consumer.run()
		ASSERT_IS_EQUAL(i, _.get())
		return
