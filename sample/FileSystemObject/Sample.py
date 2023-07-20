# -*- coding: utf-8 -*-

from Liquirizia.FileSystemObject import FileSystemObjectHelper
from Liquirizia.FileSystemObject.Implements.FileSystem import FileSystemObject, FileSystemObjectConfiguration


if __name__ == '__main__':
	FileSystemObjectHelper.Set(
		'Sample',
		FileSystemObject,
		FileSystemObjectConfiguration('.')
	)

	fo = FileSystemObjectHelper.Get('Sample')

	with fo.open('Sample.txt', 'w') as f:
		f.write('Hello World')
		f.close()

	with fo.open('Sample.txt', 'r') as f:
		print(f.read())
		f.close()
