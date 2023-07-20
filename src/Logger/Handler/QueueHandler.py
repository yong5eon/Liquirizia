# -*- coding: utf-8 -*-

from logging.handlers import QueueHandler as QueueHandlerBase

__all__ = (
	'QueueHandler',
)


class QueueHandler(QueueHandlerBase):
	def __init__(self, queue):
		super(QueueHandler, self).__init__(queue)
		return
