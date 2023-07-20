# -*- coding: utf-8 -*-

from Liquirizia.WebApplication.Client import Client


if __name__ == '__main__':

	client = Client('www.google.com', port=443, protocol='https')

	if client.connect():
		if client.get('/'):
			response = client.response()
			print(str(response))
		client.close()
