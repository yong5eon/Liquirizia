# -*- coding: utf-8 -*-

__all__ = (
	'Router'
)


class Match(object):
	def __init__(self, route, params):
		self.route = route
		self.params = params
		return


class Router(object):
	"""
	Web Application Server Router

	TODO :
	- Set default CORS
	"""
	def __init__(self):
		self.routes = []

	def matches(self, url):
		routes = {}
		
		# find matched list
		for route in self.routes:
			found, params = route.match(url)
			if not found:
				continue
			if route.method not in routes:
				routes[route.method] = []
			routes[route.method].append(Match(route, params))

		# sort ASC by parameter count
		for method in routes.keys():
			routes[method].sort(key=lambda r: len(r.params.keys()))
			routes[method] = routes[method][0]  # select top priority

		return routes

	def add(self, route):
		self.routes.append(route)
		return
