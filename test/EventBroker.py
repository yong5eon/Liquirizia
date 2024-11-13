# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.EventBroker import Helper
from Liquirizia.EventBroker import (
	Configuration as BaseConfiguration,
	Connection as BaseConnection,
	Topic as BaseTopic,
	Queue as BaseQueue,
	Consumer as BaseConsumer,
	EventHandler,
)

from queue import SimpleQueue, Empty


class Configuration(BaseConfiguration):
	def __init__(self):
		pass

class Connection(BaseConnection):
	def __init__(self, conf: Configuration):
		self.con = conf
		self.t = {}
		self.q = {}
		return
	def connect(self):
		pass
	def topic(self, topic: str = None):
		return Topic(self, topic)

	def queue(self, queue: str = None):
		return Queue(self, queue)

	def consumer(self, queue: str, handler: EventHandler = None):
		return Consumer(self, queue, handler)

	def close(self):
		pass

class Topic(BaseTopic):
	def __init__(self, con: Connection, topic: str):
		self.con = con
		if topic:
			self.create(topic)
			self.topic = topic
		return

	def create(self, topic):
		if topic in self.con.t.keys():
			return
		self.con.t[topic] = set()
		return

	def bind(self, topic):
		pass

	def send(self, v: any):
		for queue in self.con.t[self.topic]:
			self.con.q[queue].put(v)
		return

	def unbind(self, topic, **kwargs):
		pass

	def remove(self):
		del self.con.t[self.topic]
		return


class Queue(BaseQueue): 
	def __init__(self, con: Connection, queue:str = None):
		self.con = con
		if queue:
			self.create(queue)
			self.queue = queue
		return

	def create(self, queue):
		self.con.q[queue] = SimpleQueue()
		return

	def bind(self, topic):
		self.con.t[topic].add(self.queue)
		return

	def send(self, v: any):
		o = SimpleQueue()
		self.con.q[self.queue].put(v)
		return

	def unbind(self, topic):
		self.con.t[topic].remove(self.queue)
		return

	def remove(self):
		del self.con.q[self.queue]
		return


class SampleEventHandler(EventHandler):
	def __call__(self, event):
		print(event)
		return

class Consumer(BaseConsumer):
	def __init__(self, con: Connection, queue: str, handler: EventHandler = None):
		self.con = con
		self.queue = queue
		self.eh = handler
		self.alive = True
		return

	def qos(self, **kwargs):
		pass

	def read(self, timeout: float = None):
		q: SimpleQueue = self.con.q[self.queue]
		return q.get(block=True, timeout=timeout)

	def run(self, timeout: float = None):
		q: SimpleQueue = self.con.q[self.queue]
		while self.alive:
			v = q.get(block=True, timeout=timeout)
			if v:
				self.h(v)
		return

	def stop(self):
		self.alive = False
		return



class TestFileSystemObject(Case):
	@classmethod
	def setUpClass(cls) -> None:
		Helper.Set(
			'Sample',
			Connection,
			Configuration()
		)
		con = Helper.Get('Sample')
		topic = con.topic('topic')
		queue = con.queue('queue')
		queue.bind('topic')
		return super().setUpClass()

	@Order(1)
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
	def testSendToQueueReceiveFromQueue(self, i):
		con = Helper.Get('Sample')
		topic = con.queue('queue')
		topic.send(i)
		consumer = con.consumer('queue')
		o = consumer.read()
		ASSERT_IS_EQUAL(i, o)
		return
	

	@Order(2)
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
	def testSendToTopicReceiveFromQueue(self, i):
		con = Helper.Get('Sample')
		topic = con.topic('topic')
		topic.send(i)
		consumer = con.consumer('queue')
		o = consumer.read()
		ASSERT_IS_EQUAL(i, o)
		return
	
