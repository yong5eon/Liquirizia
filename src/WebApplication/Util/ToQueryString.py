# -*- coding: utf-8 -*-

from urllib.parse import urlencode

__all__ = (
	'ToQueryString',
)


def ToQueryString(params):
	return urlencode(params)
