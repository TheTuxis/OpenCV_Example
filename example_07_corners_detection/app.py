import cv2
import numpy as np

vc = cv2.VideoCapture(0)

rval, img = vc.read()

while True:

  if img is not None:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]

    cv2.imshow('dst',img)
  rval, img = vc.read()
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
