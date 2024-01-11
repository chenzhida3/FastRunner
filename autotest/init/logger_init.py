#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   logger_init.py
@Time    :   2024/01/10 15:44:57
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   配置日志格式
'''
import sys
import os
GRANDFA = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(GRANDFA)

import logging
from config import config
from pathlib import Path
from loguru import logger
from autotest.utils.local import g
from autotest.utils.common import get_str_uuid


def create_dir(file_name: str) -> Path:
    """创建文件

    Args:
        file_name (str): 文件路径名

    Returns:
        Path: 文件路径
    """    
    path = Path(file_name).absolute().parent.parent.parent / file_name  # 拼接日志文件夹路径
    if not Path(path).exists():
        Path.mkdir(path)
    return path

def logger_file() -> str:
    """创建日志文件名

    Returns:
        str: 文件路径
    """
    log_path = create_dir(config.LOGGER_DIR)
    print(log_path)

    """ 保留日志文件夹下最大个数(本地调试用) 
    本地调式需要多次重启, 日志轮转片不会生效 """
    file_list = os.listdir(log_path)
    if len(file_list) > 3:
        os.remove(os.path.join(log_path, file_list[0]))
    
    return os.path.join(log_path, config.LOGGER_NAME)

def correlation_id_filter(record):
    if not g.trace_id:
        g.trace_id = get_str_uuid()
    record['trace_id'] = g.trace_id
    return record

# 详见: https://loguru.readthedocs.io/en/stable/overview.html#features
fmt = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>| {thread} | <level>{level: <8}</level> | <yellow> {trace_id} </yellow> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
logger.remove()
logger.add(
    # logger_file(),
    sys.stdout,
    # encoding=config.GLOBAL_ENCODING,
    level=config.LOGGER_LEVEL,
    colorize=True,
    # rotation=config.LOGGER_ROTATION,
    # retention=config.LOGGER_RETENTION,
    filter=correlation_id_filter,
    format=fmt,
    # enqueue=True
)


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(level, record.getMessage())


def init_logger():
    logger_name_list = [name for name in logging.root.manager.loggerDict]

    for logger_name in logger_name_list:
        """获取所有logger"""
        effective_level = logging.getLogger(logger_name).getEffectiveLevel()
        if effective_level < logging.getLevelName(config.LOGGER_LEVEL.upper()):
            logging.getLogger(logger_name).setLevel(config.LOGGER_LEVEL.upper())
        if '.' not in logger_name:
            logging.getLogger(logger_name).handlers = []
            logging.getLogger(logger_name).addHandler(InterceptHandler())



if __name__ == '__main__':
    logger_file()