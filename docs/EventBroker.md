# Liquirizia.EventBroker
이벤트 브로커 헬퍼 및 인터페이스, 데이터 직렬화 도구

## 이벤트 브로커 인터페이스
* Configuration : 연결 설정 인터페이스
* Connection : 연결 인터페이스
* Topic : 토픽 인터페이스
* Queue : 큐 인터페이스
* Consumer : 컨슈머 인터페이스
* Event : 이벤트 인터페이스
* Response : 응답 인터페이스
* Callback : 이벤트 콜백 인터페이스

## 이벤트 브로커 오류
* Error : 공통 오류
* ConnectionError: 연결 오류
* ConnectionRefusedError : 연결 거부
* ConnectionTimeoutError : 연결 타임아웃
* ConnectionClosedError : 연결 종료
* NotFoundError : 브로커 찾을수 없음
* NotPermittedError : 브로커에 권한이 없음
* NotSupportedTypeError : 지원하지 않는 컨텐츠 타입
* EncodeError : 인코딩 에러
* DecodeError : 디코딩 에러
* TimeoutError : 타임아웃 에러, RPC 또는 컨슈머에서 사용됨

## 데이터 직렬화 도구
* SerializerHelper : 데이터 직렬화 도구
* Serializer : 데이터 직렬화를 위한 인코더, 디코더 인터페이스

### 지원 포멧
* JavaScript Object Notation : applicaiton/json
* Text : text/plain

## 이벤트 브로커 헬퍼
* EventBrokerHelper 