import cv2                          #Importing OpenCV Library
import matplotlib.image as im       #Importing Matplotlib Library
import csv                          #Importing CSV Library



#-------- Openning an Image and Converting it to Gray Image --------

#Image1 in Gray and Color
img1Colored = cv2.imread('Images/Image1.jpg')
img1Colored = cv2.resize(img1Colored,(300, 300))
img1Gray = cv2.imread('Images/Image1.jpg',0)
img1Gray = cv2.resize(img1Gray,(300, 300))

#Image2 in Gray and Color
img2Colored = cv2.imread('Images/Image2.jpg')
img2Colored = cv2.resize(img2Colored,(300,300))
img2Gray = cv2.imread('Images/Image2.jpg',0)
img2Gray = cv2.resize(img2Gray,(300,300))


#--------Blurring the Image1 and Image2----------

image1Blured = cv2.blur(img1Colored, (5, 5))
image2Blured = cv2.blur(img2Colored, (5, 5))


#-------- Extracting RGB from Color Image--------

B, G, R = cv2.split(img1Colored)


#--------- Operations on Image ---------

#Adding two Images
addedImage = cv2.add(img1Colored, img2Colored)
addWeightedImage = cv2.addWeighted(img1Colored, 0.5, img2Colored, 0.4, 0)

#Different Operations on the Images
imgSubtracted = cv2.subtract(img1Colored, img2Colored)              #Subtracting two images
imgAND = cv2.bitwise_and(img1Colored, img2Colored, mask=None)       #Bitwise AND
imgOR = cv2.bitwise_or(img1Colored, img2Colored, mask=None)         #Bitwise OR
imgXOR = cv2.bitwise_xor(img1Colored, img2Colored, mask=None)       #Bitwise XOR
imgNOT = cv2.bitwise_not(img1Colored, img2Colored, mask=None)       #Bitwise NOT


#----------Drawing the Shapes on the Image---------

imgRect = cv2.rectangle(image1Blured, (50, 50), (200, 200), (255, 255, 0), thickness=2)  #Drawing Rectangle on Image
imgCircle = cv2.circle(image2Blured, (150, 150), 100, (255, 255, 0), thickness=2)        #Drawing Circle on Image


#--------Extracting RGB Valus from Images and Storing it into CSV file--------

#importing(opening) the image
imgCSV = im.imread('Images/Image1.jpg')

r = []  #for storing red values
g = []  #for storing green values
b = []  #for storing blue values

#iterating over the image
for row in imgCSV:
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

#--------Detecting Eyes from the Face using Haarcascade Model-------

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')       #Haarcascade Model for Detecting Eyes

imgFace = cv2.imread('Images/Face.jpg')                         #Importing Image with Face
imgFace = cv2.resize(imgFace, (300, 300))
imgFaceGray = cv2.cvtColor(imgFace, cv2.COLOR_BGR2GRAY)         #Converting into Gray

eyes = eyeCascade.detectMultiScale(imgFaceGray, 1.3, 5)         #Eyes from the Model

#For Drawing Rectangle on the Detected Eyes
for (x, y, w, h) in eyes:
    cv2.rectangle(imgFace, (x, y), (x+w, y+h), (255, 0, 0), 2)


#---------Showing all the Operations----------

#Showing Eye Detected Image
cv2.imshow("Eyes Detected Image", imgFace)

#Showing Rectangle and Circle on Image
cv2.imshow("Rectangle Image", imgRect)
cv2.imshow("Circle Image", imgCircle)

#Showing Operations of the Images
cv2.imshow("Subtracted Image", imgSubtracted)
cv2.imshow("Bitwise AND", imgAND)
cv2.imshow("Bitwise OR", imgOR)
cv2.imshow("Bitwise XOR", imgXOR)
cv2.imshow("Bitwise NOT", imgNOT)

#Showing added and weighted images
cv2.imshow("Added Images", addedImage)
cv2.imshow("Weighted Images", addWeightedImage)

#Showing R, G, B Images
cv2.imshow("R Image", R)
cv2.imshow("G Image", G)
cv2.imshow("B Image", B)

#Showing Blured Image1 and Image2
cv2.imshow("Image1 Blured", image1Blured)
cv2.imshow("Image2 Blured", image2Blured)

#Showing Gray and Colored Image1
cv2.imshow("Image1 Colored", img1Colored)
cv2.imshow("Image1 Gray", img1Gray)

#Showing Gray and Colored Image2
cv2.imshow("Image2 Colored", img2Colored)
cv2.imshow("Image2 Gray", img2Gray)

cv2.waitKey(0)
cv2.destroyAllWindows()