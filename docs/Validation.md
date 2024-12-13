# 값 검증기

## 사용 방법

```python
from Liquirizia.Validator import Validator, Pattern, Error  # 검증기 임포트


class YourPattern(Pattern):
  def __init__(self, *args, **kwargs):
    # 검증을 위한 인자값을 받아서 저장
    ...
    return
  def __call__(self, parameter):
    # TODO : 파라미터 검증 후 반환
    ...
    return  parameter
  
class YourError(Error):
  def __call__(self, *args, **kwargs) -> BaseException:
    # TODO : 파라미너 검증 실패 시 발생할 예외 클래스를 리턴
    ...
    return Exception(...)

validator = Validator(YourPattern(..., error=YourError()), YourPattern(..., error=YourError()))
try:
  value = validator(...)  # 검증
except ...:
  # TODO : 예외 처리
  ...
else:
  # TODO : 검증 성공
  ...
```

## 일반 변수

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(IsNotNull(), IsIn((1, 2, 3)))  # 검증기 선언

parameter = 1
try:
  parameter = validator(parameter)  # 성공
except RuntimeError as e:
  ...

parameter = 4
try:
  parameter = validator(parameter)  # 실패
except RuntimeError as e:
  ...
```

## 정수 변수

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(
  IsNotNull(), 
  IsIn((1, 2, 3))
)  # 검증기 선언

try:
  parameter = validator(1)  # 성공
  parameter = validator(4)  # 실패
  parameter = validator(1.0)  # 실패
except RuntimeError as e:
  ...
```

## 부동 소수점 변수

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(
  IsNotNull(), 
  IsIn((1.0, 2.0, 3.0))
)  # 검증기 선언

try:
  parameter = validator(1)  # 실패
  parameter = validator(4.0)  # 실패
  parameter = validator(1.0)  # 성공
except RuntimeError as e:
  ...
```

## 문자열 변수

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(
  IsNotNull(),
  IsNotEmptyString(),
  IsString(IsIn(('허용선', '김진영', '방태식', '최준호', '홍승걸')))
)  # 검증기 선언

try:
  parameter = validator('허용선')  # 성공
  parameter = validator('방태식')  # 성공
  parameter = validator('이기현')  # 실패
except RuntimeError as e:
  ...
```

## 리스트

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(IsNotEmptyListable(), IsListable(IsIn((1, 2, 3))))  # 검증기 선언

parameter = [1, 2, 3]
try:
  parameter = validator(parameter)  # 성공
except RuntimeError as e:
  ...

parameter = [1, 2, 3, 4]
try:
  parameter = validator(parameter)  # 실패
except RuntimeError as e:
  ...
```

## 딕셔너리

```python
from Liquirizia.Validator import Validator  # 검증기 임포트
from Liquirizia.Validator.Patterns import *  # 미리 정의된 검증 패턴 임포트

valiator = Validator(
  IsNotEmptyDictionary(), 
  IsRequiredInDictionary(('a', 'b', 'c')),
  IsDictionary({
    'a': (IsNotNull(), InEqualTo(1)),
    'b': (IsNotNull(), InFewerThan(2)),
    'c': (IsNotNull(), InLessThan(4)),
  })
)  # 검증기 선언

parameter = {
  'a': 1,
  'b': 2,
  'c': 3
}
try:
  parameter = validator(parameter)  # 성공
except RuntimeError as e:
  ...

parameter = {
  'a': 1,
  'b': 2,
  'c': 4
}
try:
  parameter = validator(parameter)  # 실패
except RuntimeError as e:
  ...
```

## 함수에서 사용

```python
from Liquirizia.Validator import Validate
from Liquirizia.Validator.Patterns import *

@Validate({
  'a': (IsNotNull(), InEqualTo(1)),
  'b': (IsNotNull(), InFewerThan(2)),
  'c': (IsNotNull(), InLessThan(4)),
})
def func(a, b, c):
  # TODO : 함수 정의
  ...

try:
  func(1, 2, 1)  # 성공
  func(1, 2, 4)   # 실패
except RuntimeError as e:
  ...
```

## 클래스 메소드에서 사용

```python
from Liquirizia.Validator import Validate
from Liquirizia.Validator.Patterns import *

class A:
  @Validate({
    'a': (IsNotNull(), InEqualTo(1)),
    'b': (IsNotNull(), InFewerThan(2)),
    'c': (IsNotNull(), InLessThan(4)),
  })
  def func(self, a, b, c):
    # TODO : 함수 정의
    ...
  
try:
  a = A()
  a.func(1, 2, 1)  # 성공
  a.func(1, 2, 4)   # 실패
except RuntimeError as e:
  ...
```
