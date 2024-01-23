#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   jwtTool.py
@Time    :   2024/01/22 17:45:27
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   密码加密解密
'''

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["md5_crypt"])

class Jwt_tool:

    @staticmethod
    def get_password_hash(password):
        """密码字符串哈希

        Args:
            password (str): 密码字符串
        """
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(str_pwd, hash_pwd):
        """验证密码是否正确

        Args:
            str_pwd (str): 明文密码
            hash_pwd (str): md5密码
        """
        return pwd_context.verify(str_pwd, hash_pwd)



if __name__ == '__main__':
    b= "$1$kuPaMTUW$Gh089iURrz/Avom0LaE8E1"
    a = Jwt_tool.verify_password("123456", b)
    print(a)