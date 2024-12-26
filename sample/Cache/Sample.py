from Liquirizia.Cache import *

from hashlib import sha256
from datetime import datetime, timedelta

from time import sleep
from typing import Optional, Any


class MemoryContext(Context):
	def __init__(self):
		self.context = {}
		return

	def set(self, key: Any, value: Any, expires: int = 0):
		key = sha256(str(key).encode()).hexdigest()
		exp = datetime.now() + timedelta(seconds=expires) if expires else None
		self.context[key] = (
			exp.timestamp() if expires else 0,
			value,
		)
		return
	
	def get(self, key: Any) -> Optional[Any]:
		key = sha256(str(key).encode()).hexdigest()
		if key not in self.context.keys(): return None
		now = datetime.now().timestamp()
		exp, v = self.context[key]
		if not exp:
			return v
		if now < exp:
			return v
		del self.context[key]
		return None


if __name__ == '__main__':
	
	Helper.Set(
		'Memory',
		MemoryContext,
	)
	
	@Cached('Memory', expires=3)
	def foo(a, b):
		return a * b
	
	
	class Sample(object):
		@Cached('Memory', expires=3)
		def foo(self, a, b):
			return a + b
	
	context = Helper.Get('Memory')
	
	context.set(1, 0)
	context.set(2, 1, expires=5)

	print(foo(1,2))
	
	_ = Sample()
	print(_.foo(2, 3))
	
	sleep(1)
	print(context.get(1))
	print(context.get(2))
	print(foo(1,2))
	print(_.foo(2, 3))
	
	sleep(5)
	print(context.get(1))
	print(context.get(2))
	print(foo(1,2))
	print(_.foo(2, 3))
