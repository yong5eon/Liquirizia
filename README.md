# Liquirizia

“약방엔 감초”라는 속담처럼 파이썬에서 어플리케이션을 개발하는데 “감초”의 역할을 하는 어플리케이션 라이브러리

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
* 데이터 접근 및 모델링
  * [데이터 접근](docs/DataAccessObject.md)
  * [데이터 모델링](docs/DataModel.md)
* [값 검증기](docs/Validation.md)
* 직렬화, 비직렬화 도구
* 파일 시스템 접근 및 파일 접근
* 시스템 도구
  * 파일락
  * 신호처리
* 도구
  * 날자 및 시간 도구
  * 딕셔너리 도구
  * 리스트 도구
* 로거
* 유닛 테스트
* [병렬 처리기](docs/Parallelizer.md)

## 확장 컴포넌트

### 직렬화 및 비 직렬화

* [텍스트 형식 직렬화 및 비 직렬화](https://github.com/yong5eon/Liquirizia.Serializer.Implements.Text)
* [JSON 형식 직렬화 및 비 직렬화](https://github.com/yong5eon/Liquirizia.Serializer.Implements.JavaScriptObjectNotation)
* [Form 형식 직렬화 및 비 직렬화](https://github.com/yong5eon/Liquirizia.Serializer.Implements.FormUrlEncoded)

### 파일 시스템 접근 및 파일 접근

* [파일 시스템](https://github.com/yong5eon/Liquirizia.FileSystemObject.Implements.FileSystem)
* [AWS S3](https://github.com/yong5eon/Liquirizia.FileSystemObject.Implements.AWS.S3)

### 이벤트 처리

* [이벤트 브로커](https://github.com/yong5eon/Liquirizia.EventBroker)
* [이벤트 처리 어플리케이션](https://github.com/yong5eon/Liquirizia.EventRunner)
* [이벤트 워커](https://github.com/yong5eon/Liquirizia.EventWorker)
* [이벤트 스케줄러](https://github.com/yong5eon/Liquirizia.EventScheduler)

### 웹 서비스

* [WSGI(Web Server Gateway Interface)](https://github.com/yong5eon/Liquirizia.WSGI)

### 네트워크 확장 도구

* [이메일 송신 어플리케이션](https://github.com/yong5eon/Liquirizia.Mailer)

### 클라우드 서비스 확장 도구

* [AWS 지원 확장 도구](https://github.com/yong5eon/Liquirizia.AWS)

## 테스트

```python
python -m Liquirizia.Test test
```
