# Liquirizia.WebApplication
웹 어플리케이션을 개발하기 위한 패키지

## 기본 컴포넌트
* Request : 요청 클래스
* Response : 응답 클래스
* Serializer : 데이터 시리얼라이저
* Validator : 데이터 검증기

### 데이터 송수신
* RequestReader : 요청 리더
* ResponseWriter : 응답 라이터
* WebSocket : 웹 소켓 리더 및 라이터

### 서버 어플리케이션을 위한 컴포넌트
* RequestRunner : 서버 어플리케이션 인터페이스
* RequestStreamRunner : 스트림 처리를 위한 서버 어플리케이션 인터페이스
* RequestWebSocketRunner : 웹소켓 처리를 위한 서버 어플리케이션 인터페이스
* RequestFilter : 어플리케이션 요청 필터
* RequestFilters : 어프리케이션 요청 필터 어그리게이터
* ResponseFilter : 어플리케이션 응답 필터
* ResponseFilters : 어플리케이션 응답 필터 어그리게이터

### 클라이언트 어플리케이션을 위한 컴포넌트
* ResponseRunner : 클라이언트 어플리케이션 인터페이스

## 사용 예제
* [요청 예제](/sample/WebApplication/Request/Sample.py)
* [응답 예제](/sample/WebApplication/Response/Sample.py)
* [데이터 시리얼라이저 예제](/sample/WebApplication/Serializer/Sample.py)
* [데이터 검증기 예제](/sample/WebApplication/Validator/Sample.py)

## 클라이언트 웹 어플리케이션
* [클라이언트 샘플](/sample/WebApplication/Client/Sample.py)

## 서버 웹 어플리케이션
### 샘플
* [서버](/sample/WebApplication/Server/Sample.py)

#### 어플리케이션
* [GET](/sample/WebApplication/Server/runs/RunGet.py)
* [POST](/sample/WebApplication/Server/runs/RunPost.py)
* [PUT](/sample/WebApplication/Server/runs/RunPut.py)
* [DELETE](/sample/WebApplication/Server/runs/RunPut.py)
* [스트림 출력](/sample/WebApplication/Server/runs/RunStreamOut.py)
* [청크 스트림 출력](/sample/WebApplication/Server/runs/RunChunkedStreamOut.py)
* [웹 소켓](/sample/WebApplication/Server/runs/RunWebSocket.py)

### 서버 웹 어플리케이션 동작
```python
from Liquirizia.WebApplication.Server import Server

server = Server()
server.run()
```

### 정적 컨텐츠 서빙
#### 파일 서빙
```python
from Liquirizia.WebApplication.Server import Server

server = Server()
server.addFile('${PATH}', '${URI}')
server.run()
```

#### 파일 경로 서빙
```python
from Liquirizia.WebApplication.Server import Server

server = Server()
server.addFiles('${PATH}', '${PREFIX_URI}')
server.run()
```

#### 파일 시스템 오브젝트를 통한 서빙
```python
from Liquirizia.WebApplication.Server import Server

from Liquirizia.FileSystemObject import FileSystemObjectHelper
from Liquirizia.FileSystemObject.Implements.FileSystem import FileSystemObject, FileSystemObjectConfiguration

FileSystemObjectHelper.Set(
		'${FILE_SYSTEM_OBJECT_NAME}',
		FileSystemObject,
		FileSystemObjectConfiguration('${PATH}')
	)

server = Server()
server.addFileSystemObject(
	FileSystemObjectHelper.Get('${FILE_SYSTEM_OBJECT_NAME}'),
	'${PREFIX_URI}',
)
server.run()
```

#### 정적 컨텐츠 서빙 시 요청 응답 필터 추가
```python
from Liquirizia.WebApplication.Server import Server

from Liquirizia.FileSystemObject import FileSystemObjectHelper
from Liquirizia.FileSystemObject.Implements.FileSystem import FileSystemObject, FileSystemObjectConfiguration

from Liquirizia.WebApplication import (
	RequestFilters,
	RequestFilter,
	ResponseFilters,
	ResponseFilter,
	Response,
)


class ReqFilter(RequestFilter):
	def __init__(self, f):
		self.f = f
		return
	def run(self, request):
		if not self.f:
			return request, Response(200, 'OK', 'HTTP/1.1')
		request.header('X-Additional-Request-Filter', 'ReqFilter')
		return request, None
	
class ResFilter(ResponseFilter):
	def run(self, response):
		response.header('X-Additional-Response-Filter', 'ResFilter')
		return response

FileSystemObjectHelper.Set(
		'${FILE_SYSTEM_OBJECT_NAME}',
		FileSystemObject,
		FileSystemObjectConfiguration('${PATH}')
	)

server = Server()
server.addFileSystemObject(
	FileSystemObjectHelper.Get('${FILE_SYSTEM_OBJECT_NAME}'),
	'${PREFIX_URI}',
	onRequest=ReqFilter(True),
	onRequestOrigin=RequestFilters(ReqFilter(True), ReqFilter(False)),
	onResponseOrigin=ResponseFilter(),
	onResponse=ResFilter(),
)
server.run()
```

### 어플리케이션 서빙
```python
from Liquirizia.WebApplication import RequestRunner, Request
from Liquirizia.WebApplication.Responses import *
from Liquirizia.WebApplication.Validator import Validate
from Liquirizia.WebApplication.Validator.Patterns import *

from Liquirizia.WebApplication.Server import Server


class Run(RequestRunner):
	def __init__(self, request: Request):
		self.request = request
		return

	def run(self, body=None):
		return ResponseJSON({
			'a': self.request.qs['a'],
			'b': self.request.qs['b'],
			'c': self.request.qs['c']
		})


server = Server()
server.add(
	Run,
	method='GET',
	url='/run',
	qs=Validate(
		mappings={
			'a': (TypeEvaluate(), IsInteger(IsGreaterThan(5))),
			'b': (TypeEvaluate(), IsFloat(IsGreaterThan(9))),
			'c': (SetDefault(''), IsString()),
		},
		required=('a', 'b'),
	)
)
server.run()
```

### 설정 파일을 사용한 어플리케이션 서빙
#### 어플리케이션
```python
from Liquirizia.WebApplication import RequestRunner, Request
from Liquirizia.WebApplication.Responses import *

__all__ = (
	'Run'
)

class Run(RequestRunner):
	def __init__(self, request: Request):
		self.request = request
		return

	def run(self, body=None):
		return ResponseJSON({
			'a': self.request.qs['a'],
			'b': self.request.qs['b'],
			'c': self.request.qs['c']
		})
```
#### 설정
```python
from Liquirizia.WebApplication import RequestRunnerPropertiesHelper, RequestRunnerProperties
from Liquirizia.WebApplication.Validator.Patterns import *

from .Run import Run

RequestRunnerPropertiesHelper.Add(RequestRunnerProperties(
	Run,
	method='GET',
	url='/run',
	qs={
		'mappings': {
			'a': (TypeEvaluate(), IsInteger(IsGreaterThan(5))),
			'b': (TypeEvaluate(), IsFloat(IsGreaterThan(9))),
			'c': (SetDefault(''), IsString()),
		},
		'required': ('a', 'b'),
	}
))
```

#### 서빙
```python
from Liquirizia.WebApplication.Server import Server

server = Server()
server.load('${PATH_OR_PATTERN_WITH_PATH}')  # 단일 경로 및 패턴 지정 방식, *.conf, path/to/*.conf, ...
# server.load('${PATH}', pattern='*.conf')  # 하위 경로의 모튼 설정 파일을 포함
server.run()
```

### 개선 사항
* 캐시 컨트롤
* 기본 에러 페이지 컨트롤
* 검증기 제거 및 기본 검증기 사용

## TODO
* RequestWriter : 요청 라이터
* ResponseReader : 응답 리더
0