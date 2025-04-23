from Liquirizia.Logger import (
	LOG_FORMAT,
	LOG_LEVEL_DEBUG,
	LOG_LEVEL_INFO,
	LOG_LEVEL_ERROR,
	LOG_FILE_CREATE,
	LOG_INIT,
	LOG_GET,
	LOG_SET_FILE,
	LOG_SET_HANDLER,
	LOG_DEBUG,
	LOG_INFO,
	LOG_WARN,
	LOG_ERROR,
)
from Liquirizia.Logger.Properties import *
from Liquirizia.Logger.Formatters import *

from logging import getLogger, Handler
from sys import stderr

class SampleHandler(Handler):
	def emit(self, record):
		if record.levelname != LOG_LEVEL_ERROR:
			return
		print(record.message, file=stderr)
		if record.exc_info:
			print(record.exc_info, file=stderr)
		return


if __name__ == '__main__':

	LOG_FORMAT = '%(asctime)s - %(levelname)-8s - %(process)6s - %(thread)12s - %(filename)s:%(lineno)s - %(message)s'

	LOG_INIT(LOG_LEVEL_DEBUG, handler=StreamHandler(formatter=ColoredFormatter(LOG_FORMAT)))

	LOG_SET_FILE('Sample.log') # set log file
	LOG_SET_FILE('Sample.r.log', max = 1048576) # set rotate log file

	LOG_SET_HANDLER(SampleHandler()) # set custom handler

	LOG_DEBUG('DEBUG')
	LOG_INFO('INFO')
	LOG_WARN('WARNING')
	LOG_ERROR('ERROR')

	try:
		raise ValueError('Value Error')
	except Exception as e:
		LOG_DEBUG(str(e), e=e)
		LOG_INFO(str(e), e=e)
		LOG_WARN(str(e), e=e)
		LOG_ERROR(str(e), e=e)

	extern = getLogger('External Logger')

	LOG_GET('External Logger')

	extern.debug('EXTERNAL LOGGER DEBUG')
	extern.info('EXTERNAL LOGGER INFO')
	extern.warning('EXTERNAL LOGGER WARNING')
	extern.error('EXTERNAL LOGGER ERROR')

	try:
		raise RuntimeError('Runtime Error')
	except Exception as e:
		extern.debug(str(e), exc_info=e)
		extern.info(str(e), exc_info=e)
		extern.warning(str(e), exc_info=e)
		extern.error(str(e), exc_info=e)

