import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID') #<-- this for python 3.4.0
#fourcc = cv2.cv.CV_FOURCC('X','V','I','D')

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(10) == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
