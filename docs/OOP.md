# OOP(Object Oriented Programming) 지원

데코레이터를 통해 클래스에 대해 OOP(Object Oriented Programming) 특징을 지원

## 지원 형태

- 캡슐화(Encapsulation)
- 다형성(Polymorphism)
- 가상화(Virtual)
- 인터페이스(Interface) 및 구현(Implements)

## 클래스의 캡슐화(Encapsulation)

```python
from Liquirizia import (
  Private,
  Protected,
)

from sys import stderr


class BaseClass(object):
  def __init__(self, v):
    self.v = v
    return

  def __repr__(self):
    return str(self.v)

  @Private
  def a(self, v):
    self.v = v
    return

  @Protected
  def b(self, v):
    self.v = v
    return

  def c(self, v):
    self.v = v
    return

  def d(self, v):
    self.a(v)
    return


class DerivedClass(BaseClass):

  def aa(self, v):
    super(DerivedClass, self).a(v)
    return

  def bb(self, v):
    super(DerivedClass, self).b(v)
    return

  def cc(self, v):
    super(DerivedClass, self).c(v)
    return

  def dd(self, v):
    super(DerivedClass, self).a(v)
    return


if __name__ == '__main__':
  base = BaseClass(1)

  try:
    base.a(2)  # expected raise RuntimeError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  try:
    base.b(2)   # expected raise RuntimeError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  try:
    base.c(3)   # expected 3
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  try:
    base.d(4)  # expected 4
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  derived = DerivedClass(1)

  try:
    derived.aa(5)  # expected raise RuntimeError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)

  try:
    derived.bb(6)  # expected 6
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)

  try:
    derived.cc(7)  # expected 7
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)

  try:
    derived.dd(8)  # expected raise RuntimeError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)
```

## 다형성(Polymorphism)

```python
from Liquirizia import (
  Extends,
)

from sys import stderr


class CustomClass(object):

  @Extends
  def a(self, a):
    return a - a

  @Extends
  def a(self, a, b):
    return a - b


if __name__ == '__main__':

  obj = CustomClass()

  try:
    print(obj.a(2))  # expected 4
    print(obj.a(2, 3))  # expected 6
  except Exception as e:
    print(str(e), file=stderr)
```

## 가상화(Virtual)

```python
from Liquirizia import (
  Virtual,
)

from sys import stderr


class BaseClass(object):
  def __init__(self, v):
    self.v = v
    return

  def __repr__(self):
    return str(self.v)

  @Virtual
  def a(self, v):
    pass

  @Virtual
  def b(self, v):
    pass


class DerivedClass(BaseClass):

  def a(self, v):
    self.v = v
    return


if __name__ == '__main__':
  base = BaseClass(1)

  try:
    base.a(2)  # expected raise NotImplementedError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  try:
    base.b(2)   # expected raise NotImplementedError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(base)

  derived = DerivedClass(1)

  try:
    derived.a(3)
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)

  try:
    derived.b(5)  # expected raise NotImplementedError
  except Exception as e:
    print(str(e), file=stderr)
  else:
    print(derived)
```

## 인터페이스(Interface) 및 구현(Implements)

```python
from Liquirizia import (
  Interface,
  Implements,
)

from sys import stderr


@Interface
class Add(object):
  def add(self, other):
    pass


@Interface
class Minus(object):
  def sub(self, other):
    pass


@Interface
class Multiplication(object):
  def mul(self, other):
    pass


@Implements(Add, Minus, Multiplication)
class Calculator(object):
  def __init__(self, v):
    self.v = v
    return

  def add(self, other):
    return self.v + other

  def sub(self, other):
    return self.v - other


if __name__ == '__main__':

  cal = Calculator(10)

  try:
    print(cal.add(2))  # expected 12
    print(cal.sub(3))  # expected 7
    print(cal.mul(4))  # expected raise NotImplementedError
  except Exception as e:
    print(str(e), file=stderr)
```
