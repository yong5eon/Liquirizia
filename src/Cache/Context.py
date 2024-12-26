# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from typing import Any, Union

__all__ = (
	'Context',
)


class Context(metaclass=ABCMeta):
	"""Cache Context Interface"""
	@abstractmethod
	def set(self, key: Any, value: Any, expires: int = None) -> None: pass
	@abstractmethod
	def get(self, key: Any) -> Union[Any, None]: pass
