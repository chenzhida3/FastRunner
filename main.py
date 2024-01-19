'''
Author: chenzhida
Date: 2024-01-09 21:35:20
FilePath: \FastRunner\main.py
Description: 文件程序主入口
Copyright (c) 2024 by chenzhdia3@163.com, All Rights Reserved. 
'''
import uvicorn
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from autotest.init.logger_init import init_logger, logger
from functools import lru_cache
from config import Configs
from typing_extensions import Annotated
import os

from autotest.services.system.user import UserService
from autotest.schemas.system.user import UserIn
from autotest.models.system_models import User
from autotest.db.get_db import get_db
from sqlalchemy.orm import Session

@lru_cache
def get_settings():
    return Configs()


async def startup():
    init_logger()
    logger.info("日志初始化成功")

async def shutdown():
    print('结束')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # yield之前 相当于 startup
    await startup()

    yield

    # yield之前 相当于 shutdown
    await shutdown()


app = FastAPI(title='FastRunner', lifespan=lifespan)


@app.get("/info")
async def info(settings: Annotated[Configs, Depends(get_settings)]):
    return {
        "app_name": settings.LOGGER_DIR,
        "admin_email": settings.MYSQL_DATABASE_HOST,
        
    }

@app.post("/create")
async def create_user(user_info: UserIn, db: Session = Depends(get_db)):
    user_info = await UserService.user_register(db, user_info)
    print(user_info)

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8201, reload=True)