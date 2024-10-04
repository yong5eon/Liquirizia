# -*- coding: utf-8 -*-

from Liquirizia.Test import Loader, Runner

PATH = 'test'
START = '.'
PATTERN = '*.py'

# load tests
loader = Loader()
tests =  loader.discover(PATH, top_level_dir=START, pattern=PATTERN)

# run tests
runner = Runner(verbosity=2, failfast=False)
result = runner.run(tests)

if len(result.failures): exit(1)
if len(result.errors): exit(-1)

exit(0)