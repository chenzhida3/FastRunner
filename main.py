'''
Author: chenzhida
Date: 2024-01-09 21:35:20
FilePath: \FastRunner\main.py
Description: 文件程序主入口
Copyright (c) 2024 by chenzhdia3@163.com, All Rights Reserved. 
'''
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from autotest.init.logger_init import init_logger, logger

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
    

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8201, reload=True)