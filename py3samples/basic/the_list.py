#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)

json = [{'A':{'A':1, 'a':2}}, {'B':{'B':1, 'b':2}}]
print(json)
for dic in json:
    print(type(dic.keys()), list(dic.keys())[0])
    print(type(dic.values()), list(dic.values())[0])