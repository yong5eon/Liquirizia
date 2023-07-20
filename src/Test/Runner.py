# -*- coding: utf-8 -*-

from Liquirizia.Template import Singleton

from .Case import Case
from .Fixture import Fixture
from .Pattern import Pattern

from sys import stderr
from shutil import get_terminal_size

from importlib.machinery import SourceFileLoader
from platform import system
from os import getcwd, walk
from os.path import splitext, split
from pathlib import Path
from traceback import format_tb

__all__ = (
  'Runner'
)


class Runner(Singleton):
	"""
	Test Runner
	"""	

	ColorBlack = 30
	ColorRed = 31
	ColorGreen = 32
	ColorYellow = 33
	ColorBlue = 34
	ColorMagenta = 35
	ColorCyan = 36
	ColorWhite = 37


	def __init__(
		self, 
		setup: Fixture = None, 
		teardown: Fixture = None, 
		check: Pattern = None, 
		description: str = None, 
		ColorInfo: int = ColorYellow,
		ColorSuccess: int = ColorGreen,
		ColorFail: int = ColorRed,
		ColorMessage: int = ColorCyan,
		file=stderr,
	):
		self.setup = setup
		self.teardown = teardown
		self.check = check
		self.description = description
		self.cases = list[Case]()
		self.file = file
		self.ColorInfo = ColorInfo
		self.ColorSuccess = ColorSuccess
		self.ColorFail = ColorFail
		self.ColorMessage = ColorMessage
		self.columns, _ = get_terminal_size()
		return

	def addSetup(self, fixture: Fixture):
		pass

	def addTeardown(self, fixture: Fixture):
		pass

	def addCheck(self, pattern: Pattern):
		pass

	def add(
		self, 
		case: Case, 
		pattern: Pattern, 
		setup: Fixture = None,
		teardown: Fixture = None,
	):
		self.cases.append((case, pattern, setup, teardown))
		return

	def print(self, message, color=ColorWhite):
		print('\33[{}m{}\33[0m'.format(color, message), file=self.file)
		return

	def printc(self, case, pattern, message, color):
		print('\33[{}m{} {} - {}\33[0m'.format(color, case, pattern, message), file=self.file)
		# print('{} {} - {}'.format(
		# 	case,
		# 	pattern,
		# 	'\33[{}m{}\33[0m'.format(Color, message),
		# ))
		return

	def run(self):
		self.print('Start tests{}'.format(' - {}'.format(self.description) if self.description else ''), color=self.ColorMessage)
		stat = [0, 0, 0, 0]
		for case, pattern, setup, teardown in self.cases:
			success, fail, error = self.test(case, pattern, setup, teardown)
			if success:
				stat[1] += 1
			if fail:
				stat[2] += 1
			if error:
				stat[2] += 1
			stat[0] += 1
		self.print('Done', color=self.ColorMessage)
		self.print('-' * self.columns)
		self.print('Total               : {}'.format(stat[0]), color=self.ColorInfo)
		self.print('Success             : {}'.format(stat[1]), color=self.ColorInfo)
		self.print('Fail                : {}'.format(stat[2]), color=self.ColorInfo)
		self.print('Fail with Exception : {}'.format(stat[3]), color=self.ColorInfo)
		return

	def test(
		self, 
		case: Case, 
		pattern: Pattern, 
		setup: Fixture = None,
		teardown: Fixture = None,
	):
		stat = [0, 0, 0, 0]
		try:
			if pattern(case):
				self.printc(case, pattern, 'OK', color=self.ColorSuccess)
				return 1, 0, 0
			else:
				self.printc(case, pattern, 'Fail', color=self.ColorFail)
				return 0, 1, 0
		except Exception as e:
			self.printc(case, pattern, 'Fail with Exception({}: {})'.format(e.__class__.__name__, str(e)), color=self.ColorFail)
			for line in ''.join(format_tb(e.__traceback__)).strip().split('\n'):
				self.print(line, color=self.ColorFail)
			return 0, 1, 1
		return

	def loads(self, path, pattern='*.py'):
		if not pattern:
			head, tail = split(path)
			ps = Path(head).glob(tail)
		else:
			ps = Path(path).rglob(pattern)
		for p in ps if ps else []:
			self.load(str(p))
		return

	def load(self, path):
		head, tail = split(path)
		file, ext = splitext(tail)
		head = head.replace('\\', '.').replace('/', '.')
		mod = '{}.{}'.format(head, file)
		loader = SourceFileLoader(mod, path)
		loader.load_module()
		return
