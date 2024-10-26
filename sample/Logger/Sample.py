from Liquirizia.Logger import (
    Logger,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_INFO,
    LOG_LEVEL_ERROR,
    LOG_INIT,
    LOG_SET_FILE,
    LOG_FILE_CREATE,
    LOG_DEBUG,
    LOG_INFO,
    LOG_WARN,
    LOG_ERROR,
)
from Liquirizia.Logger.Properties import ColoredStreamHandler

from logging import StreamHandler

_1 = Logger(LOG_LEVEL_DEBUG, name='1')
_1.add(ColoredStreamHandler())

_2 = Logger(LOG_LEVEL_INFO, name='2')
_2.add(StreamHandler())

import sys

_1.debug('debug')
_2.debug('debug')
_1.info('info')
_2.info('info')
_1.warn('warn')
_2.warn('warn')
_1.error('error')
_2.error('error')


try:
    raise RuntimeError('runtime erorr')
except BaseException as e:
    _1.debug(str(e), e)
    _1.info(str(e), e)
    _1.warn(str(e), e)
    _1.error(str(e), e)
    _2.debug(str(e), e)
    _2.info(str(e), e)
    _2.warn(str(e), e)
    _2.error(str(e), e)

_3 = Logger(LOG_LEVEL_ERROR, name='3')

LOG_INIT(LOG_LEVEL_DEBUG)
LOG_SET_FILE('.log')
LOG_SET_FILE('.r.log', max = 1024)

LOG_DEBUG('DEBUG')
LOG_INFO('INFO')
LOG_WARN('WARN')
LOG_ERROR('ERROR')

_3.debug('debug')
_3.info('info')
_3.warn('warn')
_3.error('error')


try:
    raise RuntimeError('RUNTIME ERROR')
except BaseException as e:
    LOG_DEBUG(str(e), e)
    LOG_INFO(str(e), e)
    LOG_WARN(str(e), e)
    LOG_ERROR(str(e), e)
