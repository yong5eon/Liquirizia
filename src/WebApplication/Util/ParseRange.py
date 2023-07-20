# -*- coding: utf-8 -*-

__all__ = (
	'ParseRange',
)


def ParseRange(range, maxlen=0):
	"""
	Yield (start, end) ranges parsed from a HTTP Range header. Skip
	unsatisfiable ranges. The end index is non-inclusive.
	"""
	if range[:6] != 'bytes=':
		return

	ranges = [r.split('-', 1) for r in range[6:].split(',') if '-' in r]

	for offset, end in ranges:
		try:
			if not offset:  # bytes=-100 : last 100 bytes
				offset, end = max(0, maxlen - int(end)), maxlen
			elif not end:  # bytes=100- : all but the first 99 bytes
				offset, end = int(offset), maxlen
			else:  # bytes=100-200 : bytes 100-200 (inclusive)
				offset, end = int(offset), min(int(end) + 1, maxlen)
			if 0 <= offset < end <= maxlen:
				yield offset, end
		except ValueError:
			pass
