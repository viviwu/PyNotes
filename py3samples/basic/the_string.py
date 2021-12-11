#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

dt_str = '2020-01-02 00:00:00'
print(dt_str.replace('-',''))
print(dt_str.strip('2'))
print(dt_str.split('0'))

s1 = "i am %s, i am %d years old" % ('jeck',26)    #按位置顺序依次输出
s2 = "i am %(name)s, i am %(age)d years old" % {'name':'jeck','age':26}   #自定义key输出
s3 = "i am %(name)+10s, i am %(age)d years old, i am %(height).2f" % {'name':'jeck','age':26,'height':1.7512}  #定义名字宽度为10,并右对齐.定义身高为浮点类型,保留小数点2位
s4 = "原数: %d, 八进制:%o , 十六进制:%x" % (15,15,15)      #八进制\十六进制转换
s5 = "原数:%d, 科学计数法e:%e, 科学计数法E:%E" %(1000000000,1000000000,1000000000)    #科学计数法表示
s6 = "百分比显示:%.2f %%"  % 0.75     #百分号表示
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)