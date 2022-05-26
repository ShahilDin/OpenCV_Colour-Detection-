import cv2
import numpy as np
import matplotlib.pyplot as plt
from blue_detect import detect_blue
from red_detect import detect_red
from green_detect import detect_green

#Loading image
img= cv2.imread("damien_hirst_dot.jpg")
img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #converting to HSV colour space
img_copy=img.copy()

def show_result(hsv,img):

    green_result=detect_green(hsv,img)
    green_result= cv2.cvtColor(green_result, cv2.COLOR_BGR2RGB)
    plt.imshow(green_result)
    plt.show()

    blue_result = detect_blue(hsv, img)
    blue_result = cv2.cvtColor(blue_result, cv2.COLOR_BGR2RGB)
    plt.imshow(blue_result)
    plt.show()

    red_result = detect_red(hsv, img)
    red_result = cv2.cvtColor(red_result, cv2.COLOR_BGR2RGB)
    plt.imshow(red_result)
    plt.show()


show_result(img_hsv,img_copy)
