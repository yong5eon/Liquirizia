# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Serializer import SerializerHelper

from Liquirizia.WebApplication.Validator import Validator, Error, ErrorResponse
from Liquirizia.WebApplication.Validator.Patterns import *

from Liquirizia.WebApplication.Response import Response
from Liquirizia.WebApplication.Errors import *

from sys import stderr


class RequiredError(Error):
	def __call__(self, parameter, arg):
		return BadRequestError(reason='{} 에는 {} 값이 필요합니다.'.format(parameter, arg))


class RequiredResponse(ErrorResponse):
	def __call__(self, parameter, args):
		body = '{} 는 {} 필드를 충족해야 합니다.'.format(parameter, args).encode('utf-8')
		response = Response(
			status=400,
			message='Bad Request',
			version='HTTP/1.1',
			headers={
				'Content-Length': len(body)
			},
			body=body,
			format='text/plain',
			charset='utf-8'
		)
		return response


class InvalidDataError(Error):
	def __call__(self, parameter, arg):
		return BadRequestError(reason='{} 이 {} 는 다릅니다.'.format(parameter, arg))


class InvalidDataErrorResponse(ErrorResponse):
	def __call__(self, parameter, arg):
		body = '{} 는 {} 이어야 합니다.'.format(parameter, arg).encode('utf-8')
		response = Response(
			status=400,
			message='Bad Request',
			version='HTTP/1.1',
			headers={
				'Content-Length': len(body)
			},
			body=body,
			format='text/plain',
			charset='utf-8'
		)
		return response


if __name__ == '__main__':

	qs = SerializerHelper.Decode('a=1&b=2.1&c=안녕'.encode('utf-8'), format='application/x-www-form')

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', 'd'),
			IsDictionary({
				'a': IsInteger(),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected RuntimeError caused by 'd' is required
	except RuntimeError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', 'd', error=RequiredError()),
			IsDictionary({
				'a': IsInteger(),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected BadRequestError caused by 'd' is required
	except BadRequestError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', 'd', error=RequiredError(), errorResponse=RequiredResponse()),
			IsDictionary({
				'a': IsInteger(),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected return response
		if response:
			print(response)
			print(response.body.decode('utf-8'))
	except BadRequestError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', error=RequiredError(), errorResponse=RequiredResponse()),
			IsDictionary({
				'a': IsInteger(IsEqualTo(2)),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected raise RuntimeError from IsEqualTo
		if response:
			print(response)
			print(response.body.decode('utf-8'))
	except RuntimeError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', error=RequiredError(), errorResponse=RequiredResponse()),
			IsDictionary({
				'a': IsInteger(IsEqualTo(2, error=InvalidDataError())),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected raise BadRequest from IsEqualTo
		if response:
			print(response)
			print(response.body.decode('utf-8'))
	except BadRequestError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', error=RequiredError(), errorResponse=RequiredResponse()),
			IsDictionary({
				'a': IsInteger(IsEqualTo(2, error=InvalidDataError(), errorResponse=InvalidDataErrorResponse())),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected return response from IsEqualTo
		if response:
			print(response)
			print(response.body.decode('utf-8'))
	except BadRequestError as e:
		print(str(e), file=stderr)

	try:
		qsv = Validator(
			IsRequiredInDictionary('a', 'b', 'c', error=RequiredError(), errorResponse=RequiredResponse()),
			IsDictionary({
				'a': IsInteger(IsEqualTo(1, error=InvalidDataError(), errorResponse=InvalidDataErrorResponse())),
				'b': IsFloat(),
				'c': IsString(),
			}),
		)
		qs, response = qsv(qs)  # expected pass over
		if response:
			print(response)
			print(response.body.decode('utf-8'))
		else:
			print('OK')
	except BadRequestError as e:
		print(str(e), file=stderr)
