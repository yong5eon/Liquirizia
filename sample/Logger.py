from Liquirizia.Logger import (
	Logger,
	Token,
	LOG_FORMAT,
	LOG_LEVEL_DEBUG,
	LOG_LEVEL_INFO,
	LOG_LEVEL_ERROR,
	LOG_FILE_CREATE,
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

	CUSTOM_LOG_FORMAT = '{} - {} - {} - {}'.format(
		Token.FormatStr(Token.Time),
		Token.FormatStr(Token.Level, 8, align='-'),
		Token.FormatStr(Token.Name, 20, align='-'),
		Token.FormatStr(Token.Message),
	)

	print(CUSTOM_LOG_FORMAT)	

	_ = Logger('Sample Logger')
	
	_.debug('DEBUG')
	_.info('INFO')
	_.warn('WARNING')
	_.error('ERROR')

	_.setLevel(LOG_LEVEL_DEBUG)

	_.addHandler(StreamHandler(formatter=CommonFormatter(CUSTOM_LOG_FORMAT)))
	_.addHandler(StreamHandler(formatter=ColoredFormatter(CUSTOM_LOG_FORMAT)))
	_.addHandler(FileHandler('.log', formatter=CommonFormatter(CUSTOM_LOG_FORMAT)))
	_.addHandler(RotateFileHandler('.r.log', formatter=CommonFormatter(CUSTOM_LOG_FORMAT)))

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

	LOG_INIT(LOG_LEVEL_DEBUG, handler=StreamHandler(formatter=ColoredFormatter(LOG_FORMAT)))

	LOG_ADD('Sample Logger')

	LOG_SET_FILE('.app.log') # set log file
	LOG_SET_FILE('.app.r.log', max = 1048576) # set rotate log file

	LOG_DEBUG('DEBUG')
	LOG_INFO('INFO')
	LOG_WARN('WARNING')
	LOG_ERROR('ERROR')

	try:
		raise ValueError('APPLICATION LOGGER')
	except BaseException as e:
		LOG_DEBUG(str(e), e=e)
		LOG_INFO(str(e), e=e)
		LOG_WARN(str(e), e=e)
		LOG_ERROR(str(e), e=e)

	_.debug('DEBUG')
	_.info('INFO')
	_.warn('WARNING')
	_.error('ERROR')

