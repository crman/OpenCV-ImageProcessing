import numpy as np
import cv2
import math
img=cv2.imread('C:/Users/crman/PycharmProjects/ImageProcessingLab/Images/1.jpg',0)
img = cv2.resize(img,(500,500))
cv2.imshow('Original',img)
height=img.shape[0]
width=img.shape[1]

threshold=150

for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i, j)
        if a > threshold:
            b = 255
        else:
            b = 0
        img.itemset((i, j), b)
cv2.imwrite('Threshold.jpg', img)
cv2.imshow('Threshold', img)
k=cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()