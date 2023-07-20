# -*- coding: utf-8 -*-

from Liquirizia.Test import Runner
from sys import stdout

_ = Runner(description='Liquirizia', file=stdout)
# _.loads('test')

# Validator
# _.load('test/Validator/01.Validator.py')

# DataModel
_.load('test/DataModelObject/01.DataModelObject.py')

_.run()
