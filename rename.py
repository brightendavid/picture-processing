#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 此代码的功能   要求很高，慎用！！！
# 将一个文件夹内的所有文件名替换为对应位置的另一个文件夹中的文件名

import os.path

rootdir = r"C:\Users\brighten\Desktop\HLED"

rootdirs = r"E:\pythonProject\repeat methord\picture_pro\fenge"
files = os.listdir(rootdir)
files_mubiao = os.listdir(rootdirs)
print("names__________")
print(files)
print(files_mubiao)
if "ini" in files_mubiao[0]:
    files_mubiao = files_mubiao[1:]
# print(files)
b = 0
for i in range(len(files)):
    name = files[i]
    print("原名", end=" ")
    print(name)
    print("目标:", end=" ")
    print(files_mubiao[i])
    a = os.path.splitext(files[i])
    print("a:", end=" ")
    print(a)

    newname = files_mubiao[i]
    os.rename(rootdir + "/" + name, rootdir + "/" + newname)
