# Name: approach_1.py
# By Dr. S. S. Gajbhar
import cv2
import numpy as np
def auto_canny(image, sigma=0.33):
    '''
    This function automatically detects the edges of an input image.
    reference:https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-                  python-and-opencv/
    '''
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged
image = cv2.imread('apples.png')
image_d = image.copy()
img_blur = cv2.GaussianBlur(image, (5,5), 0)
img_ms = cv2.pyrMeanShiftFiltering(img_blur, 10, 90)

edge = auto_canny(img_ms)
cnts,_ = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
c_num=0
for i,c in enumerate(cnts):
    # draw a circle enclosing the object
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if r>34:
        c_num+=1
        cv2.circle(image_d, (int(x), int(y)), int(r), (0, 255, 0), 2)
        cv2.putText(image_d, "#{}".format(c_num), (int(x) - 10, int(y)), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    else:
        continue

cv2.imshow("Image with Apples",image)
cv2.imshow("Edge Map", edge)
cv2.imshow("Image with detected Apples",image_d)
cv2.waitKey(0)
