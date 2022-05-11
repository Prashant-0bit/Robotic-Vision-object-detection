import cv2
import numpy as np
import math
def nothing(x):
    pass

while True:
    frame = cv2.imread("C:/Users/Besitzer/Downloads/test3.jpg")

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_r = np.array([0, 70, 50])
    u_r = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, l_r, u_r)

    l_r = np.array([170, 70, 50])
    u_r = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, l_r, u_r)


    mask = mask1 + mask2
    res = cv2.bitwise_and(frame, frame, mask=mask)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    red_button = (0, 0)
    led_light = (0, 0)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 300 and area < 1390:
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            red_button = (int(x), int(y))
            #radius = int(radius)
            #cv2.circle(frame, red_button, radius, (0, 255, 0), 2)

        elif area > 100 and area <600  :
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            led_light= (int(x), int(y))
            #radius = int(radius)
            #cv2.circle(frame, led_light, radius, (0, 255, 0), 2)

        #print('area is ...', area)
    cv2.line(frame,  red_button, led_light, (0, 255, 0), 1)


    #def get_angle(red_button, led_light):  # These can also be four parameters instead of two arrays
    deltaY = red_button[1] - led_light[1]
    deltaX = red_button[0] - led_light[0]
    print('deltaX', deltaX)
    print('deltaY', deltaY)
    print('red button', red_button)
    print('led light', led_light)

    angleInDegrees = math.atan2(deltaY, deltaX) * 180 / math.pi
    rotationAngle = int(math.trunc(-1 * ((angleInDegrees -20) - 90)))

        #return (led_light, rotationAngle)
    print('angle is..', angleInDegrees)
    print('rotation angle', rotationAngle)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(0)
    if key == 1:
        break

cv2.destroyAllWindows()