# -*- coding: utf-8 -*-

from .EventRunner import EventRunner
from .EventRunnerComplete import EventRunnerComplete
from .EventRunnerError import EventRunnerError

from .EventType import EventType

from Liquirizia.Validator import Validator

__all__ = (
	'EventRunnerProperties',
)


class EventRunnerProperties(object):
	"""
	Event Runner Properties Class
	"""
	def __init__(
		self,
		object: type(EventRunner),
		type: EventType,
		header: Validator = None,
		body: Validator = None,
		completes: (list[EventRunnerComplete], tuple[EventRunnerComplete], EventRunnerComplete) = None,
		errors: (list[EventRunnerError], tuple[EventRunnerError], EventRunnerError) = None,
	):
		self.__properties__ = {
			'object': object,
			'type': type,
			'header': header,
			'body': body,
			'completes': completes if isinstance(completes, (list, tuple)) else (completes,) if isinstance(completes, EventRunnerComplete) else (),
			'errors': errors if isinstance(errors, (list, tuple)) else (errors,) if isinstance(errors, EventRunnerError) else (),
		}
		return

	@property
	def object(self):
		return self.__properties__['object']

	@property
	def type(self):
		return self.__properties__['type']

	@property
	def header(self):
		return self.__properties__['header']

	@property
	def body(self):
		return self.__properties__['body']

	@property
	def completes(self):
		return self.__properties__['completes']

	@property
	def errors(self):
		return self.__properties__['errors']
