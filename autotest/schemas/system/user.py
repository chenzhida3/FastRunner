#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2024/01/19 15:38:01
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   接口请求时，请求体的模型校验
'''
from typing import List, Optional
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    """用户注册请求体模型

    Args:
        BaseModel (基类): 
    """
    username: str 
    nickname: str 
    password: str
    email: Optional[str] = None
    user_type: Optional[str] = None
    remarks: Optional[str] = None
    avatar: Optional[str] = None
    tags: Optional[List] = None
    roles: Optional[List] = None

class UserQuery(BaseModel):
    """用户查询请求模型

    Args:
        BaseModel (_type_): _description_
    """
    id: int = Field(None, description="用户id")
    username: str = Field(None, description="用户名")
    nickname: str = Field(None, description="昵称")