import cv2 
import numpy as np 
from blue_detect import detect_blue
from red_detect import detect_red
from green_detect import detect_green

cap=cv2.VideoCapture(0)


while True:
    #ret returns a a true boolean if frame is there 
    ret,frame=cap.read()
    if ret:
        #coverting the image from BGR to HSV , opencv uses BGR NOT RGB
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        frame=detect_blue(hsv,frame)
        frame=detect_red(hsv,frame)
        frame=detect_green(hsv,frame)
            
        cv2.imshow("Detect Colors",frame) #showing frame
            
        k=cv2.waitKey(1) & 0xFF
        if k==27: #if esc button is pressed then break out of this 
            break
    else:
        print("Can't Read Video")
        break



cap.release()
cv2.destroyAllWindows()
print("Closing Program")
