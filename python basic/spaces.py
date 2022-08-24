import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('E:/Photos/100CANON/m/1.jpg')
cv.imshow('1', img)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

plt.imshow(resized)
plt.show()

# BGR tp Grayscale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to l*a*b
lab = cv.cvtColor(resized, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV2BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)
