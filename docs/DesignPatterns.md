# 디자인 패턴

- 싱글턴(Singleton)
- 팩토리(Factory)

## 싱글턴

프로세스 내에서 유일한 객체(Object, Instance) 만을 반환하며, 유지한다

```python
from Liquirizia.Template import Singleton
from sys import stderr


class SampleObject(Singleton):

  def onInit(self, const=None):
    self.const = const if const else 0
    self.x = 0
    return

  def set(self, x):
    self.x = self.const + x

  def get(self):
    return self.x


if __name__ == '__main__':

  a = SampleObject(5)
  try:
    b = SampleObject(2)  # it is error
  except RuntimeError as e:
    print(str(e), file=stderr)

  x = SampleObject()
  x.set(2)
  print('{}.x is {}'.format('x', x.get()))  # expected 2

  y = SampleObject()
  y.set(3)
  print('{}.x is {}'.format('x', x.get()))  # expected 3
  print('{}.x is {}'.format('y', y.get()))  # expected 3
```

## 팩토리

팩토리를 상속 받은 클래스는 생성자를 통해서 클래스를 생성할 수 없고 CreateInstance 를 통해서만 생성 가능해 진다

```python
from Liquirizia.Template import Factory

from sys import stderr


class SampleObject(Factory):

  def __init__(self, const=None):
    self.const = const
    return

  @classmethod
  def CreateInstance(Object, const=None):
    obj = Object(const)
    return obj

  def __str__(self):
    return str(self.const)


if __name__ == '__main__':

  try:
    # a = SampleObject(5)  # raise RuntimeError
    a = SampleObject.CreateInstance(3)
    print(a)
  except NotImplementedError as e:
    print('NOT IMPLEMENTED ERROR : {}'.format(str(e)), file=stderr)
  except RuntimeError as e:
    print('RUNTIME ERROR         : {}'.format(str(e)), file=stderr)
```
