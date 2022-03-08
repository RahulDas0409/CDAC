import cv2
import numpy as np

img1 = cv2.imread("C:/Users/Cdac_Robotics_Dell/Downloads/Distance_measurement_using_single_camera-main/Distance_measurement_using_single_camera-main/Apple.jpg")

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)

imgkp1 = cv2.drawKeypoints(img1,kp1,None)

print(des1)

cv2.imshow('img1', img1)
cv2.imshow("KP1", imgkp1)
cv2.waitKey(0)
