# -*- coding: utf-8 -*-

from .Loader import Loader
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

def cmp(a, b):
	return a

# load tests
loader = Loader()
tests =  loader.discover(args.path, top_level_dir=args.start, pattern=args.pattern)

# run tests
runner = Runner(verbosity=args.verbosity, failfast=args.failfast)
result = runner.run(tests)

if len(result.failures): exit(1)
if len(result.errors): exit(-1)

exit(0)