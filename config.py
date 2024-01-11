#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2024/01/10 15:48:05
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   存放配置的文件
'''
from pydantic_settings import BaseSettings


class Configs(BaseSettings):

    # logger
    LOGGER_DIR: str = 'logs'   # 日志文件夹名
    LOGGER_NAME: str = 'FastRunner.log'  # 日志文件名
    LOGGER_LEVEL: str = 'INFO'  # 日志等级
    LOGGER_ROTATION: str = "10 MB"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]


config = Configs()