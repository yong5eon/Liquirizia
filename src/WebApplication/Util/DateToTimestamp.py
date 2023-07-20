# -*- coding: utf-8 -*-

from email.utils import parsedate_tz
from time import timezone, mktime

__all__ = (
	'DateToTimestamp',
)


def DateToTimestamp(str):
	""" Parse rfc1123, rfc850 and asctime timestamps and return UTC epoch. """
	try:
		ts = parsedate_tz(str)
		return mktime(ts[:8] + (0,)) - (ts[9] or 0) - timezone
	except (TypeError, ValueError, IndexError, OverflowError):
		return None
