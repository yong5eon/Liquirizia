# -*- coding: utf-8 -*-

from pprint import PrettyPrinter

__all__ = (
	'PrettyPrint',
)


def PrettyPrint(obj, indent=2, width=80, depth=None, compact=False, sort=False):
	pp = PrettyPrinter(indent=indent, width=width, depth=depth, compact=compact, sort_dicts=sort)
	return pp.pprint(obj)
