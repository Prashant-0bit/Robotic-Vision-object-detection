import cv2
img = cv2.imread("E:/Photos/100CANON/m/1.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)