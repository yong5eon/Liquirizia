# -*- coding: utf-8 -*-

from pprint import PrettyPrinter
from sys import stdout
from re import search, IGNORECASE

__all__ = (
	'PrettyPrint',
	'PrettyDump',
	'PrettyPrintSQL',
)


def PrettyPrint(obj, indent=2, file=stdout):
	AFTER_LF_PATTERNS	  = ['[', '{', '(', ',']
	BEBFORE_LF_PATTERNS = [']', '}', ')']
	EXCEPTIONAL_AFTER_LF_PATTERNNS = [',']
	CR = '\r'
	LF = '\n'
	BLANK = ' '
	step = 0
	blank = False
	lf = False
	for _ in obj if isinstance(obj, str) else repr(obj):
		if _ in BEBFORE_LF_PATTERNS:
			step -= 1
			if not lf:
				file.write(LF)
				lf = True
		if blank and _ == BLANK:
			blank = False
			continue	
		if lf:
			file.write(BLANK * (step * indent))
		file.write(_)
		lf = False
		if _ in AFTER_LF_PATTERNS:
			if _ not in EXCEPTIONAL_AFTER_LF_PATTERNNS:
				step += 1
			else:
				blank = True
			if not lf:
				file.write(LF)
				lf = True
	file.write(LF)
	return


def PrettyDump(obj, indent=2):
	AFTER_LF_PATTERNS	  = ['[', '{', '(', ',']
	BEBFORE_LF_PATTERNS = [']', '}', ')']
	EXCEPTIONAL_AFTER_LF_PATTERNNS = [',']
	CR = '\r'
	LF = '\n'
	BLANK = ' '
	step = 0
	blank = False
	lf = False
	__ = ''
	for _ in obj if isinstance(obj, str) else repr(obj):
		if _ in BEBFORE_LF_PATTERNS:
			step -= 1
			if not lf:
				__ += LF
				lf = True
		if blank and _ == BLANK:
			blank = False
			continue	
		if lf:
			__ += BLANK * (step * indent)
		__ += _
		lf = False
		if _ in AFTER_LF_PATTERNS:
			if _ not in EXCEPTIONAL_AFTER_LF_PATTERNNS:
				step += 1
			else:
				blank = True
			if not lf:
				__ += LF
				lf = True
	__ += LF
	return __


def PrettyPrintSQL(sql, indent=2, file=stdout):
	step = 0
	offset = 0
	CR = '\r'
	LF = '\n'
	BLANK = ' '
	PATTERNS_PRE_LF = [
		'FROM',
		'INNER JOIN',
		'LEFT OUTER JOIN',
		'LEFT JOIN',
		'RIGHT OUTER JOIN ',
		'RIGHT JOIN ',
		'WHERE',
		'ORDER BY',
		'GROUP BY',
		'HAVING',
		'LIMIT',
	]
	PATTERNS_POST_LF = [
		'SELECT',
		'FROM',
		'INNER JOIN',
		'LEFT OUTER JOIN',
		'LEFT JOIN',
		'RIGHT OUTER JOIN ',
		'RIGHT JOIN ',
		'WHERE',
		'ORDER BY',
		'GROUP BY',
		'HAVING',
		'LIMIT',
		','
	]
	PATTERNS_PRE_LF_NONE_STEP = [
		'INNER JOIN',
		'LEFT OUTER JOIN',
		'LEFT JOIN',
		'RIGHT OUTER JOIN ',
		'RIGHT JOIN ',
	]
	PATTERNS_POST_LF_NONE_STEP = [',']
	PATTERNS = set(PATTERNS_PRE_LF + PATTERNS_POST_LF)
	PATTERNS_REGEX = '|'.join(PATTERNS)
	while offset < len(sql):
		m = search(PATTERNS_REGEX, sql[offset:])
		if not m:
			break
		file.write(BLANK * (step * indent))
		expr = sql[offset:offset+m.span()[0]].strip()
		if len(expr):
			file.write(expr)
		token = sql[offset+m.span()[0]:offset+m.span()[1]]
		if token.upper() in PATTERNS_PRE_LF:
			file.write(LF)
			step -= 1
			file.write(BLANK * (step * indent))
		file.write(token)
		if token.upper() in PATTERNS_POST_LF:
			file.write(LF)
			if token not in PATTERNS_POST_LF_NONE_STEP:
				step += 1
		offset += m.span()[1]
	file.write(BLANK * (step * indent))
	file.write(sql[offset:].strip())
	file.write(LF)
	return
