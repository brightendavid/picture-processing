#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import sys

import cv2
import numpy as np
import math
import traceback
from PIL import Image
import os.path


def BiLinear_interpolation(img, dstH, dstW):
    scrH, scrW, _ = img.shape
    img = np.pad(img, ((0, 1), (0, 1), (0, 0)), 'constant')
    retimg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx = (i + 1) * (scrH / dstH) - 1
            scry = (j + 1) * (scrW / dstW) - 1
            x = math.floor(scrx)
            y = math.floor(scry)
            u = scrx - x
            v = scry - y
            retimg[i, j] = (1 - u) * (1 - v) * img[x, y] + u * (1 - v) * img[x + 1, y] + (1 - u) * v * img[
                x, y + 1] + u * v * img[x + 1, y + 1]
    return retimg


def find_src_shape(gt_dir, name):
    """
        using pred name to find src and gt
        return:src_path, gt_path
        输出的名字：output_Sp_Default_34_445004_zebra -->
        输入名字，找出文件src的大小
        """

    gt_path = gt_dir + "/" + name
    if os.path.exists(gt_path):
        src = Image.open(gt_path)
        print(src.size)
        return src.size
    else:
        print(gt_path, ':not exists')
        traceback.print_exc()
        sys.exit()


if __name__ == "__main__":
    src_dir=r"C:\Users\brighten\Desktop\cat"
    save_dir=r"C:\Users\brighten\Desktop\cat1"
    jizhun_dir=r"F:\DATA\public_dataset\Columbia\src"
    files = os.listdir(src_dir)
    for name in files:
        tif_name=name.replace("bmp","tif") # 如果是后缀不同
        src_size = find_src_shape(jizhun_dir, tif_name)
        print(src_size)
        src=Image.open(src_dir+"/"+name).convert("RGB")
        src=np.array(src)

        src_re=BiLinear_interpolation(src,src_size[1],src_size[0])
        result = Image.fromarray(src_re.astype(np.uint8))
        result.save(save_dir+"/"+name)