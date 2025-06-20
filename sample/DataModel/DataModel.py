# -*- coding: utf-8 -*-

from Liquirizia.DataModel import (
	Model,
	Value,
	Parameters,
	Handler,
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *
from Liquirizia.Validator.Patterns.Number import IsRange
from Liquirizia.Description import (
	ToSchema,
	DumpSchema,
)

from Liquirizia.Utils import PrettyPrint

from typing import Annotated, Optional, Union

from random import randint

class Changed(Handler):
	def __call__(self, m, o, v, pv):
		print('{} of {} is changed {} to {}'.format(o.name, m.__class__.__name__, pv, v))
		return
	

class SampleModel(
	Model,
	fn=Changed(),
	description='Sample Model',
):
	# value = Value(type=int)
	# value: int # Value(type=int)
	# value: int = 0
	# value: int = None
	# value: Optional[int]
	# value: Optional[int] = 0
	# value: Annotated[int, 'int']
	# value: Annotated[int, {
	# 	'va': Validator(
	# 		IsInteger(IsRange(0, 1000))
	# 	),
	# 	'fn': Changed(),
	# 	'min': 0,
	# 	'max': 1000,
	# 	'description': 'An integer value with a range from 0 to 1000',
	# }]
	# value: Annotated[int, 'int'] = 0
	# value: Annotated[Optional[int], 'int']
	# value: Annotated[Optional[int], 'int'] = 0
	# value: Annotated[Optional[int], {
	# 	'va': Validator(
	# 		IsInteger(IsRange(0, 1001))
	# 	),
	# 	'fn': Changed(),
	# 	'min': 0,
	# 	'max': 1000,
	# 	'description': 'An integer value with a range from 0 to 1000',
	# }]
	value: Annotated[Optional[int], {
		'va': Validator(
			IsInteger(IsRange(0, 1001))
		),
		'fn': Changed(),
		'min': 0,
		'max': 1000,
		'description': 'An integer value with a range from 0 to 1000',
	}] = 0

PrettyPrint(DumpSchema(ToSchema(SampleModel)), indent=2)

_ = SampleModel(
# value=randint(0, 1000)
)
PrettyPrint(_, indent=2)
_.value = randint(0, 1000)
PrettyPrint(_, indent=2)