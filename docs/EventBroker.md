# 이벤트 브로커(Liquirizia.EventBroker)

![클래스 다이어그램](../res/EventBroker.svg)

- [샘플 코드](../sample/EventBroker.py)

## 구성

- Helper : 이벤트 브로커 헬퍼
- Configuration : 이벤트 브로커 설정 인터페이스
- Connection : 이벤트 브로커 연결자 인터페이스
- Exchange : 익스체인지 유형의 이벤트 브로커 인터페이스
- Queue : 큐 유형의 이벤트 브로커 인터페이스
- Consumer : 소비자 유형의 이벤트 브로커 인터페이스
- EventHandler : 소비자에서 이벤트 처리를 위한 핸들러 인터페이스

### Connection 속성 인터페이스

- GetExchange : 연결자에서 익스체이진 유형을 획득하기 위한 행동 속성  인터페이스
- GetQueue : 연결자에서 큐 유형을 획득하기 위한 행동 속성  인터페이스
- GetConsumer : 연결자에서 소바자를 획득하기 위한 행동 속성 인터페이스

### Queue 속성 인터페이스

- Gettable : 큐를 Gettable 하도록 만들기 위한 행동 속성 인터페이스
- Readable : 큐를 Readable 하도록 만들기 위한 행동 속성 인터페이스 

## 구현

- [RabbitMQ - Liquirizia.EventBroker.Implements.RabbitMQ](https://github.com/yong5eon/Liquirizia.EventBroker.Implements.RabbitMQ)

