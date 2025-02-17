# -*- coding: utf-8 -*-

__all__ = (
	'DeepMerge',
	'Remove',
	'RemoveDuplicate',
	'ToString',
	'ToDictionary',
)


def DeepMerge(tar, src):
	origin = tar
	common_length = min(len(origin), len(src))
	for idx in range(common_length):
		if isinstance(origin[idx], dict) and isinstance(src[idx], dict):
			origin[idx] = DictDeepMerge(origin[idx], src[idx])
		elif isinstance(origin[idx], list) and isinstance(src[idx], list):
			origin[idx] = DeepMerge(origin[idx], src[idx])
		# TODO : support other types, set, tuple...
		else:
			origin[idx] = src[idx]
	for idx in range(common_length, len(src)):
		origin.append(src[idx])
	return origin


def DictDeepMerge(tar, src):
	if not isinstance(tar, dict) or not isinstance(src, dict):
		raise RuntimeError('Illegal type, must be dict')
	origin = tar
	for key in src:
		if key in origin:
			if isinstance(origin[key], dict) and isinstance(src[key], dict):
				origin[key] = DeepMerge(origin[key], src[key])
			elif isinstance(origin[key], list) and isinstance(src[key], list):
				origin[key] = DeepMerge(origin[key], src[key])
			# TODO : support other types, set, tuple...
			else:
				origin[key] = src[key]
		else:
			origin[key] = src[key]
	return origin


def Remove(src, fn):
	ret = []
	if not isinstance(src, list):
		return None
	for i in src:
		if fn(i):
			continue
		ret.append(i)
	return ret


def RemoveDuplicate(src):
	return list(dict.fromkeys(src))


def ToString(src, delimiter=', '):
	return delimiter.join(src)


def ToDictionary(src, key, removeOriginKey=True):
	"""
	src = [
		{'name': '허용선', 'gender': 'm', 'addr': '왕십리'},
		{'name': '홍승걸', 'gender': 'm', 'addr': '성수'},
		{'name': '최준호', 'gender': 'm', 'addr': '성수'},
	]
	data = ToDictionary(src=src, key="name")
	return {
		'허용선': {'gender': 'm', 'addr': '왕십리'},
		'홍승걸': {'gender': 'm', 'addr': '성수'},
		'최준호': {'gender': 'm', 'addr': '성수'},
	}

	:param src: List<Dict<String, Object>>
	:param key: 딕셔너리로 변환시 기준 키
	:param removeOriginKey: 기준키로 사용한 키 기존 Dict에서 제거여부(기본값은 제거)
	:return: Dict<String, Dict<String, Object>>
	"""
	ret = {}
	if not isinstance(src, list):
		return None
	for v in src:
		ret[v[key]] = v
		if removeOriginKey:
			del ret[v[key]][key]
	return ret

