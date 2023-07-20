# Liquirizia.EventScheduler
시간에 따른 이벤트 발생 및 처리를 위한 스케줄러

## 사용 방법

### 동작 정의
```python
from Liquirizia.EventRunner import EventRunner


class SampleEventRunner(EventRunner):
	def __init__(self, event: str, header: dict = None):
		self.event = event
		self.header = header
		return

	def run(self, body=None):
		# TODO : do something
		return
```

### 동작에 따른 스케줄 정의
```python
from Liquirizia.EventRunner import EventRunnerProperties
from Liquirizia.EventRunner.Types import EventTimer, EventInterval


properties_cron = EventRunnerProperties(
	SampleEventRunner,
	type=EventTimer(
		'${EVENT_STRING}',
		pattern='${PATTERN_STRING_WITH_CRON}'
	)
)

properties_interval = EventRunnerProperties(
	SampleEventRunner,
	type=EventInterval(
		'${EVENT_STRING}',
		interval=1000*60
	)
)
```

### 스케줄러 시작
```python
from Liquirizia.EventScheduler import EventScheduler


scheduler = EventScheduler('${TIMEZONE_STRING}')
scheduler.add(properties_cron)
scheduler.add(properties_interval) 
scheduler.load('${PATH_OF_PROPERTIES}')
scheduler.run(${MAX_CONCURRENCY_WORK})
```