# -*- coding: utf-8 -*-

from Liquirizia.Test import *

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Implements.Sqlite import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Types import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Constraints import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Executors import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Functions import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Filters import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Orders import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Joins import *
from Liquirizia.DataAccessObject.Implements.Sqlite.Exprs import *

from Liquirizia.DataModel import Handler

from datetime import datetime
from time import mktime


class Updater(Handler):
	def __call__(self, m, o, v, pv):
		m.__cursor__.run(Update(TestModel).set(
			**{o.name: v}
		).where(
			IsEqualTo(TestModel.id, m.id)
		))
		return
class TestModel(
	Table,
	name='TEST',
	constraints=(
		PrimaryKey(cols='ID', autoincrement=True),
	),
	indexes=(
		Index(name='IDX_TEST_COL_INTEGER', colexprs='COL_INTEGER'),
	),
	fn=Updater(),
):
	id = INTEGER(name='ID')
	colInteger = INTEGER(name='COL_INTEGER', null=True)
	colFloat = FLOAT(name='COL_FLOAT', null=True)
	colText = TEXT(name='COL_TEXT', null=True)
	colByteArray = BLOB(name='COL_BLOB', null=True)
	colDateTime = DATETIME(name='COL_DATETIME', null=True)
	colTimestamp = TIMESTAMP(name='COL_TIMESTAMP', null=True)


class TestSqliteTable(Case):
	@classmethod
	def setUpClass(cls):
		Helper.Set(
			'Sample',
			Connection,
			Configuration(
				path=':memory:',  # File Path for SQLite Database File
				autocommit=False,
			)
		)
		return super().setUpClass()

	@Order(1)
	def testCreate(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		return

	@Order(2)
	def testDrop(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		con.run(Drop(TestModel))
		return

	@Order(3)
	def testInsert(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		row = con.run(Insert(TestModel).values(
			colInteger=1,
			colFloat=2.0,
			colText='Hello Liquirizia',
			colByteArray=open('README.md', mode='rb').read(),
			colDateTime=datetime.now(),
			colTimestamp=datetime.now().timestamp(),
		), fetch=TestModel)
		ASSERT_IS_NOT_NONE(row)
		ASSERT_IS_EQUAL(row.id, 1)
		ASSERT_IS_EQUAL(row.colInteger, 1)
		ASSERT_IS_EQUAL(row.colFloat, 2.0)
		ASSERT_IS_EQUAL(row.colText, 'Hello Liquirizia')
		ASSERT_IS_EQUAL(row.colByteArray, open('README.md', mode='rb').read())
		ASSERT_TRUE(isinstance(row.colDateTime, datetime))
		ASSERT_TRUE(isinstance(row.colTimestamp, datetime))
		return

	@Order(4)
	def testUpdate(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		inserted = con.run(Insert(TestModel).values(
			colInteger=1,
			colFloat=2.0,
			colText='Hello Liquirizia',
			colByteArray=open('README.md', mode='rb').read(),
			colDateTime=datetime.now(),
			colTimestamp=datetime.now().timestamp(),
		), fetch=TestModel)
		updated = con.run(Update(TestModel).where(IsEqualTo(TestModel.id, inserted.id)).set(
			colInteger=2,
			colFloat=2.8,
			colText='Hello World',
			colByteArray=open('README.md', mode='rb').read(),
			colDateTime=datetime.now(),
			colTimestamp=datetime.now().timestamp(),
		), fetch=TestModel)

		ASSERT_IS_NOT_NONE(updated)
		ASSERT_IS_EQUAL(updated.id, 1)
		ASSERT_IS_EQUAL(updated.colInteger, 2)
		ASSERT_IS_EQUAL(updated.colFloat, 2.8)
		ASSERT_IS_EQUAL(updated.colText, 'Hello World')
		ASSERT_TRUE(isinstance(updated.colDateTime, datetime))
		ASSERT_TRUE(isinstance(updated.colTimestamp, datetime))
		ASSERT_IS_NOT_EQUAL(inserted.colInteger, updated.colInteger)
		ASSERT_IS_NOT_EQUAL(inserted.colFloat, updated.colFloat)
		ASSERT_IS_NOT_EQUAL(inserted.colText, updated.colText)
		return

	@Order(5)
	def testUpdateWithHandler(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		inserted = con.run(Insert(TestModel).values(
			colInteger=1,
			colFloat=2.0,
			colText='Hello Liquirizia',
			colByteArray=open('README.md', mode='rb').read(),
			colDateTime=datetime.now(),
			colTimestamp=datetime.now().timestamp(),
		), fetch=TestModel)
		inserted.colInteger = 2
		inserted.colFloat = 2.8
		inserted.colText = 'Hello World'

		updated = con.run(Get(TestModel).where(IsEqualTo(TestModel.id, inserted.id)), fetch=TestModel)

		ASSERT_IS_NOT_NONE(updated)
		ASSERT_IS_EQUAL(updated.id, 1)
		ASSERT_IS_EQUAL(updated.colInteger, 2)
		ASSERT_IS_EQUAL(updated.colFloat, 2.8)
		ASSERT_IS_EQUAL(updated.colText, 'Hello World')
		ASSERT_TRUE(isinstance(updated.colDateTime, datetime))
		ASSERT_TRUE(isinstance(updated.colTimestamp, datetime))
		return

	@Order(6)
	def testDelete(self):
		con = Helper.Get('Sample')
		con.run(Create(TestModel))
		inserted = con.run(Insert(TestModel).values(
			colInteger=1,
			colFloat=2.0,
			colText='Hello Liquirizia',
			colByteArray=open('README.md', mode='rb').read(),
			colDateTime=datetime.now(),
			colTimestamp=datetime.now().timestamp(),
		), fetch=TestModel)
		con.run(Delete(TestModel).where(IsEqualTo(TestModel.id, inserted.id)))
		updated = con.run(Get(TestModel).where(IsEqualTo(TestModel.id, inserted.id)), fetch=TestModel)
		ASSERT_IS_NONE(updated)
		return

