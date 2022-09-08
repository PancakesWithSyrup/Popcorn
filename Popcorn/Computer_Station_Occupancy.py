import approximations as approximations
import cv2
import numpy as np
from matplotlib import pyplot as plt

# I found that using a light color shape is a lot easier for the algorithm to detect and draw the lines.

# reading image (Make sure to comment out the image you don't want analyzed)
# img = cv2.imread("classroom_image_with_WHITE_TRIANGLES.jpg")
# img = cv2.imread("classroom_image_with_WHITE_TRIANGLES_Two_Students_comp12_comp14.jpg")
img = cv2.imread("classroom_image_with_WHITE_TRIANGLES_Four_Students_comp22_comp25_comp32_comp35.jpg")


# ROIs for individual computer areas
comp12 = img[215:215+40, 101:101+98]
comp13 = img[198:198+39, 267:267+117]
comp14 = img[185:185+37, 545:545+117]
comp21 = img[116:116+30, 68:68+90]
comp22 = img[123:123+25, 199:199+84]
comp23 = img[117:117+30, 307:307+81]
comp24 = img[109:109+30, 431:431+77]
comp25 = img[98:98+28, 540:540+81]
comp31 = img[69:69+30, 156:156+61]
comp32 = img[61:61+32, 255:255+53]
comp33 = img[61:61+30, 321:321+51]
comp34 = img[58:58+22, 400:400+48]
comp35 = img[58:58+20, 469:469+47]
comp36 = img[41:41+30, 545:545+49]

# cropped images using ROIs
# comp12
cv2.imwrite('cropped_comp12.jpg', comp12)
cropped_comp12 = cv2.imread('cropped_comp12.jpg')
# comp13
cv2.imwrite('cropped_comp13.jpg', comp13)
cropped_comp13 = cv2.imread('cropped_comp13.jpg')
# comp14
cv2.imwrite('cropped_comp14.jpg', comp14)
cropped_comp14 = cv2.imread('cropped_comp14.jpg')
# comp21
cv2.imwrite('cropped_comp21.jpg', comp21)
cropped_comp21 = cv2.imread('cropped_comp21.jpg')
# comp22
cv2.imwrite('cropped_comp22.jpg', comp22)
cropped_comp22 = cv2.imread('cropped_comp22.jpg')
# comp23
cv2.imwrite('cropped_comp23.jpg', comp23)
cropped_comp23 = cv2.imread('cropped_comp23.jpg')
# comp24
cv2.imwrite('cropped_comp24.jpg', comp24)
cropped_comp24 = cv2.imread('cropped_comp24.jpg')
# comp25
cv2.imwrite('cropped_comp25.jpg', comp25)
cropped_comp25 = cv2.imread('cropped_comp25.jpg')
# comp31
cv2.imwrite('cropped_comp31.jpg', comp31)
cropped_comp31 = cv2.imread('cropped_comp31.jpg')
# comp32
cv2.imwrite('cropped_comp32.jpg', comp32)
cropped_comp32 = cv2.imread('cropped_comp32.jpg')
# comp33
cv2.imwrite('cropped_comp33.jpg', comp33)
cropped_comp33 = cv2.imread('cropped_comp33.jpg')
# comp34
cv2.imwrite('cropped_comp34.jpg', comp34)
cropped_comp34 = cv2.imread('cropped_comp34.jpg')
# comp35
cv2.imwrite('cropped_comp35.jpg', comp35)
cropped_comp35 = cv2.imread('cropped_comp35.jpg')
# comp36
cv2.imwrite('cropped_comp36.jpg', comp36)
cropped_comp36 = cv2.imread('cropped_comp36.jpg')


# turn cropped image to gray
# comp12
gray_cropped_comp12 = cv2.cvtColor(cropped_comp12, cv2.COLOR_BGR2GRAY)
blurred_comp12 = cv2.GaussianBlur(gray_cropped_comp12, (5, 5), 0)
# comp13
gray_cropped_comp13 = cv2.cvtColor(cropped_comp13, cv2.COLOR_BGR2GRAY)
blurred_comp13 = cv2.GaussianBlur(gray_cropped_comp13, (5, 5), 0)
# comp14
gray_cropped_comp14 = cv2.cvtColor(cropped_comp14, cv2.COLOR_BGR2GRAY)
blurred_comp14 = cv2.GaussianBlur(gray_cropped_comp14, (5, 5), 0)
# comp21
gray_cropped_comp21 = cv2.cvtColor(cropped_comp21, cv2.COLOR_BGR2GRAY)
blurred_comp21 = cv2.GaussianBlur(gray_cropped_comp21, (5, 5), 0)
# comp22
gray_cropped_comp22 = cv2.cvtColor(cropped_comp22, cv2.COLOR_BGR2GRAY)
blurred_comp22 = cv2.GaussianBlur(gray_cropped_comp22, (5, 5), 0)
# comp23
gray_cropped_comp23 = cv2.cvtColor(cropped_comp23, cv2.COLOR_BGR2GRAY)
blurred_comp23 = cv2.GaussianBlur(gray_cropped_comp23, (5, 5), 0)
# comp24
gray_cropped_comp24 = cv2.cvtColor(cropped_comp24, cv2.COLOR_BGR2GRAY)
blurred_comp24 = cv2.GaussianBlur(gray_cropped_comp24, (5, 5), 0)
# comp25
gray_cropped_comp25 = cv2.cvtColor(cropped_comp25, cv2.COLOR_BGR2GRAY)
blurred_comp25 = cv2.GaussianBlur(gray_cropped_comp25, (5, 5), 0)
# comp31
gray_cropped_comp31 = cv2.cvtColor(cropped_comp31, cv2.COLOR_BGR2GRAY)
blurred_comp31 = cv2.GaussianBlur(gray_cropped_comp31, (5, 5), 0)
# comp32
gray_cropped_comp32 = cv2.cvtColor(cropped_comp32, cv2.COLOR_BGR2GRAY)
blurred_comp32 = cv2.GaussianBlur(gray_cropped_comp32, (5, 5), 0)
# comp33
gray_cropped_comp33 = cv2.cvtColor(cropped_comp33, cv2.COLOR_BGR2GRAY)
blurred_comp33= cv2.GaussianBlur(gray_cropped_comp33, (5, 5), 0)
# comp34
gray_cropped_comp34 = cv2.cvtColor(cropped_comp34, cv2.COLOR_BGR2GRAY)
blurred_comp34 = cv2.GaussianBlur(gray_cropped_comp34, (5, 5), 0)
# comp35
gray_cropped_comp35 = cv2.cvtColor(cropped_comp35, cv2.COLOR_BGR2GRAY)
blurred_comp35 = cv2.GaussianBlur(gray_cropped_comp35, (5, 5), 0)
# comp36
gray_cropped_comp36 = cv2.cvtColor(cropped_comp36, cv2.COLOR_BGR2GRAY)
blurred_comp36 = cv2.GaussianBlur(gray_cropped_comp36, (5, 5), 0)

# convert grayscale to binary image
# comp12
_, threshold_comp12 = cv2.threshold(blurred_comp12, 245, 255, cv2.THRESH_BINARY_INV)
# comp13
_, threshold_comp13 = cv2.threshold(blurred_comp13, 245, 255, cv2.THRESH_BINARY_INV)
# comp14
_, threshold_comp14 = cv2.threshold(blurred_comp14, 245, 255, cv2.THRESH_BINARY_INV)
# comp21
_, threshold_comp21 = cv2.threshold(blurred_comp21, 245, 255, cv2.THRESH_BINARY_INV)
# comp22
_, threshold_comp22 = cv2.threshold(blurred_comp22, 245, 255, cv2.THRESH_BINARY_INV)
# comp23
_, threshold_comp23 = cv2.threshold(blurred_comp23, 245, 255, cv2.THRESH_BINARY_INV)
# comp24
_, threshold_comp24 = cv2.threshold(blurred_comp24, 245, 255, cv2.THRESH_BINARY_INV)
# comp25
_, threshold_comp25 = cv2.threshold(blurred_comp25, 245, 255, cv2.THRESH_BINARY_INV)
# comp31
_, threshold_comp31 = cv2.threshold(blurred_comp31, 245, 255, cv2.THRESH_BINARY_INV)
# comp32
_, threshold_comp32 = cv2.threshold(blurred_comp32, 245, 255, cv2.THRESH_BINARY_INV)
# comp33
_, threshold_comp33 = cv2.threshold(blurred_comp33, 245, 255, cv2.THRESH_BINARY_INV)
# comp34
_, threshold_comp34 = cv2.threshold(blurred_comp34, 245, 255, cv2.THRESH_BINARY_INV)
# comp35
_, threshold_comp35 = cv2.threshold(blurred_comp35, 245, 255, cv2.THRESH_BINARY_INV)
# comp36
_, threshold_comp36 = cv2.threshold(blurred_comp36, 245, 255, cv2.THRESH_BINARY_INV)

# finding the contours in the given image using findContours() function
# comp12
contours_comp12, _ = cv2.findContours(threshold_comp12, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp13
contours_comp13, _ = cv2.findContours(threshold_comp13, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp14
contours_comp14, _ = cv2.findContours(threshold_comp14, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp21
contours_comp21, _ = cv2.findContours(threshold_comp21, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp22
contours_comp22, _ = cv2.findContours(threshold_comp22, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp23
contours_comp23, _ = cv2.findContours(threshold_comp23, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp24
contours_comp24, _ = cv2.findContours(threshold_comp24, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp25
contours_comp25, _ = cv2.findContours(threshold_comp25, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp31
contours_comp31, _ = cv2.findContours(threshold_comp31, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp32
contours_comp32, _ = cv2.findContours(threshold_comp32, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp33
contours_comp33, _ = cv2.findContours(threshold_comp33, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp34
contours_comp34, _ = cv2.findContours(threshold_comp34, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp35
contours_comp35, _ = cv2.findContours(threshold_comp35, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# comp36
contours_comp36, _ = cv2.findContours(threshold_comp36, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp12
for count in contours_comp12:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp12, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp12_occupied = True
    elif len(approximations) > 4:
        comp12_occupied = False
    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp12 is Occupied?:  ", comp12_occupied)
    #  print("Comp12 Contours: ", len(approximations))

    cv2.imshow("class12", blurred_comp12)

    # this is the action to show those images
    cv2.imshow("comp12", comp12)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp13
for count in contours_comp13:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp13, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp13_occupied = True
    elif len(approximations) > 4:
        comp13_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp13 is Occupied?:  ", comp13_occupied)
    #  print("Comp13 Contours: ", len(approximations))

    cv2.imshow("class13", blurred_comp13)

    # this is the action to show those images
    cv2.imshow("comp13", comp13)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp14
for count in contours_comp14:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp14, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp14_occupied = True
    elif len(approximations) > 4:
        comp14_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp14 is Occupied?:  ", comp14_occupied)
    #  print("Comp14 Contours: ", len(approximations))

    cv2.imshow("class14", blurred_comp14)

    # this is the action to show those images
    cv2.imshow("comp14", comp14)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp21
for count in contours_comp21:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp21, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp21_occupied = True
    elif len(approximations) > 4:
        comp21_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp21is Occupied?:  ", comp21_occupied)
    #  print("Comp21 Contours: ", len(approximations))

    cv2.imshow("class21", blurred_comp21)

    # this is the action to show those images
    cv2.imshow("comp21", comp21)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp22
for count in contours_comp22:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp22, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp22_occupied = True
    elif len(approximations) > 4:
        comp22_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp22 is Occupied?:  ", comp22_occupied)
    # print("Comp22 Contours: ", len(approximations))

    cv2.imshow("class22", blurred_comp22)

    # this is the action to show those images
    cv2.imshow("comp22", comp22)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp23
for count in contours_comp23:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp23, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp23_occupied = True
    elif len(approximations) > 4:
        comp23_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp23 is Occupied?:  ", comp23_occupied)
    #  print("Comp23 Contours: ", len(approximations))

    cv2.imshow("class23", blurred_comp23)

    # this is the action to show those images
    cv2.imshow("comp23", comp23)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp24
for count in contours_comp24:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp24, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp24_occupied = True
    elif len(approximations) > 4:
        comp24_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp24 is Occupied?:  ", comp24_occupied)
    #  print("Comp24 Contours: ", len(approximations))

    cv2.imshow("class24", blurred_comp24)

    # this is the action to show those images
    cv2.imshow("comp24", comp24)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp25
for count in contours_comp25:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp25, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp25_occupied = True
    elif len(approximations) > 4:
        comp25_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    # print("Comp25 is Occupied?:  ", comp25_occupied)
    #  print("Comp25 Contours: ", len(approximations))

    cv2.imshow("class25", blurred_comp25)

    # this is the action to show those images
    cv2.imshow("comp25", comp25)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp31
for count in contours_comp31:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp31, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp31_occupied = True
    elif len(approximations) > 4:
        comp31_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp31 is Occupied?:  ", comp31_occupied)
    # print("Comp31 Contours: ", len(approximations))

    cv2.imshow("class31", blurred_comp31)

    # this is the action to show those images
    cv2.imshow("comp31", comp31)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp32
for count in contours_comp32:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp32, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp32_occupied = True
    elif len(approximations) > 4:
        comp32_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp32 is Occupied?:  ", comp32_occupied)
    #  print("Comp32 Contours: ", len(approximations))

    cv2.imshow("class32", blurred_comp32)

    # this is the action to show those images
    cv2.imshow("comp32", comp32)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp33
for count in contours_comp33:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp33, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp33_occupied = True
    elif len(approximations) > 4:
        comp33_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp33 is Occupied?:  ", comp33_occupied)
    #  print("Comp33 Contours: ", len(approximations))

    cv2.imshow("class33", blurred_comp33)

    # this is the action to show those images
    cv2.imshow("comp33", comp33)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp34
for count in contours_comp34:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp34, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp34_occupied = True
    elif len(approximations) > 4:
        comp34_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    #  print("Comp34 is Occupied?:  ", comp34_occupied)
    #  print("Comp34 Contours: ", len(approximations))

    cv2.imshow("class34", blurred_comp34)

    # this is the action to show those images
    cv2.imshow("comp34", comp34)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp35
for count in contours_comp35:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp35, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp35_occupied = True
    elif len(approximations) > 4:
        comp35_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    # print("Comp13 is Occupied?:  ", comp35_occupied)
    #  print("Comp13 Contours: ", len(approximations))

    cv2.imshow("class35", blurred_comp35)

    # this is the action to show those images
    cv2.imshow("comp35", comp35)

# using approxPolyDP() function and the contours are drawn in the image using drawContours() function
# comp36
for count in contours_comp36:
    epsilon = 0.01*cv2.arcLength(count, True)
    approximations = cv2.approxPolyDP(count, epsilon, True)
    cv2.drawContours(blurred_comp36, [approximations], 0, 0, 3)
    i, j = approximations[0][0]

    # if statement to determine if Occupied or Vacant
    if len(approximations) <= 4:
        comp36_occupied = True
    elif len(approximations) > 4:
        comp36_occupied = False

    # This is to test individual 'for' loop results (1st cycle should report 4)
    # print("Comp36 is Occupied?:  ", comp36_occupied)
    # print("Comp36 Contours: ", len(approximations))

    # will show the blurred gray cropped image with the drawn lines (comment out to hide)
    cv2.imshow("class36", blurred_comp36)

    # this is the action to show the image used (comment out to hide)
    cv2.imshow("comp36", comp36)

# Final Results of computer stations either Occupied:True or Occupied:False
print("Comp12 is Occupied?:  ", comp12_occupied)
print("Comp13 is Occupied?:  ", comp13_occupied)
print("Comp14 is Occupied?:  ", comp14_occupied)
print("Comp21 is Occupied?:  ", comp21_occupied)
print("Comp22 is Occupied?:  ", comp22_occupied)
print("Comp23 is Occupied?:  ", comp23_occupied)
print("Comp24 is Occupied?:  ", comp24_occupied)
print("Comp25 is Occupied?:  ", comp25_occupied)
print("Comp31 is Occupied?:  ", comp31_occupied)
print("Comp32 is Occupied?:  ", comp32_occupied)
print("Comp33 is Occupied?:  ", comp33_occupied)
print("Comp34 is Occupied?:  ", comp34_occupied)
print("Comp35 is Occupied?:  ", comp35_occupied)
print("Comp36 is Occupied?:  ", comp36_occupied)

cv2.waitKey(0)


