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
from autotest.schemas.system.user import UserIn
from autotest.models.system_models import User
from autotest.db.get_db import get_db



router = APIRouter()

@router.post('/userRegister', description='新增用户')
async def user_register(user_info: UserIn, db: Session = Depends(get_db)):
    data = await UserService.user_register(db, user_info)
    print(data)