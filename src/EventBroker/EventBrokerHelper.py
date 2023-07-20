# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .EventBrokerFactory import EventBrokerFactory
from .Configuration import Configuration
from .Connection import Connection

__all__ = (
	'EventBrokerHelper'
)


class EventBrokerHelper(Singleton):
	"""
	Event Broker Helper Class
	"""

	def onInit(self):
		self.brokers = {}
		return

	@classmethod
	def Set(cls, key, object: type(Connection),  conf: Configuration, persistent: bool = False):
		helper = cls()
		return helper.set(key, object, conf, persistent)

	def set(self, key, object: type(Connection), conf: Configuration, persistent: bool = False):
		self.brokers[key] = EventBrokerFactory(object, conf, persistent)
		return

	@classmethod
	def Get(cls, key):
		helper = cls()
		return helper.get(key)

	def get(self, key):
		if key not in self.brokers:
			return None
		broker = self.brokers[key]
		return broker.connect()

	@classmethod
	def CreateTopic(cls, key, topic, **kwargs):
		helper = cls()
		return helper.createTopic(key, topic, **kwargs)

	def createTopic(self, key, topic, **kwargs):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic()
		channel.declare(topic, **kwargs)
		return

	@classmethod
	def CreateQueue(cls, key, queue, **kwargs):
		helper = cls()
		return helper.createQueue(key, queue, **kwargs)

	def createQueue(self, key, queue, **kwargs):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue()
		channel.declare(queue, **kwargs)
		return

	@classmethod
	def DeleteTopic(cls, key, topic):
		helper = cls()
		return helper.deleteTopic(key, topic)

	def deleteTopic(self, key, topic):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic(topic)
		channel.remove()
		return

	@classmethod
	def DeleteQueue(cls, key, queue):
		helper = cls()
		return helper.deleteQueue(key, queue)

	def deleteQueue(self, key, queue):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue(queue)
		channel.remove()
		return

	@classmethod
	def Publish(cls, key, topic, event, body=None, format='application/json', charset='utf-8', headers=None, persistent=True, priority=None, expiration=None):
		helper = cls()
		return helper.publish(key, topic, event, body, format, charset, headers, persistent, priority, expiration)

	def publish(self, key, topic, event, body=None, format='application/json', charset='utf-8', headers=None, persistent=True, priority=None, expiration=None):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic(topic)
		return channel.publish(
			event=event,
			body=body,
			format=format,
			charset=charset,
			headers=headers,
			persistent=persistent,
			priority=priority,
			expiration=expiration,
		)

	@classmethod
	def Send(cls, key, queue, event, body=None, format='application/json', charset='utf-8', headers=None, persistent=True, priority=None, expiration=None):
		helper = cls()
		return helper.send(key, queue, event, body, format, charset, headers, persistent, priority, expiration)

	def send(self, key, queue, event, body=None, format='application/json', charset='utf-8', headers=None, persistent=True, priority=None, expiration=None):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue(queue)
		return channel.send(
			event=event,
			body=body,
			format=format,
			charset=charset,
			headers=headers,
			persistent=persistent,
			priority=priority,
			expiration=expiration,
		)

	@classmethod
	def Recv(cls, key, queue, timeout: int = None):
		helper = cls()
		return helper.recv(key, queue, timeout)

	def recv(self, key, queue, timeout: int = None):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue(queue)
		return channel.recv(timeout)
