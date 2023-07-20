# -*- coding: utf-8 -*-

__all__ = (
	'VersionToString',
)


def VersionToString(version):
	return {
		10: 'HTTP/1.0',
		11: 'HTTP/1.1',
		20: 'HTTP/2.0',
	}.get(version, 10)
