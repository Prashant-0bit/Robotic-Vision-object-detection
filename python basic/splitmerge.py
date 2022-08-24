import cv2 as cv
import numpy as np

img = cv.imread('E:/Photos/100CANON/m/1.jpg')
cv.imshow('1', img)

# resized image
resize = cv.resize(img, (700, 700), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

blank = np.zeros(resize.shape[:2], dtype='uint8')


b, g, r = cv.split(resize)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


print(resize.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
