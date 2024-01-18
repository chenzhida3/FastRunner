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
    

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8201, reload=True)