
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   common.py
@Time    :   2024/01/11 11:37:31
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   一些通用方法
'''
import uuid

def get_str_uuid():
    return str(uuid.uuid4()).replace("-", "")





if __name__ == '__main__':
    get_str_uuid()