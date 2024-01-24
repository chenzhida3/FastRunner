#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2024/01/22 13:55:54
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   接口user
'''

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from autotest.services.system.user import UserService
from autotest.schemas.system.user import UserIn, UserQuery
from autotest.utils.http_response import resp_200
from autotest.db.get_db import get_db
from fastapi.encoders import jsonable_encoder



router = APIRouter()

@router.post('/userRegister', description='新增用户')
async def user_register(user_info: UserIn, db: Session = Depends(get_db)):
    data = await UserService.user_register(db, user_info)
    return resp_200(data=data)

@router.post("/list", description="用户列表")
async def user_list(params:UserQuery, db: Session = Depends(get_db)):
    data = await UserService.list(db, params)
    return resp_200(data=data)
    