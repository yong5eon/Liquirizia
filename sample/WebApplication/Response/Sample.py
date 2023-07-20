# -*- coding: utf-8 -*-

from Liquirizia.WebApplication import Response


if __name__ == '__main__':
	response = Response(
		200,
		'OK',
		'HTTP/1.1',
		headers={
			'Content-Length': 10
		},
		body='0123456789'.encode('utf-8'),
		format='text/plain',
		charset='utf-8'
	)
	print(response)
