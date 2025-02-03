from Liquirizia.Logger import (
	Logger,
	LOG_LEVEL_DEBUG,
	LOG_LEVEL_INFO,
	LOG_LEVEL_ERROR,
	LOG_FILE_CREATE,
	LOG_FORMAT,
	LOG_FORMAT_WITH_NAME,
	LOG_INIT,
	LOG_ADD,
	LOG_SET_FILE,
	LOG_DEBUG,
	LOG_INFO,
	LOG_WARN,
	LOG_ERROR,
)
from Liquirizia.Logger.Properties import *
from Liquirizia.Logger.Formatters import *

if __name__ == '__main__':
	
	_ = Logger(name='Sample Logger')
	
	_.debug('DEBUG')
	_.info('INFO')
	_.warn('WARNING')
	_.error('ERROR')

	_.setLevel(LOG_LEVEL_DEBUG)

	_.addHandler(StreamHandler(formatter=Formatter(LOG_FORMAT_WITH_NAME)))
	_.addHandler(StreamHandler(formatter=ColoredFormatter(LOG_FORMAT_WITH_NAME)))
	_.addHandler(FileHandler('.log', formatter=Formatter(LOG_FORMAT_WITH_NAME)))
	_.addHandler(RotateFileHandler('.r.log', formatter=Formatter(LOG_FORMAT_WITH_NAME)))

	_.debug('DEBUG')
	_.info('INFO')
	_.warn('WARNING')
	_.error('ERROR')

	try:
		raise RuntimeError('LOGGER')
	except BaseException as e:
		_.debug('DEBUG', e=e)
		_.info('INFO', e=e)
		_.warn('WARNING', e=e)
		_.error('ERROR', e=e)

	_ = Logger('Addtional Logger')

	LOG_INIT(LOG_LEVEL_DEBUG)

	LOG_ADD('Additional Logger')

	LOG_SET_FILE('.app.log') # set log file
	LOG_SET_FILE('.app.r.log', max = 1048576) # set rotate log file

	LOG_DEBUG('DEBUG')
	_.debug('ADDITIONAL LOGGER DEBUG')
	LOG_INFO('INFO')
	_.info('ADDITIONAL LOGGER INFO')
	LOG_WARN('WARNING')
	_.warn('ADDITIONAL LOGGER WARN')
	LOG_ERROR('ERROR')
	_.warn('ADDITIONAL LOGGER ERROR')

	try:
		raise ValueError('APPLICATION LOGGER')
	except BaseException as e:
		LOG_DEBUG(str(e), e=e)
		LOG_INFO(str(e), e=e)
		LOG_WARN(str(e), e=e)
		LOG_ERROR(str(e), e=e)

	try:
		raise NotImplementedError('ADDITIONAL LOGGER')
	except BaseException as e:
		_.debug(str(e), e=e)
		_.info(str(e), e=e)
		_.warn(str(e), e=e)
		_.error(str(e), e=e)
