# -*- coding: utf-8 -*-

from Liquirizia.DataModelObject import Model, Type
from Liquirizia.DataModelObject.Immutable import DataModelObject
from Liquirizia.DataModelObject.Immutable.Types import *

from Liquirizia.Validator.Patterns import *

from Liquirizia.Validator import Pattern

from random import randint

from sys import stderr


class IsStringFixedLength(Pattern):
	def __init__(self, length):
		self.length = length
		return

	def __call__(self, parameter):
		if len(parameter) != self.length:
			raise RuntimeError('{} is must be {} length'.format(parameter, self.length))
		return parameter


@Model(
	id=Type(Integer),
	type=Type(String, IsStringFixedLength(2)),
	typeName=Type(String),
	name=Type(String),
	size=Type(String, IsIn('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')),
	stock=Type(Integer, IsGreaterEqualTo(0)),
	price=Type(Integer, IsGreaterThan(0))
)
class ProductModel(DataModelObject):
	def __init__(self, id, type, typeName, name, size, stock, price):
		super(ProductModel, self).__init__(id, type, typeName, name, size, stock, price)
		return

	@classmethod
	def CreateShirt(cls, id, size, stock, price):
		return cls.CreateInstance(id, 'MU', '상의', '셔츠', size, stock, price)

	@classmethod
	def CreatePants(cls, id, size, stock, price):
		return cls.CreateInstance(id, 'MB', '하의', '청바지', size, stock, price)

	@classmethod
	def CreateJacket(cls, id, size, stock, price):
		return cls.CreateInstance(id, 'MO', '아우터', '가죽 재킷', size, stock, price)


@Model(
	id=Type(Integer),
	products=Type(List),
)
class StoreModel(DataModelObject):
	def __init__(self, id, products):
		super(StoreModel, self).__init__(id, products)
		return

	@classmethod
	def Open(cls, id):
		products = list()
		products.append(ProductModel.CreateShirt(1, 'M', 3, randint(10000, 100000)))
		products.append(ProductModel.CreateShirt(2, 'L', 3, randint(10000, 100000)))
		products.append(ProductModel.CreatePants(3, 'M', 2, randint(10000, 100000)))
		products.append(ProductModel.CreatePants(4, 'L', 1, randint(10000, 100000)))
		products.append(ProductModel.CreateJacket(5, 'S', 4, randint(10000, 100000)))
		products.append(ProductModel.CreateJacket(6, 'M', 3, randint(10000, 100000)))
		products.append(ProductModel.CreateJacket(7, 'XL', 2, randint(10000, 100000)))
		return cls.CreateInstance(id, products)


@Model(
	store=Type(Integer),
	product=Type(ProductModel)
)
class PackageModel(DataModelObject):
	def __init__(self, store, product):
		super(PackageModel, self).__init__(store, product)
		return

	@classmethod
	def Add(cls, store, product):
		return cls.CreateInstance(store, product)


@Model(
	id=Type(Integer),
	carts=Type(List),
)
class UserModel(DataModelObject):
	def __init__(self, id, carts=()):
		super(UserModel, self).__init__(id, carts=List(carts))
		return

	@classmethod
	def Create(cls, id, carts=()):
		return cls.CreateInstance(id, carts)

	def addToCart(self, store, product):
		package = PackageModel.Add(store, product)
		self['carts'].append(package)
		return

	def addToCart2(self, store, product):
		carts = list(self['carts'])
		carts.append(PackageModel.Add(store, product))
		return UserModel.Create(self['id'], carts)


if __name__ == '__main__':

	store = StoreModel.Open(1)

	print(store['products'])

	for product in store['products']:
		print(product)

	for i in range(0, len(store['products'])):
		print(store['products'][i])

	user = UserModel.Create(1)

	for product in store['products']:
		try:
			user.addToCart(store['id'], product)  # expected RuntimeError
		except Exception as e:
			print(str(e), file=stderr)
		user = user.addToCart2(store['id'], product)
		print(user)

	print(user)
