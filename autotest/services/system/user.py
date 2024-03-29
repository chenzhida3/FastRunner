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
from autotest.schemas.system.user import UserIn, UserQuery
from autotest.models.system_models import User
from autotest.utils.codes import CodeEnum
from autotest.utils.jwtTool import Jwt_tool
from autotest.utils.http_response import resp_502

from fastapi_pagination import Page
from fastapi.encoders import jsonable_encoder


class UserService:
    """用户类服务"""

    @staticmethod
    async def user_register(db: Session, user_info: UserIn) -> "dict":
        """用户注册"""
        user = await User.get_user_by_name(db, user_info.username)
        if user:
            data = {"code":CodeEnum.USERNAME_OR_EMAIL_IS_REGISTER.code,
                    "msg":CodeEnum.USERNAME_OR_EMAIL_IS_REGISTER.msg}
            return data
        try:
            user_info.password = Jwt_tool.get_password_hash(user_info.password)
        except:
            raise resp_502(data={})
        await User.create_user(db, user_info)
        return {"username": user_info.username,
                "code":CodeEnum.PARTNER_CODE_OK.code,
                "msg":CodeEnum.PARTNER_CODE_OK.msg}
    

    @staticmethod
    async def list(db: Session, params: UserQuery, page: int, size: int):
        """获取用户列表"""
        query = await User.get_user_list(db, params)
        total = query.count()
        items = query.offset((page - 1) * size).limit(size).all()
        res = []
        if len(items) > 0:
            for item in items:
                userdata = User(id=item.id, username=item.username, nickname=item.nickname,
                                    email=item.email, roles=item.roles, status=item.status, remarks=item.remarks
                                    , creation_date=item.creation_date, updation_date=item.updation_date)
                res.append(jsonable_encoder(userdata))
        # 使用 paginate 函数进行分页查询
        items_page = Page(total=total, page=page, size=size, items=res)

        # 返回带有分页信息的结果
        return items_page
        
    

if __name__ == '__main__':
    a = {"id": "1", "name":"czd", "czd": None, "s": None}
    query = {key:value for key, value in a.items() if value is not None}
    print(**query)