#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2024/01/19 16:52:11
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   用户服务端逻辑
'''
import sys
import os
GRANDFA = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.append(GRANDFA)

from sqlalchemy.orm import Session
from autotest.schemas.system.user import UserIn
from autotest.models.system_models import User
from autotest.db.get_db import get_db

class UserService:
    """用户类服务"""

    @staticmethod
    async def user_register(db: Session, user_info: UserIn) -> "User":
        """用户注册"""
        user = await User.get_user_by_name(db, user_info.username)
        if user:
            print('已被注册')
        else:
            user = await User.create_user(db, user_info)
            return user
    

if __name__ == '__main__':
    UserService.user_register("czd")

