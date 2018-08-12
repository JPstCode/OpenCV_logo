import numpy as np
import cv2 as cv

img = np.zeros((600,600,3), np.uint8)
img[:] = (255,255,255)

cv.circle(img, (300, 135),95, (0,0,255),75)
cv.circle(img, (155,386),95, (0,255,0),75)
tripts = np.array([[300,135],[155,386],[445,386]],np.int32 )



cv.fillConvexPoly(img,tripts,(255,255,255))
cv.circle(img, (445, 386),95, (255,0,0),75)

blutripts = np.array([[445,386],[363,250],[531,240]],np.int32)


cv.fillConvexPoly(img,blutripts,(255,255,255))


cv.imshow('opencv_logo',img)
cv.waitKey(0)
cv.destroyAllWindows()
