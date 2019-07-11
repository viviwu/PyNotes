#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

def re_match(str):
    print(re.match('www', str).span())  # 在起始位置匹配
    print(re.match('com', str))         # 不在起始位置匹配
    return;

re_match('www.vivi.com')

line = "Cats are smarter than dogs"
def re_match_group(string):
    matchObj = re.match( r'(.*) are (.*?) .*', string, re.M|re.I)

    if matchObj:
        print "matchObj.group() : ", matchObj.group()
        print "matchObj.group(1) : ", matchObj.group(1)
        print "matchObj.group(2) : ", matchObj.group(2)
    else:
        print "No match!!"
    return;
re_match_group(line)
