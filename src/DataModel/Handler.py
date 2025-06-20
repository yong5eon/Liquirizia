# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from typing import Any

__all__ = (
	'Handler'
)


class Handler(metaclass=ABCMeta):
	"""Handler Interface for Data Model"""
	@abstractmethod
	def __call__(
		self,
		o, # model
		p, # value descriptor
		v: Any, # changed value
		pv: Any,  # previous value
	):
		pass
