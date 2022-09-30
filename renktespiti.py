"""
Bu ödevde arabadaki yeşil renkleri tespit ettim

"""


import cv2
import numpy as np

img = cv2.imread("car.png")


hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

alt = np.array([40,120,0])

üst = np.array([65,280,255])

mask = cv2.inRange(hsv,alt,üst)

mask = cv2.medianBlur(mask,5)

filter = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("image",img)

cv2.imshow("filter",filter)


# cv2.imshow("mask",mask)





# cv2.imshow("hsv",hsv)


cv2.waitKey(0)

cv2.destroyAllWindows()
