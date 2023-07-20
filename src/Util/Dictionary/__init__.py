# -*- coding: utf-8 -*-

__all__ = (
	'DeepMerge',
	'Replace',
)


def DeepMerge(tar, src):
	if not isinstance(tar, dict) or not isinstance(src, dict):
		raise RuntimeError('Illegal type, must be dict')
	origin = tar
	for key in src:
		if key in origin:
			if isinstance(origin[key], dict) and isinstance(src[key], dict):
				origin[key] = DeepMerge(origin[key], src[key])
			elif isinstance(origin[key], list) and isinstance(src[key], list):
				origin[key] = ListDeepMerge(origin[key], src[key])
			# TODO : support other types, set, tuple...
			else:
				origin[key] = src[key]
		else:
			origin[key] = src[key]
	return origin


def ListDeepMerge(tar, src):
	origin = tar
	common_length = min(len(origin), len(src))
	for idx in range(common_length):
		if isinstance(origin[idx], dict) and isinstance(src[idx], dict):
			origin[idx] = DeepMerge(origin[idx], src[idx])
		elif isinstance(origin[idx], list) and isinstance(src[idx], list):
			origin[idx] = ListDeepMerge(origin[idx], src[idx])
		# TODO : support other types, set, tuple...
		else:
			origin[idx] = src[idx]
	for idx in range(common_length, len(src)):
		origin.append(src[idx])
	return origin


def Replace(dic: dict, fn: callable):
	def ReplaceList(li: (list, tuple), fn):
		for i, l in enumerate(li):
			if isinstance(l, (list, tuple)):
				li[i] = ReplaceList(l, fn)
				continue
			if isinstance(l, dict):
				li[i] = Replace(l, fn)
				continue
			li[i] = fn(l)
		return li
	for key, val in dic.items():
		if isinstance(val, (list, tuple)):
			dic[key] = ReplaceList(val, fn)
			continue
		if isinstance(val, dict):
			dic[key] = Replace(val, fn)
			continue
		dic[key] = fn(val)
	return dic
