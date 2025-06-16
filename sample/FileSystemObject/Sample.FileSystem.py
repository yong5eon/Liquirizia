# -*- coding: utf-8 -*-

from Liquirizia.FileSystemObject import Helper
from Liquirizia.FileSystemObject.Implements.FileSystem import Configuration, Connection

from random import sample

if __name__ == '__main__':

    Helper.Set(
        'Sample',
        Connection,
        Configuration('.')
    )

    fo: Connection = Helper.Get('Sample')

    PATTERN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    with fo.open('Sample.txt', 'w') as f:
        f.write(''.join(sample(PATTERN, 12)))
        f.close()

    with fo.open('Sample.txt', 'r') as f:
        print(f.read())
        f.close()
