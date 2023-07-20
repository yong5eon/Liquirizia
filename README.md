# Liquirizia
“약방엔 감초”라는 속담처럼 파이썬에서 어플리케이션을 개발하는데 “감초”의 역할을 하는 어플리케이션 프레임워크 라이브러리

## 목표

### 철할적 목표
* 사용하기 쉬워야 한다.
* 단순하고 명확해야 한다.
* 명확한 OOP(Object Oriented Programming)을 실현할 수 있어야 한다

### 기능적 목표
* 유연한 데이터 접근 및 모델링 지원
* 이벤트 주도 마이크로 서비스 아키텍처 지원
* 크로스 플랫폼 지원
  * 온프레미스(On-Premise) 구축 환경 지원
  * FaaS(Function as a Service) 구축 환경 지원
  
## 구성
* [OOP(Object Oriented Programming) 지원](docs/OOP.md)
* [템플릿 및 디자인 패턴](docs/DesignPatterns.md)
* 파일 시스템 접근 및 파일 접근
* 로거
* [값 검증기](docs/Validation.md)
* [데이터 접근 및 모델링](docs/DataAccessModel.md)
* 개발 지원 도구
  * 유닛 테스트
* [병렬 처리기](docs/Parallelizer.md)
* [웹 어플리케이션](docs/WebApplication.md)

## 확장 컴포넌트

### 이벤트 처리
* [이벤트 브로커](https://github.com/yong5eon/Liquirizia.EventBroker)
* [이벤트 처리 어플리케이션](https://github.com/yong5eon/Liquirizia.EventRunner)
* [이벤트 워커](https://github.com/yong5eon/Liquirizia.EventWorker)
* [이벤트 스케줄러](https://github.com/yong5eon/Liquirizia.EventScheduler)

### 네트워크 확장 도구
* [이메일 송신 어플리케이션](https://github.com/yong5eon/Liquirizia.Mailer)

### 클라우드 서비스 확장 도구
* [AWS 지원 확장 도구](https://github.com/yong5eon/Liquirizia.AWS)

## 할일
* [ ] EventBroker 분리
* [ ] EventRunner 분리
* [ ] EventScheduler 분리
* [ ] EventWorker 분리
* [ ] WebApplication 분리
* [ ] WebApplication 에서 Validator 제거 후 기본 Validator 를 사용하도록 변경
