#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
什么是装饰器？

装饰器（decorator）是 Python 的一个语法糖，它允许你动态地修改函数或类的行为。
你可以把装饰器想象成给函数或类穿上了一件外衣，这件外衣会给这个函数或类增加一些新的功能，但是不会改变它原来的功能。

装饰器有什么用？

装饰器在 Python 中有很多用途，比如：

日志记录: 记录函数的调用信息，参数和返回值。
性能测试: 测量函数的执行时间。
权限校验: 在函数执行前检查是否有相应的权限。
缓存: 缓存函数的返回值，避免重复计算。
事务处理: 在数据库操作中，保证数据的一致性。


'''

#################################################
# 装饰器怎么用？
# 装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数。
#################################################

import functools

def decorator(func):
    def wrapper(*args, **kwargs):
        # 在函数执行前做一些事情
        print("函数开始执行")
        result = func(*args, **kwargs)
        # 在函数执行后做一些事情
        print("函数执行结束")
        return result
    return wrapper

# 使用装饰器时，只需要在要装饰的函数前面加上 @ 符号和装饰器名即可：
@decorator
def my_function():
    print("这是我的函数")

# my_function()


#################################################
# 记录一个函数的执行时间
#################################################
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time} 秒")
        return result
    return wrapper

@timer
def my_function2():
    # 模拟耗时操作
    time.sleep(2)
    print("函数执行完成")

my_function2()


#################################################
# 系统缓存装饰器
#################################################
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)

#################################################
# 自定义缓存装饰器
#################################################
from functools import wraps
import time

def cache(timeout=60):
    cache_dict = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            key = (args, tuple(kwargs.items()))
            if key in cache_dict and cache_dict[key][1] + timeout > now:
                return cache_dict[key][0]
            else:
                result = func(*args, **kwargs)
                cache_dict[key] = (result, now)
                return result
        return wrapper
    return decorator

import requests

@cache(timeout=60)
def fetch_data(query):
    response = requests.get(f"http://data_provider/query?q={query}")
    return response.json()

# Gateway 中处理请求的代码
def handle_request(request):
    query = request.args.get('query')
    data = fetch_data(query)
    return data

'''
工作原理
当 Gateway 收到一个请求时，会调用 handle_request 函数。
handle_request 函数会调用 fetch_data 函数获取数据。
fetch_data 函数首先检查缓存中是否有对应的结果，如果有且未过期，则直接返回缓存数据。
如果缓存中没有数据或数据已过期，则调用 requests.get 向 data_provider 发送请求，获取最新数据，并将结果存入缓存。
'''