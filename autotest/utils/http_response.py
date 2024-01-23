#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   http_response.py
@Time    :   2024/01/22 15:32:26
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   配置相应状态码模型
'''
from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Union


def resp_200(*, code=1000, data: Union[list, dict, str], message="Success") -> Response:

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={
                            'code': code,
                            'message': message,
                            'data': data
                        })

def resp_502(*, code=502, data: str = None, message="API server error") -> Response:

    return JSONResponse(status_code=status.HTTP_502_BAD_GATEWAY,
                        content={
                            'code': code,
                            'message': message,
                            'data': data
                        })