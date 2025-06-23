# -*- coding: utf-8 -*-

from .Numeric import (
	Integer,
	Float,
)
from .String import Text
from .Binary import Binary
from .DateTime import (
	DateTime,
	Timestamp,
)

__all__ = (
	'Integer', 'INTEGER',
	'Float', 'FLOAT', 'REAL',
	'Text', 'TEXT', 'STRING',
	'Binary', 'BLOB',
	'DateTime', 'DATETIME',
	'Timestamp', 'TIMESTAMP',
)

# NUMERIC
INTEGER = Integer
FLOAT = Float
REAL = Float
# TEXT
TEXT = Text
STRING = Text
# BINARY
BLOB = Binary
# DATETIME
DATETIME = DateTime
TIMESTAMP = Timestamp
