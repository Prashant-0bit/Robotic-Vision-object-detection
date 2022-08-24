import cv2 as cv
#img = cv.imread('E:/Photos/100CANON/m/IMG-20180707-WA0011.jpg')
#cv.imshow('IMG-20180707-WA0011', img)
#cv.waitKey(0)

#work for image, video and live video

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#work for live video
#def changeRes(width,height):
#    capture.set(3,width)
#    capture.set(4,height)

capture = cv.VideoCapture('E:/Photos/video/video/VID_20210814_200620.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
