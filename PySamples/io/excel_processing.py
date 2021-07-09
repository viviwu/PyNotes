#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: viviwu
@email: vivi705@icloud.com
@file: excel_processing.py
@time: 2021/1/9 9:46 下午
@desc: Copyright © viviwu All rights reserved.

"""
from pathlib import Path
import pandas as pd
import os

orgi_home = '../../../express_orders/'
dest_home = '../../../new_express_orders/'

def resolve_data(price):
    np = price
    if price<0:
        np = 0
    return np

def resolve_xls(f_name):
    df = pd.read_excel(orgi_home+f_name, sheet_name='T2Data1')
    df['快件价格'] = [resolve_data(x) for x in df.快件价格.to_list()]
    df.to_excel(dest_home+f_name, encoding='utf-8', index=True, header=True)
    # writer = pd.ExcelWriter(self.filename)
    # open_data.T.to_excel(writer, 'T2Data1')

def list_file_in_path(dir):
    fls = []
    try:
        ls = os.listdir(dir)
    except :
        print("Access Deny.")
    else:
        for fn in ls:
            if fn.endswith(".xls"):
                # fpath = os.path.join(dir, fn)
                # fls.append(fpath)
                fls.append(fn)
                # if os.path.isdir(fpath):
            else:
                print("Other files:", fn)
    return fls



fls = list_file_in_path(orgi_home)
print(fls)
for f_name in fls:
    resolve_xls(f_name)
    print(f_name, " done!")


