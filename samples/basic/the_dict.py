#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

print('1', list(d))
print(d.items())
print(d.keys())
print(d.values())
# if  d.keys().contains("Bob"):
#     print("Bob")
if "Bob" in d.keys():
    print('Bob')

for key in d:
    print(key, d[key])

print(list(d.items())[0])

for key,value in d.items():
    print(key,':',value)

