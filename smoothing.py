import cv2 as cv
# import numpy as np

img = cv.imread('E:/Photos/wallpaper/3.jpg')
cv.imshow('3', img)

# resized image
resize = cv.resize(img, (1000, 700), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

# Averaging
average = cv.blur(resize, (3, 3))
cv.imshow('Average', average)

# Gaussian blur
gaussian = cv.GaussianBlur(resize, (3, 3), 0)
cv.imshow('>Gaussian', gaussian)

# median blur
median = cv.medianBlur(resize, 3)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(resize, 15, 35, 35)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
