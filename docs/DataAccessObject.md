# 데이터 접근 도구(Liquirizia.DataAccessObject)

데이터 접근을 위한 객체의 인터페이스 및 헬퍼

## 구성

- 데이터 접근 헬퍼
- 데이터 접근 설정 인터페이스
- 데이터 접근 인터페이스
- 데이터 접근 확장 인터페이스

### 데이터 접근 헬퍼

싱글턴 디자인 패턴으로 프로세스 내에서 유일하다. 헬퍼에 접근 설정 클래스와, 접근 클래스를 이름으로 등록하여 어느곳에서나 이름으로 가져와 사용 가능하다

### 데이터 접근 인터페이스

접근하고자 하는 데이터 공급자에 맞추어 인터페이스를 구현하여 사용하면 된다.

### 데이터 접근 확장 인터페이스

- 데이터베이스 - Liquirizia.DataAccessObject.Properties.Database
- 문서 - Liquirizia.DataAccessObject.Properties.Document
- 인덱스 - Liquirizia.DataAccessObject.Properties.Index
- 캐시 - Liquirizia.DataAccessObject.Properties.Cache

## 사용방법

```python
from Liquirizia.DataAccessObject import Helper  # 데이터 접근 헬퍼 임포트
from Liquirizia.DataAccessObject import (
  Configuration,  # 데이터 접근 설정 선언을 위한 추상 설정 클래스 임포트
  Connection,  # 데이터 접근 객체 선언을 위한 추상 클래스 임포트
)

import sys

# 데이터 접근 설정 객체 선언
class SampleConfiguration(Configuration):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    return

# 데이터 접근 객체 선언
class SampleConnection(Connection):

  def __init__(self, conf: SampleConfiguration):
    self.conf = conf
    self.data = None
    return

  def __del__(self):
    self.close()
    return

  def connect(self):
    self.data = self.conf.a + self.conf.b
    return

  def close(self):
    self.data = None
    return

  def get(self):
    if self.data is None:
      raise RuntimeError('{} is not connected and initialized'.format(self.__class__.__name__))
    return self.data

  def set(self, data):
    if not isinstance(data, int):
      raise DataAccessObjectError('{} must be int'.format(data))
    self.data = data
    return self.data


if __name__ == '__main__':

  con = None

  try:
    # Set connection
    Helper.Set(
      'Sample',
      SampleConnection,
      SampleConfiguration(1, 2)
    )

    # Get Connection
    con = Helper.Get('Sample')
    print(con.get())  # expected print 3
    print(con.set(5))  # expected print 5
    print(con.set('a'))  # expected DataAccessObjectError
  except RuntimeError as e:
    print(str(e), file=sys.stderr)
```

## 구현체

### Database

- Sqlite
- [PostgreSQL](https://github.com/yong5eon/Liquirizia.DataAccessObject.Implements.PostgreSQL)

### Cache

- [Redis](https://github.com/yong5eon/Liquirizia.DataAccessObject.Implements.Redis)
