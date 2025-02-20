# -*- coding: utf-8 -*-

from .Loader import Loader
from .Runner import Runner

from argparse import ArgumentParser

from sys import stderr

parser = ArgumentParser(prog='Liquirizia Test Runner')

parser.add_argument('path', help="File or Module to test")

parser.add_argument('-n', '--pattern', dest='pattern', default='*.py', help='Pattern of test file(default=*.py)')
parser.add_argument('-t', '--base', dest='base', help='Top level directory of test from path')

parser.add_argument('-v', '--verbose', dest='verbosity', action='store', default=2, help='Verbose output(default=2)')
parser.add_argument('-s', '--failfast', dest='failfast', action='store_true', help='Stop on first fail or error')

args = parser.parse_args()

if not args.path:
	parser.print_help(file=stderr)
	exit(-1)

# load tests
loader = Loader()

tests = None

try:
	tests =  loader.file(args.path)
except Exception as e:
	tests =  loader.discover(args.path, pattern=args.pattern, top_level_dir=args.base)
finally:
	if not tests:
		print('No Test Found\n', file=stderr)
		parser.print_help(file=stderr)
		exit(0)

# run tests
runner = Runner(verbosity=args.verbosity, failfast=args.failfast)
result = runner.run(tests)

if len(result.failures): exit(0)
if len(result.errors): exit(0)

exit(0)