import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)

cap.set(3 , 400 )
cap.set(4 , 512 )
cap.set(10, 100 ) 

def empty():
    pass 
cv2.namedWindow("HSV")
cv2.resizeWindow( "HSV" , 400 , 400 )
cv2.createTrackbar("HUE_MIN" , "HSV" , 0 , 179 , empty )
cv2.createTrackbar("SAT_MIN" , "HSV" , 0 , 255  , empty)
cv2.createTrackbar("VALUE_MIN" , "HSV" , 0 , 255 , empty )
cv2.createTrackbar("HUE_MAX" , "HSV" , 179 , 179 , empty)
cv2.createTrackbar("SAT_MAX" , "HSV" , 255 , 255 ,empty)
cv2.createTrackbar("VALUE_MAX" , "HSV" , 255 , 255 , empty)


while True: 
    _ , img = cap.read() 
    img = cv2.resize( img , ( 400 , 400 ))
    hsv_img = cv2.cvtColor( img , cv2.COLOR_BGR2HSV )
    h_min = cv2.getTrackbarPos( "HUE_MIN" , "HSV" )
    h_max = cv2.getTrackbarPos( "HUE_MAX" , "HSV" )
    s_min = cv2.getTrackbarPos( "SAT_MIN" , "HSV" )
    s_max = cv2.getTrackbarPos( "SAT_MAX" , "HSV" )
    v_min = cv2.getTrackbarPos( "VALUE_MIN" , "HSV" )
    v_max = cv2.getTrackbarPos( "VALUE_MAX" , "HSV" )
    lower = np.array([ h_min , s_min , v_min])
    higher = np.array([ h_max , s_max , v_max])
    mask = cv2.inRange(hsv_img , lower , higher)
    
    cv2.imshow( "hsv" , img )
    cv2.imshow( "mask" , mask)
    if cv2.waitKey(1) & 0xff == ord('q') :
        break
    
