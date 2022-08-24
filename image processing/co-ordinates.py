import cv2
import numpy as np

image = cv2.imread(r'C:\Users\Besitzer\PycharmProjects\pythonProject\image\main.jpg')


def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(X_Location) + ', ' + str(Y_Location)
        cv2.putText(image, strXY, (x, y), font, 0.5, (0, 0, 255), 1)
        print(strXY)
        cv2.imshow('image', image)


#image = cv2.resize(image, (640, 480))
gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cm_to_pixel = 39/1280

Difference = np.absolute(np.matrix(np.int16(gray_image1)))
Difference[Difference > 300] = 300
Difference = np.uint8(Difference)

BW = Difference
BW[BW <= 100] = 0
BW[BW > 100] = 1

column_sums = np.matrix(np.sum(BW, 0))
column_numbers = np.matrix(np.arange(720))
column_multi = np.dot(column_sums, column_numbers)
total = np.sum(column_multi)
total_total = np.sum(np.sum(BW))
column_location = total/total_total

X_Location = column_location*cm_to_pixel

row_sums = np.matrix(np.sum(BW, 1))
row_sums = row_sums.transpose()
row_numbers = np.matrix(np.arange(721))
row_multi = np.multiply(row_sums, row_numbers)
total = np.sum(row_multi)
total_total = np.sum(np.sum(BW))
row_location = total / total_total

Y_Location = row_location*cm_to_pixel

print(X_Location, Y_Location)

cv2.imshow('image', image)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
