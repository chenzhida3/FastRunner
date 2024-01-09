'''
Author: chenzhida
Date: 2024-01-09 21:35:20
FilePath: /FastRunner/main.py
Description: 

Copyright (c) 2024 by chenzhdia3@163.com, All Rights Reserved. 
'''

from fastapi import FastAPI
import uvicorn

app = FastAPI(title='FastRunner')

@app.get('/')
async def one():
    return {'msg':'hello word'}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='127.0.0.1', port=8201, reload=True)