#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   router_init.py
@Time    :   2024/01/22 14:12:56
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   路由初始化
'''
from fastapi import FastAPI
from autotest.apis.api_router import app_router
from config import config


def init_router(app: FastAPI):
    """注册路由"""
    app.include_router(app_router, prefix=config.API_PREFIX)