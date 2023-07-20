# -*- coding: utf-8 -*-

from platform import system
from signal import signal

__all__ = (
	'Signal'
)


class Signal(object):
	"""
	System Signal Handling Class

	Usage
	------
	from System import Signal

	signal=Signal(Signal.HUP, Signal.QUIT, Signal.KILL, Signal.SEGV, Signal.STOP, fn=models)

	while not signal.now():
		....
		do_something()
		...
	
	"""

	NONE = 0  # None signal
	HUP = 1 if system().upper() != 'WINDOWS' else 2
	INT = 2
	QUIT = 3 if system().upper() != 'WINDOWS' else 2
	ILL = 4
	TRAP = 5
	IOT = 6
	EMT = 7
	FPE = 8
	KILL = 9 if system().upper() != 'WINDOWS' else 2
	BUS = 10
	SEGV = 11
	SYS = 12
	PIPE = 13
	ALRM = 14
	TERM = 15
	URG = 16
	STOP = 17 if system().upper() != 'WINDOWS' else 2
	TSTP = 18
	CONT = 19
	CHLD = 20
	TTIN = 21
	TTOU = 22
	IO = 23
	XCPU = 24
	XFSZ = 25
	VTALRM = 26
	PROF = 27
	WINCH = 28
	INFO = 29
	USR1 = 30
	USR2 = 31

	def __init__(self, *args, fn=None):
		self.sig = Signal.NONE
		self.dic = dict()
		for i, sig in enumerate(args):
			self.attach(sig, fn)
		return

	def __handle__(self, sig, frame):
		self.sig = sig
		if sig not in self.dic:
			return
		self.dic[sig](sig)
		return

	def attach(self, sig, fn=None):
		self.dic[sig] = fn
		signal(sig, self.__handle__)
		return

	def detach(self, sig):
		signal(sig, None)
		del self.dic[sig]
		return

	def now(self):
		return self.sig
