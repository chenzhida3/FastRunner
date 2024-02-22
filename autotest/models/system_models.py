#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   system_models.py
@Time    :   2024/01/19 11:40:24
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   系统类的数据库模型
'''
import sys
import os
GRANDFA = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(GRANDFA)

from sqlalchemy import Column, String, Text, JSON, Integer, and_, select
from sqlalchemy.orm import Session
from autotest.db.get_db import Base, engine
from autotest.models.baseTable import BaseTable
from autotest.schemas.system.user import UserIn, UserQuery

from fastapi.encoders import jsonable_encoder
from fastapi_pagination.ext.sqlalchemy import paginate




class User(BaseTable,Base):
    """用户表"""
    __tablename__ = 'user'
    id = Column(Integer(), nullable=False, primary_key=True, autoincrement=True, comment='主键')
    username = Column(String(64), nullable=False, comment='用户名', index=True)
    password = Column(Text, nullable=False, comment='密码')
    email = Column(String(64), comment='邮箱')
    roles = Column(JSON, comment='用户类型')
    status = Column(Integer, comment='用户状态  1 锁定， 0 正常', default=0)
    nickname = Column(String(255), comment='用户昵称')
    user_type = Column(Integer, comment='用户类型 10 管理人员, 20 测试人员', default=20)
    remarks = Column(String(255), comment='用户描述')
    avatar = Column(Text, comment='头像')
    tags = Column(JSON, comment='标签')

    @classmethod
    async def get_user_by_name(cls, db: Session, username: str):
        """根据用户名称查询数据库

        Args:
            db (Session): 数据库连接
            username (str): 用户名
        """
        return db.query(User).filter(User.username == username, User.enabled_flag == 1).first()
    
    @classmethod
    async def create_user(cls, db: Session, user_info: UserIn): 
        """创建用户     

        Args:
            db (Session): 数据库谅解
            user_info (UserIn): 请求体内容
        """
        data = user_info.model_dump()
        db_user = User(**data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    
    @classmethod
    async def get_user_list(cls, db: Session, params: UserQuery):
        """获取查询语句

        Args:
            db (Session): 数据库连接
            params (UserQuery): 请求参数

        Returns:
            _type_: 请求语句
        """
        q = [User.enabled_flag == 1]
        if params.username:
            q.append(User.username.like('%{}%'.format(params.username)))
        if params.nickname:
            q.append(User.nickname.like('%{}%'.format(params.nickname)))
        if params.id:
            q.append(User.id == params.id)
        query = db.query(User).filter(and_(*q)).order_by(User.id.desc())
        return query
    


        


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    

