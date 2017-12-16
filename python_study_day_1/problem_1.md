#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-13 19:43:15
# @Author  : longfellow (longfellow.wang@gmail.com)
# @Link    : https://github.com/wadasworths
# @Version : 装饰器（decorator）

# 装饰器实现单例模式
from functools import wraps


def singleton(cls):
	instance = {}
	@wraps(cls)
	def getinstance(*args, **kw):
		