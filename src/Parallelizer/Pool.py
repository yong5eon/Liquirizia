# -*- coding: utf-8 -*-

from .Handler import Handler
from .Runnable import Runnable

__all__ = (
	'PoolBase'
)


class Pool(object):
	"""
	Runnable Pool Abstract Class for Parallelize
	"""

	def __init__(self, handler: Handler = None, pool=None):
		if not pool:
			raise RuntimeError('Pool must be set which thread or process pool')
		self.pool = pool
		self.handler = handler
		self.runners = []
		return

	def __del__(self):
		if 'pool' in self.__dict__ and self.pool:
			self.stop()
		return

	def __len__(self):
		return len(self.runners)

	def __getstate__(self):
		refer = self.__dict__.copy()
		del refer['pool']
		return refer

	def __setstate__(self, state):
		self.__dict__.update(state)

	def add(self, runnable: type(Runnable), *args, **kwargs):
		# if Runnable not in runner.__bases__:
		#   raise RuntimeError('{} must be Runnable'.format(runner.__name__))
		self.runners.append(self.pool.apply_async(
			self.__run__,
			args=({'runner': runnable, 'args': args, 'kwargs': kwargs}, self.handler),
			error_callback=self.handler.onError if self.handler else None
		))
		return

	@staticmethod
	def __run__(args, handler: Handler):
		try:
			if handler:
				handler.onInitialize(*args['args'], **args['kwargs'])
			runner = args['runner'](*args['args'], **args['kwargs'])
			if handler:
				handler.onStart()
			runner.run()
			if handler:
				handler.onCompleted()
		# TODO : add more cases for SIGINT
		except KeyboardInterrupt as e:
			if handler:
				handler.onStopped()
			return None
		except Exception as e:
			if handler:
				handler.onError(e)
		return None

	def waits(self, timeout=None):
		try:
			for runner in self.runners:
				runner.wait(timeout)
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return

	def stop(self):
		try:
			self.pool.close()
			self.pool.join()
			self.pool = None
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return

	def shutdown(self):
		try:
			self.pool.terminate()
			self.pool.join()
			self.pool = None
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return
