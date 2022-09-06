import cv2
import numpy as np


framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, framewidth)
cap.set(4, frameheight)

def empty(a):
    pass


cv2.namedWindow("HSV_EDIT")
cv2.resizeWindow("HSV_EDIT", 640, 250)
cv2.createTrackbar("HUE MIN", "HSV_EDIT", 0,179,empty)
cv2.createTrackbar("HUE MAX", "HSV_EDIT", 179,179,empty)
cv2.createTrackbar("SAT MIN", "HSV_EDIT", 0,255,empty)
cv2.createTrackbar("SAT MAX", "HSV_EDIT", 255,255,empty)
cv2.createTrackbar("VAL MIN", "HSV_EDIT", 0,255,empty)
cv2.createTrackbar("VAL MAX", "HSV_EDIT", 255,255,empty)


while True:
    
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("HUE MIN", "HSV_EDIT")
    h_max = cv2.getTrackbarPos("HUE MAX", "HSV_EDIT")
    v_min = cv2.getTrackbarPos("VAL MIN", "HSV_EDIT")
    v_max = cv2.getTrackbarPos("VAL MAX", "HSV_EDIT")
    s_min = cv2.getTrackbarPos("SAT MIN", "HSV_EDIT")
    s_max = cv2.getTrackbarPos("SAT MAX", "HSV_EDIT")
    print(v_min)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img,img, mask = mask)
    
    cv2.imshow("IMAGE", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("MASK", mask)
    cv2.imshow("RESULT", result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Q was pressed")
        break

cap.release()
cv2.destroyAllWindows()