import cv2 as cv


# Image Resize
def rescaleFrame(img, scale=0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('E:/Photos/100CANON/m/1.jpg')

img_resized = rescaleFrame(img)

cv.imshow('1', img)
cv.imshow('image Resized', img_resized)

# Converting to grayscale
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img_resized, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img_resized, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the Image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# resized
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
crop = img_resized[50:200, 200:400]
cv.imshow('Crop', crop)

cv.waitKey(0)
