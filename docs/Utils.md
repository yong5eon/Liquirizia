# 도구(Liquirizia.Utils)

- 데이터 타입 도구
  - 딕셔너리
  - 리스트
- 날자 및 시간 도구
- 동작 시간 도구

## 데이터 타입 도구

### 딕셔너리

#### 딕셔너리를 데이터 클래스로 변환하는 도구

```python
from Liquirizia.Utils.Dictionary import (
  CreateDataClass,
  ToDataClass,
)

_ = {
  'a': 1,
  'b': 2.0,
  'c': 'Hello',
  'd': [1,2,3],
  'e': (1,2),
  'f': {1,3,3},
  'g': {
    'a': 1,
    'b': 2.0,
    'c': 'World',
    'd': [1,2,3],
    'e': (1,2),
    'f': {1,3,3},
  }
}

obj = CreateDataClass('SampleObject', _)
inst = ToDataClass(_, obj)
print(inst) # expect, SampleObject(a=1, b=2.0, c='Hello', d=[1, 2, 3], e=(1, 2), f={1, 3}, g={'a': 1, 'b': 2.0, 'c': 'World', d=[1, 2, 3], e=(1, 2), f={1, 3}})
```
