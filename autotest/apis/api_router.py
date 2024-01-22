#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   api_router.py
@Time    :   2024/01/22 14:15:00
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   api路由
'''

from fastapi import APIRouter

from autotest.apis.system import user

app_router = APIRouter()


# system 

app_router.include_router(user.router, prefix='/user', tags=['user'])