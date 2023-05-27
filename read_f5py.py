#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import h5py
import cv2

filename = r"./test_imgs_v2.hdf5"

f = h5py.File(filename, 'r')
data = f['feat'][:]


num = data.shape[0]
img1 = data[0]

for i in range(num):
    img = data[i]
    print(img.shape)
    img = img[:, :, ::-1]
    cv2.imwrite("hebing/"+str(i) + '.png', img)