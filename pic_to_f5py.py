## -*- coding: utf-8 -*-
import cv2
import numpy as np
import h5py
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow.python.client import device_lib  # gpu cpu information
from datetime import datetime
import time
import os

# 从图片到f5py
# 再回来会偏色
tf.reset_default_graph()  # Use this to clear the defualt graph and nodes
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
log_device_placement = True

img1 = []
# dir='D:\\download\\dataset\\Bernard0\\Computer_Vision\\spliced_copymove_NIST\\rgb_imgs'
dir = r'./fenge'

# img1=np.zeros()
for filename in os.listdir(dir):
    img1.append(dir + '/' + filename)
print(img1)

with tf.device('/gpu:0'):
    # # num=13470

    imagedata_shape = (len(img1), 256, 256, 3)
    maskdata_shape = (len(img1), 256, 256)
    f = h5py.File('spliced_NIST.hdf5', mode='w')
    f.create_dataset("test_img", imagedata_shape, np.int8)

    start_time = time.time()

    for i in range(len(img1)):

        print(img1[i])
        if i % 1000 == 0 and i > 1:
            print('image_data: {}/{}'.format(i, len(img1)))
        img = cv2.imread(img1[i])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width = img.shape[:2]
        # size = (int(width * 0.25), int(height * 0.25))
        # img = cv2.resize(img, size)
        # # imgData[i]=img

        f['test_img'][i] = img  # write data under the primary key data of the file

    f.close()  # Close the file
    duration = time.time() - start_time
    print(duration)
