import numpy as np
import cv2 as cv
import time


def access_pixel(image):
    print(image.shape)
    height =image.shape[0]
    width =image.shape[1]
    channels =image.shape[2]
    print('height:',height,'width',width,'channels:',channels)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv =image[row,col,c]
                image[row,col,c] =255-pv
    cv.imshow('image_p',image)


def create_color_image():
    """彩色图，3通道"""
    img1 =np.zeros([400,400,3],dtype=np.uint8)#创建三通道的图片 blue green red初始化为0
    img1[:,:,0] =255#第一个通道全部变为255,(0,0,255)，此时img1为蓝色
    #img1[:,:,0]前面不写表示全部的
    print('height1:'+str(img1.shape))#其中shape为元祖(400,400,3)
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            for k in range(img1.shape[2]):
               img1[i,j,k] =(i+j+k)%255
    cv.imshow('new_img1',img1)


def create_gray_image():
    """彩色图，1通道"""
    img2 =np.zeros([1000,1000,3],dtype=np.uint8)
    print('img2:'+str(img2.shape))#显示黑色图片
    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for k in range(img2.shape[2]):
                img2[i,j,k]=(i+j+k)%255
    cv.imshow('new_img2',img2)


create_color_image()
create_gray_image()
src =cv.imread('E:/demo/images/cat.jpg')
cv.imshow('cat',src)
t1 =time.time()
access_pixel(src)
t2 =time.time()
print('time:',t2-t1)
cv.waitKey(0)
cv.destroyAllWindows()

