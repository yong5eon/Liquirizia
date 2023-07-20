# Liquirizia.Parallelizer
멀티 쓰레드 또는 프로세스를 활용한 병렬 처리기

## 지원 모델
* 워커 러너
* 워커 풀

## 지원 형식
* 멀티 쓰레딩
* 멀티 프로세싱

### 멀티 쓰레딩
개별 작업이 작업자 프로세스 내에서 다른 쓰레드로 동작 하는 방식
```python
from Liquirizia.Parallelizer.MultiThread import Pool  # import Multi Threading Pool
from Liquirizia.Parallelizer.MultiThread import Runner  # import Multi Threading Runner
```

### 멀티 프로세싱
개별 작업이 작업자 프로세스와 다른 개별 프로세스로 동작하는 방식
```python
from Liquirizia.Parallelizer.MultiProcess import Pool  # import Multi Threading Pool
from Liquirizia.Parallelizer.MultiProcess import Runner  # import Multi Threading Runner
```

## 워커 러너
작업을 사전에 정의하여 작업자 등록을 하여 작업자가 일괄 동작 시키는 방식

### 샘플
* [작업 정의](sample/MultiThread/Runner/SampleWork.py)
* [작업자 정의](sample/MultiThread/Runner/SampleRunner.py)
* [사용 방법](sample/MultiThread/Runner/Sample.py)

### 작업 정의
```python
from Liquirizia.Parallelizer import Runnable

from Liquirizia.System.Util import GetProcessId

__all__ = (
	'SampleWork'
)


class SampleWork(Runnable):
	def __init__(self, a, b):
		super(Runnable, self).__init__()
		self.a = a
		self.b = b
		return

	def run(self):
		print('{} - {} + {} = {}'.format(GetProcessId(), self.a, self.b, self.a + self.b))
		return
```

### 작업자 정의
```python
from Liquirizia.Parallelizer import Handler
from Liquirizia.Parallelizer.MultiThread import Runner

import sys

__all__ = (
	'SampleRunner'
)


class SampleRunner(Runner, Handler):
	def __init__(self):
		super(SampleRunner, self).__init__(self)
		return

	def onInitialize(self, *args, **kwargs):
		print('initialize')
		print(args)
		print(kwargs)
		return

	def onStart(self):
		print('started')
		return

	def onCompleted(self):
		print('completed')
		return

	def onStopped(self):
		print('stopped')
		return

	def onError(self, error=None):
		print('error', file=sys.stderr)
		print(str(error), file=sys.stderr)
		return
```

### 사용 방법
```python
# -*- coding: utf-8 -*-
from Liquirizia.Parallelizer import Proxy

from Liquirizia.System import Signal

from SampleWork import SampleWork
from SampleRunner import SampleRunner


if __name__ == '__main__':
	worker = SampleRunner()

	def stop(sig):
		worker.stop()
		return

	def shutdown(sig):
		worker.stop()
		return

	signal = Signal(Signal.HUP, Signal.INT, Signal.QUIT, Signal.KILL, Signal.STOP, fn=stop)
	signal.attach(Signal.TERM, fn=shutdown)

	queue = Proxy.CreateQueue()
	lock = Proxy.CreateLock()

	for v in range(0, 100):
		queue.put(v)

	for i in range(0, 5):
		worker.add(SampleWork, lock, queue)

	worker.run()
```

## 워커 풀
작업자가 작업 대기 상태로 동작하여 작업 요청이 발생 할 때 바로 동작 시키는 방식

### 샘플
* [작업 정의](sample/MultiThread/Pool/SampleWork.py)
* [작업자 정의](sample/MultiThread/Pool/SamplePool.py)
* [사용 방법](sample/MultiThread/Pool/Sample.py)

### 작업 정의
```python
from Liquirizia.Parallelizer import Runnable

from Liquirizia.System.Util import GetProcessId

__all__ = (
	'SampleWork'
)


class SampleWork(Runnable):
	def __init__(self, a, b):
		super(Runnable, self).__init__()
		self.a = a
		self.b = b
		return

	def run(self):
		print('{} - {} + {} = {}'.format(GetProcessId(), self.a, self.b, self.a + self.b))
		return
```

### 작업자 정의
```python
from Liquirizia.Parallelizer import Handler
from Liquirizia.Parallelizer.MultiThread import Pool

import sys

__all__ = (
	'SamplePool'
)


class SamplePool(Pool, Handler):
	def __init__(self, size=None):
		super(SamplePool, self).__init__(size, self)
		return

	def onInitialize(self, *args, **kwargs):
		print('initialize')
		print(args)
		print(kwargs)
		return

	def onStart(self):
		print('started')
		return

	def onCompleted(self):
		print('completed')
		return

	def onStopped(self):
		print('stopped')
		return

	def onError(self, error=None):
		print('error', file=sys.stderr)
		print(str(error), file=sys.stderr)
		return
```

### 사용 방법
```python
from SampleWork import SampleWork
from SamplePool import SamplePool

from random import randint


if __name__ == '__main__':
	# with redefined pool and handler
	worker = SamplePool()

	def stop(sig):
		worker.stop()
		return


	def shutdown(sig):
		worker.stop()
		return


	for i in range(0, 100):
		worker.add(SampleWork, randint(1, 100), randint(1, 100))

	worker.stop()
```