import cv2
import numpy as np


def detect_red(hsv,frame):
    
    ## Follows the same step as detecting the color blue just with a different  value 
    r_low=np.array([0,120,70])
    r_high=np.array([20,255,255])
    r_mask= cv2.inRange(hsv,r_low,r_high)
    

    detect_red=cv2.bitwise_and(frame,frame,mask=r_mask)
        
    
    _,contour,hierarcy= cv2.findContours(r_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
    for i, contour in enumerate(contour):
       
        if cv2.contourArea(contour) > 500:
            x,y,w,h= cv2.boundingRect(contour) #highlight the ROI after obtaining contours from an image.
            red_rect=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1) #drawing the rectangle from the obtained ROI
            cv2.putText(frame,"Red Object",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1,cv2.LINE_AA)
    
    return frame
