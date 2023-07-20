# -*- coding: utf-8 -*-

from .EventRunnerProperties import EventRunnerProperties

from Liquirizia.Template import Singleton

from importlib.machinery import SourceFileLoader

from os.path import split, splitext


__all__ = (
	'EventRunnerPropertiesHelper',
)


class EventRunnerPropertiesHelper(Singleton):
	"""
	Event Runner Properties Helper
	"""
	def onInit(self, *args, **kwargs):
		self.properties = []
		return

	@classmethod
	def Load(cls, path, name='properties'):
		helper = EventRunnerPropertiesHelper()
		return helper.load(path, name)

	def load(self, path, name='properties'):
		head, tail = split(path)
		file, ext = splitext(tail)
		head = head.replace('\\', '.').replace('/', '.')
		mod = '{}.{}'.format(head, file)
		loader = SourceFileLoader(mod, path)
		mo = loader.load_module()
		if not mo:
			return None
		if not mo.__getattribute__(name):
			return None
		return mo.__getattribute__(name)

	@classmethod
	def Add(cls, properties: EventRunnerProperties):
		helper = EventRunnerPropertiesHelper()
		return helper.add(properties)

	def add(self, properties: EventRunnerProperties):
		self.properties.append(properties)
		return properties

	def __getitem__(self, index):
		return self.properties.__getitem__(index)

	def __setitem__(self, index, value):
		if index not in [idx for idx, val in enumerate(self.properties)]:
			return self.insert(index, value)
		return self.properties.__setitem__(index, value)

	def __delitem__(self, index):
		return self.properties.__delitem__(index)

	def __len__(self):
		return self.properties.__len__()

	def insert(self, index, value):
		properties = self.properties[index:]
		self.properties[index] = value
		for i, p in enumerate(properties):
			self.properties[index + i] = p
		return

	def append(self, value):
		return self.properties.append(value)

	def extend(self, value):
		return self.properties.extend(value)
