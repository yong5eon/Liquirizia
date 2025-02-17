# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from time import mktime

import email
import time

__all__ = (
	'GetUTCTimezone',
	'Now',
	'ToTimestamp',
	'FromStrToTimestamp',
	'ToString',
)


def GetUTCTimezone():
	def toString(td):
		"""Convert timedelta objects to a HH:MM string with (+/-) sign"""
		if td < timedelta(seconds=0):
			sign = '-'
			td = -td
		else:
			sign = '+'
		tdhours, rem = divmod(td.total_seconds(), 3600)
		tdminutes, rem = divmod(rem, 60)
		tdstr = '{}{:02d}{:02d}'.format(sign, int(tdhours), int(tdminutes))
		return tdstr

	return 'UTC{}'.format(toString(datetime.now() - datetime.utcnow()))


def Now(utc=False):
	return datetime.now() if not utc else datetime.utcnow()


def ToTimestamp(dt: datetime):
	return mktime(dt.timetuple())


def FromStrToTimestamp(str):
	""" Parse rfc1123, rfc850 and asctime timestamps and return UTC epoch. """
	try:
		ts = email.utils.parsedate_tz(str)
		return time.mktime(ts[:8] + (0,)) - (ts[9] or 0) - time.timezone
	except (TypeError, ValueError, IndexError, OverflowError):
		return None


def ToString(dt: datetime, form="%Y/%m/%d %H:%M:%S"):
	try:
		return dt.strftime(form)
	except Exception:
		return None
