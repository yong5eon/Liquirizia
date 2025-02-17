# 감초(Liquirizia)

“약방엔 감초”라는 속담처럼 파이썬에서 어플리케이션을 개발하는데 “감초”의 역할을 하는 어플리케이션 라이브러리

## 목표

### 철할적 목표

- 사용하기 쉬워야 한다.
- 단순하고 명확해야 한다.
- 명확한 OOP(Object Oriented Programming)을 실현할 수 있어야 한다

### 기능적 목표

- 유연한 데이터 접근 및 모델링 지원
- 이벤트 주도 마이크로 서비스 아키텍처 지원
- 크로스 플랫폼 지원
  - 온프레미스(On-Premise) 구축 환경 지원
  - FaaS(Function as a Service) 구축 환경 지원
  
## 구성

- [OOP(Object Oriented Programming) 지원](docs/OOP.md)
- [템플릿 및 디자인 패턴](docs/DesignPatterns.md)
- 파일 시스템 접근 및 파일 접근
- [데이터 접근 도구](docs/DataAccessObject.md)
- [데이터 모델링](docs/DataModel.md)
- [데이터 검증기](docs/Validation.md)
- 데이터 직렬화, 비직렬화 도구
- [병렬 처리기](docs/Parallelizer.md)
- [이벤트 브로커](docs/EventBroker.md)
- [로거](docs/Logger.md)
- 테스트
- 시스템
  - 파일락
  - 신호처리
  - 도구
    - [타이머](docs/System/Utils/Timer.md)
- [도구](docs/Utils.md)
  - 데이터 타입 도구
    - 딕셔너리
    - 리스트
  - 날자 및 시간 도구
  - 동작 시간 도구
- [설정 도구](sample/Configuration/Sample.py)

## 확장 컴포넌트

- [WSGI(WebServer Gateway Interface)](https://github.com/yong5eon/Liquirizia.WSGI)

## 구현체

### 데이터 접근

- [PostgreSQL 데이터 접근 도구](https://github.com/yong5eon/Liquirizia.DataAccessObject.Implements.PostgreSQL)
- [Redis 데이터 접근 도구](https://github.com/yong5eon/Liquirizia.DataAccessObject.Implements.Redis)

### 이벤트 브로커

- [RabbitMQ 이벤트 브로커](https://github.com/yong5eon/Liquirizia.EventBroker.Implements.RabbitMQ)
