import PIL.Image as Image
import os
import cv2
import numpy as np

base_path = '.'  # 原图地址
fenge_path = './fenge'  # 分割后的地址
hebing_path = './hebing'  # 合并后的地址
IMAGE_SIZE = 256  # 每张小图片的大小


def image_compose2(file_name):
    img_path = os.path.join(base_path, file_name)
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)
    height, width, depth = img.shape
    height_cut = height // 256
    width_cut = width // 256
    new_image = Image.new('RGB', (width_cut * IMAGE_SIZE, height_cut * IMAGE_SIZE))
    for j in range(height_cut):
        for i in range(width_cut):
            temp_images = Image.open(os.path.join(fenge_path, file_name[:-4] + '_{}{}'.format(j, i) + '.jpg'))
            new_image.paste(temp_images, (i * IMAGE_SIZE, j * IMAGE_SIZE))
    return new_image.save(os.path.join(hebing_path, file_name))


for file_name in os.listdir(base_path):
    image_compose2(file_name)  # 调用函数
