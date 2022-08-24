import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank )

#1. Point the certain colors
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

#2. Draw rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('rectangle', blank)

#3. Draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle', blank)

#4. Draw line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

#5. write text
cv.putText(blank, 'Hello, my name is peter', (10,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)