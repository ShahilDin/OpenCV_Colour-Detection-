import cv2
import numpy as np


def detect_green(hsv,frame):
    
    #Same Steps as getting the blue and red
    g_low = np.array([40,40,40])
    g_high = np.array([70,255,255])
    g_mask = cv2.inRange(hsv,g_low,g_high)
    
    detect_green= cv2.bitwise_and(frame,frame,mask=g_mask)
    
    _,contour,hierarcy = cv2.findContours(g_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for i,contour in enumerate(contour):
        
        if cv2.contourArea(contour) > 500:
            x,y,w,h=cv2.boundingRect(contour)
            green_rect=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
            
            cv2.putText(frame,"Green Object",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
    
    return frame
