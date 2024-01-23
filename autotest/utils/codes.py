#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   codes.py
@Time    :   2024/01/22 17:26:29
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   响应状态码及msg
'''

from enum import Enum

class CodeEnum(Enum):

    @property
    def code(self):
        "获取状态码"
        return self.value[0]
    
    @property
    def msg(self):
        "获取消息"
        return self.value[1]
    

    # 业务状态码
    PARTNER_CODE_OK = (1000, "OK")
    PARTNER_CODE_FAIL = (-1, "操作失败")

    # 账号体系相关  1001~1100
    USERNAME_OR_EMAIL_IS_REGISTER = (1001, "用户名已被注册")


