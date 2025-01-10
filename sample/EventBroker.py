# Sample for EventBroker

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
	e = con.exchange('e')
	q1 = con.queue('q1')
	q2 = con.queue('q2')
	q3 = con.queue('q3')
	q1.bind('e')
	q2.bind('e')
	q3.bind('e')

	e.send(1) # expect q1, q2 have 1 
	q1.send(2) # expect q1 has 1, 2
	q3.send(2) # expect q3 has 1, 2
	q2.send(3) # expect q2 has 1, 3
	q3.send(3) # expect q3 has 1, 2, 3

	print(q1.get()) # expect print 1
	print(q1.get()) # expect print 2

	print(q2.get()) # expect print 1
	print(q2.get()) # expect print 3

	c = con.consumer(SampleEventHandler())
	c.subs('q3')

	def stop():
		c.stop()
		return
	
	SetTimer(10, stop)

	c.run()

