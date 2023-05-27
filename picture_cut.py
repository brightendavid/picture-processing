import os
import cv2
import numpy as np
import random
import tqdm
from xml.etree import ElementTree as ET

base_path = r'C:\Users\brighten\Desktop\11'  # 图片地址
for file_name in tqdm.tqdm(os.listdir(base_path)):
    if file_name.endswith('.png'):
        img_path = os.path.join(base_path, file_name)
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
        height, width, depth = img.shape
        height_cut = height
        width_cut = width
        print(height_cut)
        pattern_height = 90
        pattern_width = 90
        for j in range(height_cut):
            for i in range(width_cut):
                left_h = j * pattern_height
                left_w = i * pattern_width
                right_h = left_h + pattern_height
                right_w = left_w + pattern_width
                sub_img = img[left_h: right_h, left_w: right_w]
                cv2.imencode('.jpg', sub_img)[1].tofile(
                    os.path.join('fenge', file_name[:-4] + '_{}{}'.format(j, i) + '.png'))  # 图片保存地址'fe
