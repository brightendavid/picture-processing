import cv2 as cv
import numpy as np

def big(img):
    img2 = img[150:250, 220:320, :]
    return img2


def huakuang(img):
    cv.rectangle(img, (220, 150), (320, 250), (200, 0, 200), 2)
    return img

def conver_color(img):
    img = np.where(img>(100,200,200),(0,0,255),img)
    return img

def conver_color_blue(img):
    img = np.where(img>(100,200,200),(255,0,0),img)
    return img

if __name__ == '__main__':
    img1 = cv.imread(r"C:\Users\brighten\Desktop\11\1.png")
    img1 = big(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22\1.png", img1)
    img1 = cv.imread(r"C:\Users\brighten\Desktop\11\2.png")
    img1 = big(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/2.png", img1)

    img1 = cv.imread(r"C:\Users\brighten\Desktop\22\6.png")
    img1 = big(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/3.png", img1)

    img1 = cv.imread(r"C:\Users\brighten\Desktop\11\1.png")
    img1 = huakuang(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/4.png", img1)

    img1 = cv.imread(r"C:\Users\brighten\Desktop\11\2.png")
    img1 = huakuang(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/5.png", img1)

    img1 = cv.imread(r"C:\Users\brighten\Desktop\11\3.png")
    img1 = conver_color(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/6.png", img1)


    img1 = cv.imread(r"C:\Users\brighten\Desktop\22\6.png")
    img1 = huakuang(img1)
    cv.imwrite(r"C:\Users\brighten\Desktop\22/7.png", img1)

