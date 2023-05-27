
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
top_size,bottom_size,left_size,right_size=(50,50,50,50)

img=cv.imread('./Tp_D_CND_M_N_ani00018_sec00096_00138.tif')
print(img.shape)
constant=cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv.BORDER_CONSTANT,value=(0,255,0))
cv.imshow("1",constant)
cv.waitKey(0)