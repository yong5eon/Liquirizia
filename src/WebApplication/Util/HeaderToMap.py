# -*- coding: utf-8 -*-

__all__ = (
	'HeadersToMap',
)


def HeadersToMap(headers):
	o = {}
	for k, v in headers:
		o[k] = v
	return o
