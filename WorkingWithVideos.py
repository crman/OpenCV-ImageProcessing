#Importing OpenCV Library
import cv2

#Capturing Video From the Camera
cap1 = cv2.VideoCapture(0)
#Taking Video from the File
cap2 = cv2.VideoCapture('C:/Users/crman/PycharmProjects/DataAnalyticsLabs/Data/Practical 4/Demo.mp4')

#Saving Video file from the WebCam
outputNormal = out=cv2.VideoWriter('OutputNormal.mp4',cv2.VideoWriter_fourcc('m','p','4','v'),20.0,(640,480))

#Storing the video frame
frame_list = []

while True:
    ret1, frame1 = cap1.read()      #From Webcam
    ret2, frame2 = cap2.read()      #From File

    #Storing Frame from the video file for reversing
    frame_list.append(frame2)

    #Converting video file into GrayScale
    grayFrame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    if ret1 == True:
        outputNormal.write(frame1)      #Saving Video file from the WebCam

    #Showing Video Frames
    cv2.imshow('Web Camera', frame1)
    cv2.imshow('Gray Camera', grayFrame)
    cv2.imshow('Demo Video', frame2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        #Storing Image on press 'q'
        cv2.imwrite('CapturedImage.jpg', frame1)

        outputNormal.release()
        cap1.release()
        cap2.release()

        cv2.destroyAllWindows()

#Reversing the Video File
frame_list.pop()
frame_list.reverse()

for frame in frame_list:
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print("Image Captured")
print("Video Saved")
cv2.destroyAllWindows()

