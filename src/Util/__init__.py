# -*- coding: utf-8 -*-

from pprint import PrettyPrinter
from sys import stdout

__all__ = (
	'PrettyPrint',
	'PrettyDump',
)


def PrettyPrint(obj, indent=2, fd=stdout):
	AFTER_LF_PATTERNS	  = ['[', '{', '(', ',']
	BEBFORE_LF_PATTERNS = [']', '}', ')']
	EXCEPTIONAL_AFTER_LF_PATTERNNS = [',']
	CR = '\r'
	LF = '\n'
	BLANK = ' '
	step = 0
	blank = False
	lf = False
	for _ in repr(obj):
		if _ in BEBFORE_LF_PATTERNS:
			step -= 1
			if not lf:
				fd.write(LF)
				lf = True
		if blank and _ == BLANK:
			blank = False
			continue	
		if lf:
			fd.write(BLANK * (step * indent))
		fd.write(_)
		lf = False
		if _ in AFTER_LF_PATTERNS:
			if _ not in EXCEPTIONAL_AFTER_LF_PATTERNNS:
				step += 1
			else:
				blank = True
			if not lf:
				fd.write(LF)
				lf = True
	fd.write(LF)
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
	for _ in repr(obj):
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
