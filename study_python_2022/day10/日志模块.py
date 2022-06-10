#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: 日志模块.py
# TIME: 6月  星期三

# import logging
#
# logging.basicConfig(
#     # 日志输出位置：终端，文件
#     filename='access.log',encoding='utf-8', # 不指定，默认打印到终端
#
#
#     # 日志格式
#     # format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(pathname)s - %(filename)s - %(module)s',
#     # format='%(asctime)s   %(levelname)s   %(name)s   %(message)s    %(module)s',
#     format='%(asctime)s   %(levelname)s   %(name)s  %(user)s[%(ip)s]  %(message)s    %(module)s',
#
#     # 时间格式
#     datefmt='%Y-%m-%d %H:%M:%S ',
#
#     # 日志级别
#     # critical => 50
#     # error => 40
#     # warning => 30
#     # info => 20
#     # debug => 10
#     # level=10
#     level=logging.DEBUG,
# )
#
#
# logging.warning("等待请求.",extra={'user':'张三','ip':'172.16.0.1'})

# logging.basicConfig(filename='my.log',encoding='utf-8',level=20)
# logging.debug("调式日志")
# logging.info("消息日志")
# logging.warning("警告日志")
# logging.error("错误日志")
# logging.critical("严重critical")

# logging.log(logging.DEBUG,"debug")
# logging.log(logging.INFO,"Info")
# logging.log(logging.WARNING,"Warning")
# logging.log(logging.ERROR,"Error")
# logging.log(logging.CRITICAL,"Critical")

# import logging
# import logging.handlers
# import datetime
#
# logger = logging.getLogger('mylog') # 定义文件
# logger.setLevel(logging.DEBUG)  # 设置日志级别
#
# rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',encoding='utf-8',when='midnight',interval=1,backupCount=7,atTime=datetime.time(0,0,0,0))
# rf_handler.setFormatter("%(asctime)s  %(levelname)s  %(message)s")
#
# # f_handler = logging.FileHandler('error.log',encoding='utf-8')
# f_handler = logging.FileHandler('error.log',encoding='utf-8')
# f_handler.setLevel(logging.DEBUG)
# f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
#
# logger.addHandler(rf_handler)
# logger.addHandler(f_handler)

# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# import logging.config
# import logging.handlers

# 定义三种日志格式用于后期排查问题
# standard_format = '%(asctime)s  %(msecs)d  %(threadName)s:%(thread)d   %(levelno)s  %(filename)s:%(lineno)d %(message)s  %(module)s'
#
# simple_format = '%(asctime)s  %(msecs)d  %(levelno)s  %(message)s  %(module)s'
#
# errors_format = '%(asctime)s  %(msecs)d   %(levelno)s  %(filename)s:%(lineno)d  %(message)s  %(module)s'
#
# # 配置日志字典
#
# LOGGING_DICT = {
#     'version':1,
#     'disable_existing_loggers':False,
#     'formatters':{
#         'standard':{
#             'format':standard_format
#         },
#         'simple':{
#             'format':simple_format
#         },
#         'errors':{
#             'format':errors_format
#         }
#     },
#     'filters':{},
#     'handlers':{
#         'console':{
#             'level':'DEBUG',
#             'class':'logging.StreamHandler',
#             'formatter':'simple'
#         },
#         'defaults':{
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'maxBytes':'1024*1024*10',
#             'backupCount':5,
#             'filename':'default.log',
#             'encoding':'utf-8',
#             'formatter':'standard'
#         },
#         'errors':{
#             'level':'DEBUG',
#             'class':'logging.FileHandler',
#             'filename':'error.log',
#             'encoding':'utf-8',
#             'formatter':'errors'
#         }
#     },
#
#     'loggers':{
#          'kkk':{
#              'handlers':['console','errors'],
#              'level':'DEBUG',
#              'propagate':False
#          },
#          'infos':{
#              'handlers':['console',],
#              'level':'DEBUG',
#              'propagate':False
#          },
#         '':{
#             'handlers':['defaults',],
#             'level':'DEBUG',
#             'propagate':False
#         }
#     }
# }


# 配置日志格式
import logging.handlers
from logging import config

standard_format = '%(asctime)s- %(threadName)s:%(thread)d - 日志名字:%(name)s - %(filename)s:%(lineno)d -%(levelname)s - %(message)s'

simple_format = '%(levelname)s  %(asctime)-15s  %(filename)-8s:%(lineno)d 8s %(message)s'

test_format = '%(asctime)s] %(message)s'

# 日志字典
LOGGING_DICT = {
    'version':1,  # 版本
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format
        },
        'simple':{
            'format':simple_format
        },
        'test':{
            'format':test_format
        }
    },
    'filters':{},
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'simple'
        },
        'default':{
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            # 'formatter':'standard',
            'formatter':'simple',
            'maxBytes':1024*1024*10,
            'backupCount':7,
            'filename':'default.log',
            'encoding':'utf-8'
        },
        'other':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter':'test',
            'filename':'test.log',
            'encoding':'utf-8'
        }
    },
    'loggers':{
        'kkk':{
            'handlers':['console','other'],
            'level':'DEBUG',
            'propagate':False
        },
        '终端提示':{
            'handlers':['console'],
            'level':'DEBUG',
            'propagate':False
        },
        '':{
            'handlers':['default'],
            'level':'DEBUG',
            'propagate':False
        }
    }
}

config.dictConfig(LOGGING_DICT)

logger1 = logging.getLogger('kkk')
logger1.debug("debug !")

logger2 = logging.getLogger('终端提示')
# logger2.info('info !')
# logger2.warning('2 warning')
# logger2.error('2 error')
# logger2.critical('2 critical')

logger3 = logging.getLogger('交易')
logger3.error('Eroor!')
logger3.info('3 info')
logger3.error('3 error')
logger3.warning('3 warning')
logger3.critical('3333')

logger4 = logging.getLogger('None')
logger4.warning('warning')




