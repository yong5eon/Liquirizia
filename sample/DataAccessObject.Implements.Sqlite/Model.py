# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Properties.Database import *

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
from Liquirizia.Utils import *

from random import randrange
from datetime import datetime

from typing import Dict

# Tables
class StudentUpdated(Handler):
	def __call__(self, m, o, v, pv):
		print('{}({}) of {}({}) is changed {} to {}'.format(
			o.name, o.key,
			m.__class__.__name__, m.__model__,
			pv,
			v,
		))
		changed = m.__cursor__.run(Update(Student).set(
			**{o.name: v}
		).where(
			IsEqualTo(Student.id, m.id)
		))
		PrettyPrint(changed)
		return
class Student(
	Table,
	name='STUDENT',
	constraints=(
		PrimaryKey('ID', autoincrement=True),
		Unique('IDX_UNIQUE_STUDENT_CODE', colexprs='CODE'),
	),
	indexes=(
		Index(name='IDX_STUDENT_IS_DELETED', colexprs='IS_DELETED'),
		Index(name='IDX_STUDENT_AT_CREATED', colexprs='AT_CREATED DESC'),
		Index(name='IDX_STUDENT_AT_UPDATED', colexprs='AT_UPDATED DESC'),
	),
	fn=StudentUpdated(),
):
	id = Integer('ID')
	code = Text('CODE')
	name = Text(name='NAME')
	metadata = BLOB(name='METADATA')
	atCreated = DateTime(name='AT_CREATED', default='CURRENT_TIMESTAMP')
	atUpdated = Timestamp(name='AT_UPDATED', null=True)
	isDeleted = Text(name='IS_DELETED', default='N')

class ClassUpdated(Handler):
	def __call__(self, m, o, v, pv):
		print('{}({}) of {}({}) is changed {} to {}'.format(
			o.name, o.key,
			m.__class__.__name__, m.__model__,
			pv,
			v,
		))
		changed = m.__cursor__.run(Update(Class).set(
			**{o.name: v}
		).where(
			IsEqualTo(Class.id, m.id)
		))
		PrettyPrint(changed)
		return
class Class(
	Table,
	name='CLASS',
	constraints=(
		PrimaryKey('ID', autoincrement=True),
		Unique(name='IDX_CLASS_CODE', colexprs='CODE'),
	),
	indexes=(
		Index(name='IDX_CLASS_IS_DELETED', colexprs='IS_DELETED'),
		Index(name='IDX_CLASS_AT_CREATED', colexprs='AT_CREATED DESC'),
		Index(name='IDX_CLASS_AT_UPDATED', colexprs='AT_UPDATED DESC'),
	),
	fn=ClassUpdated(),
):
	id = Integer(name='ID')
	code = Text(name='CODE')
	name = Text(name='NAME')
	atCreated = DateTime(name='AT_CREATED', default='CURRENT_TIMESTAMP')
	atUpdated = Timestamp(name='AT_UPDATED', null=True)
	isDeleted = Text(name='IS_DELETED', default='N')

class StudentClassUpdated(Handler):
	def __call__(self, m, o, v, pv):
		print('{}({}) of {}({}) is changed {} to {}'.format(
			o.name, o.key,
			m.__class__.__name__, m.__model__,
			pv,
			v,
		))
		changed = m.__cursor__.run(Update(StudentOfClass).set(
			**{o.name: v}
		).where(
			IsEqualTo(StudentOfClass.studentId, m.studentId),
			IsEqualTo(StudentOfClass.classId, m.classId),
		))
		PrettyPrint(changed)
		return
class StudentOfClass(
	Table,
	name='STUDENT_CLASS',
	constraints=(
		PrimaryKey(('STUDENT', 'CLASS')),
		ForeignKey(cols='STUDENT', reference='STUDENT', referenceCols='ID'),
		ForeignKey(cols='CLASS', reference='CLASS', referenceCols='ID'),
	),
	indexes=(
		Index(name='IDX_STUDENT_CLASS_SCORE', colexprs='SCORE'),
		Index(name='IDX_STUDENT_CLASS_AT_CREATED', colexprs='AT_CREATED DESC'),
		Index(name='IDX_STUDENT_CLASS_AT_UPDATED', colexprs='AT_UPDATED DESC'),
	),
	fn=StudentClassUpdated(),
):
	studentId = Integer(name='STUDENT')
	studentName = Text(name='STUDENT_NAME')
	classId = Integer(name='CLASS')
	className = Text(name='CLASS_NAME')
	score = Float(name='SCORE', null=True)
	atCreated = DateTime(name='AT_CREATED', default='CURRENT_TIMESTAMP')
	atUpdated = Timestamp(name='AT_UPDATED', null=True)


# View 
class StatOfStudent(
	View,
	name='STAT_STUDENT',
	executor=Select(Student).join(
		LeftOuter(StudentOfClass, IsEqualTo(Student.id, StudentOfClass.studentId)),
		LeftOuter(Class, IsEqualTo(StudentOfClass.classId, Class.id)),
	).where(
		IsEqualTo(Student.isDeleted, 'N')
	).groupBy(
		Student.id
	).values(
		Student.id,
		Student.name,
		Alias(Count(Class.id), 'COUNT'),
		Alias(Sum(StudentOfClass.score), 'SUM'),
		Alias(Average(StudentOfClass.score), 'AVG'),
		Student.atCreated,
		Student.atUpdated,
	).orderBy(
		Ascend(Student.id)
	),
):
	id = Integer(name='ID')
	name = Text(name='NAME')
	count = Integer(name='COUNT')
	sum = Float(name='SUM', null=True)
	average = Float(name='AVG', null=True)
	atCreated = DateTime(name='AT_CREATED')
	atUpdated = Timestamp(name='AT_UPDATED', null=True)


class StatOfClass(
	View,
	name='STAT_CLASS',
	executor=Select(Class).join(
		LeftOuter(StudentOfClass, IsEqualTo(Class.id, StudentOfClass.classId)),
		LeftOuter(Student), IsEqualTo(StudentOfClass.studentId, Student.id)
	).where(
		IsEqualTo(Class.isDeleted, 'N')
	).groupBy(
		Class.id
	).values(
		Class.id,
		Class.name,
		Alias(Count(Student.id), 'COUNT'),
		Alias(Sum(StudentOfClass.score), 'SUM'),
		Alias(Average(StudentOfClass.score), 'AVG'),
		Class.atCreated,
		Class.atUpdated,
	).orderBy(
		Ascend(Class.id)
	),
):
	id = Integer(name='ID')
	name = Text(name='NAME')
	count = Integer(name='COUNT')
	sum = Float(name='SUM', null=True)
	average = Float(name='AVG', null=True)
	atCreated = DateTime(name='AT_CREATED')
	atUpdated = Timestamp(name='AT_UPDATED', null=True)


if __name__ == '__main__':

	# Set connection
	Helper.Set(
		'Sample',
		Connection,
		Configuration(
			path='Sample.DB',  # File Path for SQLite Database File
			autocommit=False
		)
	)

	# Get Connection
	con = Helper.Get('Sample')

	con.begin()
	
	con.run(Drop(StudentOfClass))
	con.run(Drop(Class))
	con.run(Drop(Student))
	con.run(Drop(StatOfStudent))
	con.run(Drop(StatOfClass))
	con.run(Create(Student))
	con.run(Create(Class))
	con.run(Create(StudentOfClass))
	con.run(Create(StatOfStudent))
	con.run(Create(StatOfClass))

	STUDENT = [
		['SU970001', 'Koo Hayoon', 'README.md'],
		['SU970002', 'Ma Youngin', 'README.md'],
		['SU970003', 'Kang Miran', 'README.md'],
		['SU970004', 'Song Hahee', 'README.md'],
	]

	CLASS = [
		['CS000', 'What is Computer Science'],
		['CS100', 'Programming Language'],
		['CS101', 'C'],
		['CS102', 'C++'],
		['CS103', 'Java'],
		['CS104', 'JavaScript'],
		['CS105', 'Python'],
		['CS120', 'Operating System'],
		['CS130', 'Network'],
		['CS131', 'TCP/IP'],
		['CS132', 'HTTP'],
		['CS140', 'Database'],
		['CS141', 'Practice of RDBMS with MySQL'],
		['CS142', 'Practice of RDBMS with PostgreSQL'],
		['CS150', 'Distributed System'],
		['CS160', 'AI(Artificial Intelligence)'],
	]

	STUDENT_OF_CLASS = [
		['SU970001', 'CS000'],
		['SU970001', 'CS100'],
		['SU970001', 'CS120'],
		['SU970001', 'CS130'],
		['SU970002', 'CS000'],
		['SU970002', 'CS100'],
		['SU970002', 'CS101'],
		['SU970002', 'CS102'],
		['SU970003', 'CS000'],
		['SU970003', 'CS120'],
		['SU970003', 'CS130'],
		['SU970003', 'CS140'],
		['SU970003', 'CS150'],
		['SU970004', 'CS000'],
		['SU970004', 'CS130'],
		['SU970004', 'CS132'],
		['SU970004', 'CS140'],
		['SU970004', 'CS142'],
		['SU970004', 'CS150'],
	]

	students = []
	for _ in STUDENT:
		students.append(con.run(
			Insert(Student).values(
				code=_[0],
				name=_[1],
				metadata=open(_[2], mode='rb').read(),
			),
			fetch=Student,
		))
	
	for _ in students:
		PrettyPrint(_)
		_.atUpdated = datetime.now().timestamp()
		PrettyPrint(_)
	
	students = con.run(Select(Student), fetch=Student)
	PrettyPrint(students)

	classes = []
	for _ in CLASS:
		classes.append(con.run(
			Insert(Class).values(
				code=_[0],
				name=_[1],
			),
			fetch=Class,
		))
	
	for _ in classes:
		PrettyPrint(_)
		_.atUpdated = datetime.now().timestamp()
		PrettyPrint(_)
	
	classes = con.run(Select(Class), fetch=Class)
	PrettyPrint(classes)
	
	for scode, ccode in STUDENT_OF_CLASS:
		s = con.run(Get(Student).where(IsEqualTo(Student.code, scode)), fetch=Student)
		c = con.run(Get(Class).where(IsEqualTo(Class.code, ccode)), fetch=Class)
		con.run(Insert(StudentOfClass).values(
			studentId=s.id,
			studentName=s.name,
			classId=c.id,
			className=c.name,
		), fetch=StudentOfClass)
	
	studentsOfClasses = con.run(Select(StudentOfClass), fetch=StudentOfClass)
	PrettyPrint(studentsOfClasses)
	
	for _ in studentsOfClasses:
		o = con.run(
			Update(StudentOfClass).set(
				score=randrange(10, 45)/10,
				atUpdated=datetime.now().timestamp(),
			).where(
				IsEqualTo(StudentOfClass.studentId, _.studentId),
				IsEqualTo(StudentOfClass.classId, _.classId),
			),
			fetch=StudentOfClass,
		)
		PrettyPrint(o)
	
	studentsOfClasses = con.run(Select(StudentOfClass), fetch=StudentOfClass)
	PrettyPrint(studentsOfClasses)
	
	for _ in studentsOfClasses:
		PrettyPrint(_)
		_.score = randrange(10, 45)/10
		_.atUpdated = datetime.now().timestamp()
		PrettyPrint(_)
	
	studentsOfClasses = con.run(Select(StudentOfClass), fetch=StudentOfClass)
	PrettyPrint(studentsOfClasses)
	
	exec = Select(Student).join(
			LeftOuter(StudentOfClass, IsEqualTo(Student.id, StudentOfClass.studentId)),
			LeftOuter(Class, IsEqualTo(StudentOfClass.classId, Class.id)),
		).values(
			Alias(Student.id, 'STUDENT_ID'),
			Alias(Student.name, 'STUDENT_NAME'),
			Alias(Class.id, 'CLASS_ID'),
			Alias(Class.name, 'CLASS_NAME'),
			Alias(Count(StudentOfClass.score), 'COUNT'),
			Alias(Sum(StudentOfClass.score), 'SUM'),
			Alias(Average(StudentOfClass.score), 'AVG'),
			Alias(Student.atCreated, 'STUDENT_AT_CREATED'),
			Alias(StudentOfClass.atCreated, 'STUDENT_OF_CLASS_AT_CREATED'),
			Alias(StudentOfClass.atUpdated, 'STUDENT_OF_CLASS_AT_UPDATED'),
		).where(
			IsEqualTo(Student.isDeleted, 'N')
		).groupBy(
			Student.id,
		).having(
			IsGreaterEqualTo('AVG', 3)
		).orderBy(
			Ascend(Student.id),
			Descend('AVG'),
			Ascend('SUM'),
		).limit(0, 10)

	class RowFilter(Filter):
		def __call__(self, row: Dict) -> Dict:
			return {
				'id': row['STUDENT_ID'],
				'name': row['STUDENT_NAME'],
				'className': row['CLASS_NAME'],
				'count': row['COUNT'],
				'sum': row['SUM'],
				'avg': row['AVG'],
				'updated': max(row['STUDENT_AT_CREATED'], row['STUDENT_OF_CLASS_AT_CREATED']),
			}
	PrettyPrint(con.run(exec, filter=RowFilter()))

	con.run(Delete(StudentOfClass).where(
		IsEqualTo(StudentOfClass.studentName, 'Song Hahee')
	))

	PrettyPrint(con.run(exec))
	
	statOfStudent = con.run(Select(StatOfStudent))
	PrettyPrint(statOfStudent)
	
	statOfStudent = con.run(
		Select(StatOfStudent).where(
			IsGreaterThan(StatOfStudent.average, 3)
		)
	)
	PrettyPrint(statOfStudent)
	
	statOfClass = con.run(Select(StatOfClass))
	PrettyPrint(statOfClass)
	
	statOfClass = con.run(
		Select(StatOfClass).where(
			IsEqualTo(StatOfClass.count, 0)
		)
	)
	PrettyPrint(statOfClass)

	con.commit()

