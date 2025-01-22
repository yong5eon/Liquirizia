# -*- coding: utf-8 -*-

from .Configuration import Configuration
from .Connection import Connection
from .Cursor import Cursor
from .Session import Session
from .Context import Context

from .Table import Table
from .View import View

from .Constraint import Constraint
from .Index import Index
from .Expr import Expr
from .Function import Function

from sqlite3 import register_adapter
from datetime import datetime

__all__ = (
	'Configuration',
	'Connection',
	'Cursor',
	'Session',
	'Context',
	'Table',
	'View',
	'Constraint',
	'Index',
	'Expr',
	'Function',
)


class DateTimeAdator(object):
	def __call__(self, o: datetime):
		return o.isoformat()

register_adapter(datetime, DateTimeAdator())
