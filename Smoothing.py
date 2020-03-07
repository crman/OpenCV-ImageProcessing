import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/crman/PycharmProjects/ImageProcessingLab/Images/Water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernal)

median = cv2.medianBlur(img, 5) #kernL SIZE MUST BE ODD , NOT 1 = SAME AS ORIGINAL

titles = ['image','2DConvolution/Mean','Median']
images = [img, dst, median]

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([], plt.yticks([]))

plt.show()