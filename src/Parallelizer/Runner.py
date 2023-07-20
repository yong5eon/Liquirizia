# -*- coding: utf-8 -*-

from .Handler import Handler
from .Runnable import Runnable

__all__ = (
	'Runner'
)


class Runner(object):
	"""
	Runner of Runnable Abstract Class for Parallelize
	"""

	def __init__(self, handler: Handler = None):
		self.handler = handler
		self.pool = None
		self.runners = []
		return

	def __getstate__(self):
		self_dict = self.__dict__.copy()
		del self_dict['pool']
		return self_dict

	def __setstate__(self, state):
		self.__dict__.update(state)

	def add(self, runnable: type(Runnable), *args, **kwargs):
		# if Runnable not in runner.__bases__:
		#   raise RuntimeError('{} must be Runnable'.format(runner.__name__))
		self.runners.append({
			'runner': runnable,
			'args': args,
			'kwargs': kwargs
		})
		return

	def clear(self):
		self.runners.clear()
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

	def getPool(self, size):
		raise NotImplementedError('{} must be implemented getPool method'.format(self.__class__.__name__))

	def start(self):
		try:
			self.pool = self.getPool(len(self.runners))
			for run in self.runners:
				self.pool.apply_async(self.__run__, args=(run, self.handler), error_callback=self.handler.onError if self.handler else None)
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return

	def run(self):
		try:
			self.pool = self.getPool(len(self.runners))
			for run in self.runners:
				self.pool.apply_async(self.__run__, args=(run, self.handler), error_callback=self.handler.onError if self.handler else None)
			self.pool.close()
			self.pool.join()
		except (EOFError, KeyboardInterrupt, OSError, SystemError, SystemExit) as e:
			if self.handler:
				self.handler.onStopped()
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return

	def stop(self):
		if not self.pool:
			return
		try:
			self.pool.close()
			self.pool.join()
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return

	def shutdown(self):
		if not self.pool:
			return
		try:
			self.pool.terminate()
			self.pool.join()
		except Exception as e:
			if self.handler:
				self.handler.onError(e)
		return
