#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   baseTable.py
@Time    :   2024/01/18 10:41:59
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   基础模型表
'''
import sys
import os
GRANDFA = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(GRANDFA)
from sqlalchemy import Column, BigInteger, Boolean, String, DateTime, func


class BaseTable:
    '''基本表'''
    creation_date = Column(DateTime(), default=func.now(), comment='创建时间')
    created_by = Column(BigInteger, comment='创建人ID')
    updation_date = Column(DateTime(), default=func.now(), onupdate=func.now(), comment='更新时间')
    updated_by = Column(BigInteger, comment='更新人ID')
    enabled_flag = Column(Boolean(), default=1, nullable=False, comment='是否删除, 0 删除 1 非删除')

