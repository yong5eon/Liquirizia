# Liquirizia.EventRunner
이벤트 처리를 위한 어플리케이션 인터페이스 및 도구

## 이벤트 처리를 위한 어플리케이션 컴포넌트(Liquirizia.EventRunner)
* EventRunner : 이벤터 처리 어플리케이션 인터페이스

## 이벤트 유형 컴포넌트(Liquirizia.EventRunner.Types)
* EventWorker : 이벤트 워커를 위한 이벤트 유형
* EventInterval : 밀리초 간격의 이벤트 스케줄러를 위한 이벤트 유형
* EventTimer : 크론 패턴의 이벤트 스케줄러를 위한 이벤트 유형

## 이벤트 처리 어플리케이션 설정 컴포넌트
* EventRunnerProperties : 이벤트 처리 어플리케이션 속성
* EventRunnerPropertiesHelper : 이벤트 처리 어플리케이션 속성 도구

## 이벤트 처리를 위한 에러 유형
* NotSupportedTypeError : 지원되지 않는 이벤트 유형 오류
* NotSupportedEventError : 지원되지 않는 이벤트 오류
* InvalidHeaderError : 올바르지 않는 헤어 오류
* InvalidBodyError : 올바르지 않는 바디 오류

## 예제
### 이벤트 워커를 위한 예제
```python
from Liquirizia.EventRunner import EventRunner
from Liquirizia.EventRunner import	EventRunnerProperties
from Liquirizia.EventRunner.Types import EventWorker


class SampleEventRunner(EventRunner)
	def __init__(self, event: str, headers: dict = None):
		self.event = event
		self.headers = headers
		return

	def run(self, body=None):
		# TODO : do something
		return


properties = EventRunnerProperties(
	SampleEventRunner,
	type=EventWorker(
		event='${EVENT_STRING}',
		name='${BROKER_NAME}', 
		queue='${QUEUE_NAME}'	
	)
)
```

### 밀리초 간격의 이벤트 스케줄러를 위한 예제
```python
from Liquirizia.EventRunner import EventRunner
from Liquirizia.EventRunner import	EventRunnerProperties
from Liquirizia.EventRunner.Types import EventInterval


class SampleEventRunner(EventRunner)
	def __init__(self, event: str, headers: dict = None):
		self.event = event
		self.headers = headers
		return

	def run(self, body=None):
		# TODO : do something
		return


properties = EventRunnerProperties(
	SampleEventRunner,
	type=EventInterval(
		event='${EVENT_STRING}',
		interval=${INTERVAL_MILLESECONDS},
	)
)
```

### 크론 패턴의 이벤트 스케줄러를 위한 예체
```python
from Liquirizia.EventRunner import EventRunner
from Liquirizia.EventRunner import	EventRunnerProperties
from Liquirizia.EventRunner.Types import EventTimer


class SampleEventRunner(EventRunner)
	def __init__(self, event: str, headers: dict = None):
		self.event = event
		self.headers = headers
		return

	def run(self, body=None):
		# TODO : do something
		return


properties = EventRunnerProperties(
	SampleEventRunner,
	type=EventTimer(
		event='${EVENT_STRING}',
		pattern='${PATTERN_STRING_WITH_CRON}',
	)
)
```