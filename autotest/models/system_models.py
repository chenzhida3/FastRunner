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

from sqlalchemy import Column, String, Text, JSON, Integer, and_
from sqlalchemy.orm import Session
from autotest.db.get_db import Base, engine
from autotest.models.baseTable import BaseTable
from autotest.schemas.system.user import UserIn, UserQuery

from fastapi.encoders import jsonable_encoder




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
        data = db.query(User).filter(User.enabled_flag==1).all()
        # 看请求体是否带以下参数，如果有则取满足所有条件的数据
        if params.id:
            data = db.query(User).filter(and_(User.id==params.id,
                                            User.enabled_flag==1)).all()
        if params.username:
            data = db.query(User).filter(User.username.like(f"%{params.username}%"),
                                            User.enabled_flag==1).all()
        if params.nickname:
            data = db.query(User).filter(User.nickname.like(params.nickname),
                                            User.enabled_flag==1).all()
        if params.id and params.username:
            data = db.query(User).filter(User.id==params.id, User.username.like(params.username), 
                                        User.enabled_flag==1).all()
        if params.id and params.nickname:
            data = db.query(User).filter(User.id==params.id, User.nickname.like(params.nickname), 
                                            User.enabled_flag==1).all()
        if params.username and params.nickname:
            data = db.query(User).filter(User.username.like(params.username), 
                                        User.nickname.like(params.nickname),User.enabled_flag==1).all()
        
        if params.id and params.username and params.nickname:
            data = db.query(User).filter(User.id==params.id, User.username.like(params.username), 
                                        User.nickname.like(params.nickname),User.enabled_flag==1).all()
        
        res = []
        if len(data) > 0:
            for item in data:
                userdata = User(id=item.id, username=item.username, nickname=item.nickname,
                                    email=item.email, roles=item.roles, status=item.status, remarks=item.remarks
                                    , creation_date=item.creation_date, updation_date=item.updation_date)
                res.append(jsonable_encoder(userdata))
        return res

        


        


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    

