
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   local.py
@Time    :   2024/01/11 11:15:23
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   获取全局(可以获取请求头header那种)
'''
from contextvars import ContextVar
import typing


class Local:
    __slots__ = ("_storage",)

    def __init__(self) -> None:
        object.__setattr__(self, '_storage', ContextVar("local_storage"))
    
    def __iter__(self) -> typing.Iterator[typing.Tuple[int, typing.Any]]:
        return iter(self._storage.get({}).items())
    
    def __getattr__(self, name: str) -> typing.Any:
        values = self._storage.get({})
        try:
            return values[name]
        except KeyError:
            return None

    def __setattr__(self, name: str, value: typing.Any) -> None:
        values = self._storage.get({}).copy()
        values[name] = value
        self._storage.set(values)

    def __delattr__(self, name: str) -> None:
        values = self._storage.get({}).copy()
        try:
            del values[name]
            self._storage.set(values)
        except KeyError:
            ...

g = Local()

       