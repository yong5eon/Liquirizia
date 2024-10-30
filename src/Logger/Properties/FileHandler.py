# -*- coding: utf-8 -*-

from logging import (
    FileHandler as BaseFileHandler,
)

__all__ = (
    'FileHandledr',
    'LOG_FILE_CREATE',
    'LOG_FILE_APPEND',
)

LOG_FILE_CREATE = 'w'
LOG_FILE_APPEND = 'a'


class FileHandler(BaseFileHandler):
    def __init__(self, filename, mode = LOG_FILE_CREATE):
        super().__init__(filename, mode)
    def format(self, record):
        try:
            if getattr(record, 'file'):
                record.filename = record.file
            if getattr(record, 'line'):
                record.lineno = record.line
        except AttributeError:
            pass
        return self.formatter.format(record)
