import cv2
import glob
import os

inputFolder = r'//your directory
os.mkdir('p')

i=0

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    imgResized = cv2.resize(image, (640, 480))
    cv2.imwrite("p/image%04i.jpg" %i, imgResized)

    i +=1
    cv2.imshow('image', imgResized)
    cv2.waitKey(30)

cv2.destroyAllWindows()
