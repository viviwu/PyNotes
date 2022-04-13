#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

array = [x*2 for x in range(10)]
print(array)

print(list(map(lambda x:x*x, array)))


dates = ["2019-5-1", "2021-4-12"]
from datetime import datetime
fn = lambda ds:datetime.strptime(ds, '%Y-%m-%d')
print(list(map(fn, dates)))