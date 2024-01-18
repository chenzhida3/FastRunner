#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2024/01/18 10:41:59
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   基础模型表
'''
from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base:
    '''基本表'''

