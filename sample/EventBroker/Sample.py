from Liquirizia.EventBroker import Helper
from Liquirizia.EventBroker import (
	Configuration as BaseConfiguration,
	Connection as BaseConnection,
	GetTopic,
	GetQueue,
	GetConsumer,
	Topic as BaseTopic,
	Queue as BaseQueue,
	Consumer as BaseConsumer,
	EventHandler,
)

from queue import SimpleQueue, Empty


class Configuration(BaseConfiguration):
	def __init__(self):
		pass

class Connection(BaseConnection, GetTopic, GetQueue, GetConsumer):
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


if __name__ == '__main__':

	Helper.Set(
		'Sample',
		Connection,
		Configuration()
	)

	con = Helper.Get('Sample')
	topic = con.topic('topic')
	queue = con.queue('queue')
	queue.bind('topic')

	queue.send(1)
	topic.send(2)

	# consumer = con.consumer('queue', SampleEventHandler())
	# consumer.run()

	consumer = con.consumer('queue')
	while True:
		try:
			v = consumer.read(1)
			print(v)
		except Empty as e:
			break
