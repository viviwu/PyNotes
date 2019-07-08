#!/usr/bin/env python
# -*-coding:UTF-8-*-

import os
from subprocess import call

path1 = "/Users/river/Library/Developer/Xcode/DerivedData"
path2 = "/Users/river/Library/Developer/Xcode/Archives"
path3 = "/Users/river/Library/Developer/CoreSimulator/Devices"
path4 = "/Users/river/Library/Developer/XCPGDevices"

paths = [path1, path2, path3, path4]

for path in paths:
    # if path.exists():
    if os.path.exists(path):
        os.chdir(path)
        os.system('pwd')
        os.system('rm -rf *')
        print('文件清理完成')
    else:
        print("路径不存在！")
