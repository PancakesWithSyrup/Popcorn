import cv2
import numpy as np
from matplotlib import pyplot as plt

# Connecting to the Webcam(*Remember 0 on one computer will be different for another computer*)
# cap = cv2.VideoCapture(0)
# Get a frame from the capture device
# ret, frame = cap.read()

# print (ret)

# Releases capture back into the wild
# cap.release()
# Function to take a picture
# def take_photo():
    # cap = cv2.VideoCapture(0)
    # ret, frame = cap.read()
    # cv2.imwrite('webcamphoto.jpg', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    # cap .release()


# Connect to Webcam(*Remember 0 on one computer will be different for another computer*)
# You will be able to see all ROIs on the screen while the camera is on.
# Organize each window and the next time you start the program they will appear in the order you place them.
cap = cv2.VideoCapture(0)
# Loop through every frame until we close our webcam
while cap.isOpened():
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #show image
    cv2.imshow('Webcam', gray_frame)

    # cropped using ROI
    comp11 = cv2.cvtColor(frame[255:255 + 92, 23:23 + 176], cv2.COLOR_BGR2GRAY)
    comp12 = cv2.cvtColor(frame[255:255 + 92, 23:23 + 176], cv2.COLOR_BGR2GRAY)
    comp13 = cv2.cvtColor(frame[257:257 + 72, 251:251 + 181], cv2.COLOR_BGR2GRAY)
    comp14 = cv2.cvtColor(frame[246:246 + 65, 534:534 + 142], cv2.COLOR_BGR2GRAY)
    comp15 = cv2.cvtColor(frame[246:246 + 65, 534:534 + 142], cv2.COLOR_BGR2GRAY)
    comp21 = cv2.cvtColor(frame[102:102 + 43, 68:68 + 83], cv2.COLOR_BGR2GRAY)
    comp22 = cv2.cvtColor(frame[99:99 + 51, 193:193 + 94], cv2.COLOR_BGR2GRAY)
    comp23 = cv2.cvtColor(frame[104:104 + 37, 308:308 + 77], cv2.COLOR_BGR2GRAY)
    comp24 = cv2.cvtColor(frame[88:88 + 42, 428:428 + 76], cv2.COLOR_BGR2GRAY)
    comp25 = cv2.cvtColor(frame[93:93 + 37, 540:540 + 77], cv2.COLOR_BGR2GRAY)
    comp26 = cv2.cvtColor(frame[93:93 + 37, 540:540 + 77], cv2.COLOR_BGR2GRAY)
    comp31 = cv2.cvtColor(frame[43:43 + 49, 160:160 + 61], cv2.COLOR_BGR2GRAY)
    comp32 = cv2.cvtColor(frame[51:51 + 38, 253:253 + 52], cv2.COLOR_BGR2GRAY)
    comp33 = cv2.cvtColor(frame[52:52 + 31, 320:320 + 52], cv2.COLOR_BGR2GRAY)
    comp34 = cv2.cvtColor(frame[51:51 + 32, 400:400 + 52], cv2.COLOR_BGR2GRAY)
    comp35 = cv2.cvtColor(frame[47:47 + 31, 463:463 + 52], cv2.COLOR_BGR2GRAY)
    comp36 = cv2.cvtColor(frame[38:38 + 31, 540:540 + 54], cv2.COLOR_BGR2GRAY)

    # this is the action to show those live feeds cropped out
    cv2.imshow("comp11", comp11)
    cv2.imshow("comp12", comp12)
    cv2.imshow("comp13", comp13)
    cv2.imshow("comp14", comp14)
    cv2.imshow("comp15", comp15)
    cv2.imshow("comp21", comp21)
    cv2.imshow("comp22", comp22)
    cv2.imshow("comp23", comp23)
    cv2.imshow("comp24", comp24)
    cv2.imshow("comp25", comp25)
    cv2.imshow("comp26", comp26)
    cv2.imshow("comp31", comp31)
    cv2.imshow("comp32", comp32)
    cv2.imshow("comp33", comp33)
    cv2.imshow("comp34", comp34)
    cv2.imshow("comp35", comp35)
    cv2.imshow("comp36", comp36)

    # Checks whether q has been hit and stops the Loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releases the webcam
cap.release()
# closes the frame
cv2.destroyAllWindows()
