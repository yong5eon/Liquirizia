# -*- coding: utf-8 -*-

from typing import TextIO
from unittest import TestResult as BaseTestResult, TestCase
from time import time

__all__ = (
	'Result'
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


class Result(BaseTestResult):

	def __init__(
		self,
		stream: TextIO = None,
		descriptions: bool = None,
		verbosity: int = None,
		failfast: bool = False,
	) -> None:
		super().__init__(stream, descriptions, verbosity)
		self.stream = stream
		self.verbosity = verbosity
		self.fmt = '{result:6} - {duration:7.03f} - {class}.{method}'
		self.succeeded = []
		self.tb_locals = True
		return
	
	def startTestRun(self) -> None:
		self.stream.write(WHITE)
		self.stream.write('=' * 80)
		self.stream.write(RESET)
		self.stream.write(LF)
		return super().startTestRun()
	
	def stopTestRun(self) -> None:
		for f in self.failures:
			self.stream.write(YELLOW)
			self.stream.write('-' * 80)
			self.stream.write(LF)
			self.stream.write('FAIL   - ')
			self.stream.write('{}.{}'.format(f[0].__properties__['class'], f[0].__properties__['method']))
			self.stream.write(LF)
			self.stream.write('-' * 80)
			self.stream.write(LF)
			self.stream.write(f[1])
			self.stream.write(RESET)
		for e in self.errors:
			self.stream.write(BRIGHT_RED)
			self.stream.write('-' * 80)
			self.stream.write(LF)
			self.stream.write('ERROR  - ')
			self.stream.write('{}.{}'.format(e[0].__properties__['class'], e[0].__properties__['method']))
			self.stream.write(LF)
			self.stream.write('-' * 80)
			self.stream.write(LF)
			self.stream.write(e[1])
			self.stream.write(RESET)
		self.stream.write(WHITE)
		self.stream.write('=' * 80)
		self.stream.write(RESET)
		self.stream.write(LF)
		self.stream.write('TOTAL  - {:71}'.format(self.testsRun))
		self.stream.write(LF)
		if len(self.succeeded):
			self.stream.write(GREEN)
			self.stream.write('PASS   - {:71}'.format(len(self.succeeded)))
			self.stream.write(RESET)
			self.stream.write(LF)
		if len(self.failures):
			self.stream.write(YELLOW)
			self.stream.write('FAIL   - {:71}'.format(len(self.failures)))
			self.stream.write(RESET)
			self.stream.write(LF)
		if len(self.errors):
			self.stream.write(BRIGHT_RED)
			self.stream.write('ERROR  - {:71}'.format(len(self.errors)))
			self.stream.write(RESET)
			self.stream.write(LF)
		if len(self.skipped):
			self.stream.write(DARK_GRAY)
			self.stream.write('SKIP   - {:71}'.format(len(self.skipped)))
			self.stream.write(RESET)
			self.stream.write(LF)
		return super().stopTestRun()
	
	def startTest(self, test: TestCase) -> None:
		super().startTest(test)
		test.__properties__ = {
			'module': test.__module__,
			'class': test.__class__.__name__,
			'method': test._testMethodName,
			'start': time(),
			'end': None,
			'duration': None,
			'result': None,
			'error': None,
			'traceback': None,
			'reason': None,
		}
		return
	
	def stopTest(self, test: TestCase) -> None:
		test.__properties__['end'] = time()
		test.__properties__['duration'] = test.__properties__['end'] - test.__properties__['start']
		if test.__properties__['result'] == 'PASS': self.stream.write(GREEN)
		if test.__properties__['result'] == 'FAIL': self.stream.write(YELLOW)
		if test.__properties__['result'] == 'ERROR': self.stream.write(BRIGHT_RED)
		if test.__properties__['result'] == 'SKIP': self.stream.write(DARK_GRAY)
		self.stream.write(self.fmt.format(**test.__properties__))
		self.stream.write(RESET)
		self.stream.write(LF)
		return super().stopTest(test)
	
	def addSuccess(self, test: TestCase) -> None:
		test.__properties__['result'] = 'PASS'
		self.succeeded.append(test)
		return super().addSuccess(test)

	def addFailure(self, test: TestCase, err) -> None:
		test.__properties__['result'] = 'FAIL'
		test.__properties__['error'] = err[1]
		test.__properties__['traceback'] = err[2]
		return super().addFailure(test, err)
	
	def addError(self, test: TestCase, err) -> None:
		test.__properties__['result'] = 'ERROR'
		test.__properties__['error'] = err[1]
		test.__properties__['traceback'] = err[2]
		test.__properties__['traceback'] = err[2]
		return super().addError(test, err)
	
	def addSkip(self, test: TestCase, reason: str) -> None:
		test.__properties__['result'] = 'SKIP'
		test.__properties__['reason'] = reason
		return super().addSkip(test, reason)
