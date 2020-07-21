#importing required libraries
from PIL import Image
import matplotlib.image as im
import csv
import glob
import numpy as np


#importing(opening) the image
img = im.imread('1.jpg')

r = []  #for storing red values
g = []  #for storing green values
b = []  #for storing blue values

#iterating over the image
for row in img:
    for pixel in row:

        t_r, t_g, t_b = pixel
        r.append(t_r)
        g.append(t_g)
        b.append(t_b)

#combining the values for inserting in csv file
rows = zip(r, g, b)

#opening csv file and writing rgb values to file
with open('RGB1Image.csv', 'w') as file:
    wr = csv.writer(file)

    wr.writerow(['r', 'g', 'b'])
    for row in rows:
        wr.writerow(row)


#for finding rgb values of images
def r_g_b(image):
    r = []
    g = []
    b = []

    for row in image:
        for pixel in row:
            t_r, t_g, t_b = pixel
            r.append(t_r)
            g.append(t_g)
            b.append(t_b)
    
    return r, g, b

#for importing 10 RGB images
allimages = glob.glob('RGBImages/*.jpg')
i = 0

for image in allimages:
    img = im.imread(image)
    r, g, b = r_g_b(img)
    i += 1
    
    myFile = open('RGB10Images.csv', 'a', newline='')
    writer = csv.writer(myFile)

    writer.writerow(['R value of image no. {}:'.format(i)])
    writer.writerow(r)
    writer.writerow(['G value of image no. {}:'.format(i)])
    writer.writerow(g)
    writer.writerow(['B value of image no. {}:'.format(i)])
    writer.writerow(b)
    writer.writerow([" "])