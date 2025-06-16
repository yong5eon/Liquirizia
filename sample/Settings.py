# -*- coding: utf-8 -*-

from Liquirizia.Settings import (
	Settings as BaseSettings,
	Handler,
	Value
)
from Liquirizia.Validator import Validator
from Liquirizia.Validator.Patterns import *

from typing import List

class SettingHandler(Handler):
	def __call__(self, conf: 'Settings'):
		print(conf)
		return

class Settings(BaseSettings, onLoad=SettingHandler(), onLoaded=SettingHandler()):
	# MODE
	MODE: str = Value('MODE', default='DEBUG', va=Validator(IsString()))
	# SETTINGS
	LOG_LEVEL: str = 'DEBUG'
	LOG_NAME: str = 'WORKER'
	LOG_FORMAT: str = '%(asctime)s [%(levelname)s] %(message)s'
	# TIMEZONE
	TIMEZONE: str = 'Asia/Seoul'


if __name__ == '__main__':
	a = Settings()
	a.MODE = 'PRODUCTION'
	print(a)
	b = Settings()
	b.LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
	print(b)
	print(a)
