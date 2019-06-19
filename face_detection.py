#The following program is used to detect faces in webcam feed. For image face detecting comment out the while loop and uncomment the commented code.

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('nasa_small.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,150,0), 2)

#Resizing image
img = cv2.resize(img, (1400,700))
cv2.imshow('NASA', img)
cv2.waitKey(0)


cv2.destroyAllWindows()