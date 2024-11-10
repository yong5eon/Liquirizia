# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Factory import Factory
from .Configuration import Configuration
from .Connection import Connection

from .Topic import Topic
from .Queue import Queue

from typing import Type, Any, Dict

__all__ = (
	'Helper'
)


class Helper(Singleton):
	"""
	Event Broker Helper Class
	"""

	def __init__(self):
		self.brokers = {}
		return

	@classmethod
	def Set(cls, key: str, object: Type[Connection],  conf: Configuration):
		helper = cls()
		return helper.set(key, object, conf)

	def set(self, key: str, object: Type[Connection], conf: Configuration):
		self.brokers[key] = Factory(object, conf)
		return

	@classmethod
	def Get(cls, key: str) -> Connection:
		helper = cls()
		return helper.get(key)

	def get(self, key: str) -> Connection:
		if key not in self.brokers:
			return None
		broker = self.brokers[key]
		return broker.connect()

	@classmethod
	def CreateTopic(cls, key: str, topic: str, **kwargs) -> Topic:
		helper = cls()
		return helper.createTopic(key, topic, **kwargs)

	def createTopic(self, key: str, topic: str, **kwargs) -> Topic:
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic()
		channel.create(topic, **kwargs)
		return

	@classmethod
	def CreateQueue(cls, key: str, queue: str, **kwargs) -> Queue:
		helper = cls()
		return helper.createQueue(key, queue, **kwargs)

	def createQueue(self, key: str, queue: str, **kwargs) -> Queue:
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue()
		channel.create(queue, **kwargs)
		return

	@classmethod
	def DeleteTopic(cls, key: str, topic: str):
		helper = cls()
		return helper.deleteTopic(key, topic)

	def deleteTopic(self, key: str, topic: str):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic(topic)
		channel.remove()
		return

	@classmethod
	def DeleteQueue(cls, key: str, queue: str):
		helper = cls()
		return helper.deleteQueue(key, queue)

	def deleteQueue(self, key: str, queue: str):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue(queue)
		channel.remove()
		return

	@classmethod
	def Publish(
		cls,
		key: str,
		topic: str,
		**kwargs
	):
		helper = cls()
		return helper.publish(
			key, 
			topic, 
			**kwargs
		)

	def publish(
		self,
		key: str,
		topic: str,
		**kwargs
	):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.topic(topic)
		return channel.send(**kwargs)

	@classmethod
	def Send(
		cls,
		key: str,
		queue: str,
		**kwargs
	):
		helper = cls()
		return helper.send(key, queue, **kwargs)

	def send(
		self,
		key: str,
		queue: str,
		**kwargs
	):
		broker = self.get(key)
		if not broker:
			return
		channel = broker.queue(queue)
		return channel.send(*kwargs)
