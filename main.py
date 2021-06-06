import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    
    #cv2.imshow("Webcam", frame)

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Webcam", gray)

    #canny = cv2.Canny(frame, 25,175)
    #cv2.imshow("Webcam",canny)

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    u_green = np.array([80,255,255])
    l_green = np.array([65,60,60])
    u_blue = np.array([130,255,255])
    l_blue = np.array([110,50,20])
    mask = cv2.inRange(hsv, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    ret,thrshed = cv2.threshold(cv2.cvtColor(res,cv2.COLOR_BGR2GRAY),3,255,cv2.THRESH_BINARY)
    contours,hier = cv2.findContours(thrshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.imshow('mask', mask)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area >500:
            cv2.drawContours(frame, cnt, -1, (255, 255, 255), 3)

    mask = cv2.inRange(hsv, l_blue, u_blue)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    ret,thrshed = cv2.threshold(cv2.cvtColor(res,cv2.COLOR_BGR2GRAY),3,255,cv2.THRESH_BINARY)
    contours,hier = cv2.findContours(thrshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area >10:
            cv2.drawContours(frame, cnt, -1, (0, 0, 255), 3)

    cv2.imshow('frame',frame)
    

    if cv2.waitKey(1) & 0xFF == 27: # use ESC to quit
        break

cap.release()
cv2.destroyAllWindows()


#capturas :90 graus, camera angulo aleatorio, duas cameras
#sombras, chave ou duas cameras para ver contato
#segmentação
#
#
#
#
#