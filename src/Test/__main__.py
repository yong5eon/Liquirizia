# -*- coding: utf-8 -*-

from .Result import Result
from .Runner import Runner

from unittest import TestLoader, TestProgram
from sys import argv
from argparse import ArgumentParser

parser = ArgumentParser(prog='Liquirizia Test Runner')

parser.add_argument('path', default='.', help="Path to test('.' default)")
parser.add_argument('-v', '--verbose', dest='verbosity', action='store', default=2, help='Verbose output(default=2)')
parser.add_argument('-f', '--failfast', dest='failfast', action='store_true', help='Stop on first fail or error')
parser.add_argument('-s', '--start', dest='start', default='.', help='Start base directory of test(default=., start directory)')
parser.add_argument('-p', '--pattern', dest='pattern', default='*.py', help='Pattern of test file(default=*.py)')


args = parser.parse_args()

# load tests
loader = TestLoader()
tests =  loader.discover(args.path, top_level_dir=args.start, pattern=args.pattern)

# run tests
_ = Runner(verbosity=args.verbosity, failfast=args.failfast)
_.run(tests)