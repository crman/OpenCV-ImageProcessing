import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

img = cv2.imread('Car.png',0)
#img = cv2.resize(img, (500, 500))
cv2.imshow("Original", img)
height = img.shape[0]
width = img.shape[1]

pixel = width*height

def histogram(img):
    height = img.shape[0]
    width = img.shape[1]
    hist = np.zeros((256))
    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            hist[a] = hist[a] + 1
    return hist

def cum_histogram(hist):
    cum_hist = hist.copy()
    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]
    return cum_hist

hist = histogram(img)
cum_hist = cum_histogram(hist)

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = math.floor(cum_hist[a]*255/pixel)
        img.itemset((i, j), b)

cv2.imwrite('AfterEqualization.jpg', img)
cv2.imshow('AfterEqualization', img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
