import cv2 as cv
from PIL import Image
import os
import numpy as np
def read_img(dir,save_dir):
    # img=cv.imread(dir,0)
    for name in os.listdir(dir):
        print(name)
        img_path=os.path.join(dir,name)
        img=cv.imread(img_path)
        # print(img)
        # cv.imwrite("0.png", img_path)
        img=np.where(img<200,0,255)
        # print(img)
        # cv.imshow("Img",img)
        save_path=os.path.join(save_dir,name)
        cv.imwrite(save_path,img)

if __name__=="__main__":
    dir=r"C:\Users\brighten\Desktop\DATA\public_dataset\casia\gt"
    save_dir=r"C:\Users\brighten\Desktop\data_new\casia"
    read_img(dir,save_dir)
