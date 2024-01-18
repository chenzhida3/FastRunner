#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   get_db.py
@Time    :   2024/01/18 11:01:12
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   获取数据库链接
'''
import sys
import os
GRANDFA = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(GRANDFA)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  config import config
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://"+config.MYSQL_DATABASE_USERNAME+":"+config.MYSQL_DATABASE_PASSWORD+"@"+str(config.MYSQL_DATABASE_HOST)+":"+str(config.MYSQL_DATABASE_PORT)+"/"+config.MYSQL_DATABASE_DB

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

