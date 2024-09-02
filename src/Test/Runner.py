# -*- coding: utf-8 -*-

from .Result import Result

from typing import TextIO
from sys import stderr
from unittest import registerResult
from warnings import catch_warnings, simplefilter, filterwarnings
from time import perf_counter

__all__ = (
	'Runner'
)


CR = '\r'
LF = '\n'

RESET = '\033[0m' # called to return to standard terminal text color

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'


class Runner(object):
	def __init__(
		self,
		stream: TextIO = stderr,
		description: bool = True,
		failfast: bool = False,
		verbosity: int = 2,
		resultType = Result
	):
		self.stream = stream
		self.description = description
		self.failfast = failfast
		self.verbosit = verbosity
		self.resultType = resultType
		return
	
	def createResult(self):
		return self.resultType(self.stream, self.description, self.verbosit, self.failfast)

	def run(self, test):
		self.stream.write(CR + LF)
		self.stream.write(CYAN)
		self.stream.write('Liquirizia Test Run...')
		self.stream.write(RESET)
		self.stream.write(LF)
		result = self.createResult()
		registerResult(result)
		with catch_warnings():
			startTime = perf_counter()
			startTestRun = getattr(result, 'startTestRun', None)
			if startTestRun is not None:
				startTestRun()
			try:
				test(result)
			finally:
				stopTestRun = getattr(result, 'stopTestRun', None)
				if stopTestRun is not None:
					stopTestRun()
			stopTime = perf_counter()
		timeTaken = stopTime - startTime
		result.printErrors()
		self.stream.write(DARK_GRAY)
		self.stream.write('-' * 80)
		self.stream.write(RESET)
		self.stream.write(LF)
		self.stream.write(DARK_GRAY)
		self.stream.write('TOTAL DURATION {:64.3f}s'.format(timeTaken))
		self.stream.write(RESET)
		self.stream.write(LF)
		self.stream.flush()
		return result
