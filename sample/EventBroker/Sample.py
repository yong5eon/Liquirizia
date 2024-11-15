
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

	def consumer(self, queue: str, handler: EventHandler = None):
		return Consumer(self, queue, handler)

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
	def __init__(self, con: Connection, queue: str, handler: EventHandler = None):
		self.con = con
		self.queue = queue
		self.handler = handler
		self.alive = True
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
				v = q.get(block=True, timeout=1)
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


class SampleEventHandler(EventHandler):
	def __call__(self, event):
		print(event)
		return



if __name__ == '__main__':

	Helper.Set(
		'Sample',
		Connection,
		Configuration()
	)

	con = Helper.Get('Sample')
	exchange = con.exchange('topic')
	queue = con.queue('queue')
	queue.bind('topic')

	queue.send(1)
	exchange.send(2)

	reader = con.consumer('queue')
	print(reader.read())
	print(reader.read())

	queue.send(1)
	exchange.send(2)

	consumer = con.consumer('queue', SampleEventHandler())

	def stop():
		consumer.stop()
		return
	
	SetTimer(1, stop)

	consumer.run()
