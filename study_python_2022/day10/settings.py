#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: settings.py
# TIME: 6月  星期日

import logging.handlers
from logging import config

# 定义三种日志格式用于后期排查问题
standard_format = '%(asctime)s  %(msecs)d  %(threadName)s:%(thread)d   %(levelno)s  %(filename)s:%(lineno)d %(message)s  %(module)s'

simple_format = '%(asctime)s  %(msecs)d  %(levelno)s  %(message)s  %(module)s'

errors_format = '%(asctime)s  %(msecs)d   %(levelno)s  %(filename)s:%(lineno)d  %(message)s  %(module)s'

# 配置日志字典

LOGGING_DICT = {
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format
        },
        'simple':{
            'format':simple_format
        },
        'errors':{
            'format':errors_format
        },
    },
    'filters':{},
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',  # 打印到屏幕
            'formatter':'simple'
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'standard',
            'maxBytes':'1024*1024*10',
            'backupCount':5,
            'filename':'default.log',
            'encoding':'utf-8'
        },
        'errors':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter':'errors',
            'filename':'error.log',
            'encoding':'utf-8'
        },
    },

    'loggers':{
         'kkk':{
             'handlers':['console','errors'],
             'level':'DEBUG',
             'propagate':False
         },
         'infos':{
             'handlers':['console',],
             'level':'DEBUG',
             'propagate':False
         },
        '':{
            'handlers':['default',],
            'level':'DEBUG',
            'propagate':True   # 向上传递
        },
    },
}

config.dictConfig(LOGGING_DICT)

logger1 = logging.getLogger('kkk')
logger1.debug("debug")


