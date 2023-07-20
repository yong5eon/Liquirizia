# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Serializer import SerializerHelper

import sys
from datetime import datetime


if __name__ == '__main__':

  val = {
    'string': 'abc',
    'integer': 1,
    'listOfInteger': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'listOfString': ['abc', 'def', 'ghi'],
    'listOfObject': [
      {
        'string': 'abc',
        'integer': 1
      },
      {
        'string': 'def',
        'integer': 2
      }
    ],
    'object': {
      'string': 'abc',
      'integer': 1,
    },
    'datetime': datetime.now(),
    'datetimes': [datetime.now(), datetime.now(), datetime.now()],
    'nested1': {
      'datetime': datetime.now(),
      'datetimes': [datetime.now(), datetime.now(), datetime.now()],
      'nested2': {
        'datetime': datetime.now(),
        'datetimes': [datetime.now(), datetime.now(), datetime.now()],
        'nested3': {
          'datetime': datetime.now(),
          'datetimes': [datetime.now(), datetime.now(), datetime.now()],
        }
      },
    }
  }

  print('ORIGIN : {}'.format(val), file=sys.stdout)

  encoded = SerializerHelper.Encode(str(val), 'text/plain')
  print('ENCODE WITH {} : {}'.format('text/plain', encoded), file=sys.stdout)
  decoded = SerializerHelper.Decode(encoded, 'text/plain')
  print('DECODE WITH {} : {}'.format('text/plain', decoded), file=sys.stdout)

  encoded = SerializerHelper.Encode(val, 'application/x-www-form-urlencoded')
  print('ENCODE WITH {} : {}'.format('application/x-www-form-urlencoded', encoded), file=sys.stdout)
  decoded = SerializerHelper.Decode(encoded, 'application/x-www-form-urlencoded')
  print('DECODE WITH {} : {}'.format('application/x-www-form-urlencoded', decoded), file=sys.stdout)

  encoded = SerializerHelper.Encode(val, 'application/json')
  print('ENCODE WITH {} : {}'.format('application/json', encoded), file=sys.stdout)
  decoded = SerializerHelper.Decode(encoded, 'application/json')
  print('DECODE WITH {} : {}'.format('application/json', decoded), file=sys.stdout)

  encoded = SerializerHelper.Encode(val, 'application/xml')
  print('ENCODE WITH {} : {}'.format('application/xml', encoded), file=sys.stdout)
  decoded = SerializerHelper.Decode(encoded, 'application/xml')
  print('DECODE WITH {} : {}'.format('application/xml', decoded), file=sys.stdout)
