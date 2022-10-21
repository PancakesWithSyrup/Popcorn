import cv2

def findPeople(img) -> bool:
    cv2.imwrite("croppedImg.jpg", img)
    croppedImage = cv2.imread("croppedImg.jpg")
    # Turn image to grey and then blur it
    grayCropped = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
    blurredImage = cv2.GaussianBlur(grayCropped, (5, 5), 0)
    # Convert the blurred image to a binary image
    _, binaryImage = cv2.threshold(blurredImage, 245, 255, cv2.THRESH_BINARY_INV)
    # Now find the contours
    contours, _ = cv2.findContours(binaryImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # using approxPolyDP function and the contours are drawn in the image using drawContours() function
    for count in contours:
        epsilon = 0.01*cv2.arcLength(count, True)
        approximations = cv2.approxPolyDP(count, epsilon, True)
        cv2.drawContours(blurredImage, [approximations], 0, 0, 3)
        i, j = approximations[0][0]
        # if statement to determine if Occupied or Vacant
        if len(approximations) <= 4:
            occupied = True
        elif len(approximations) > 4:
            occupied = False
        # This is to test individual 'for' loop results (1st cycle should report 4)
        #  print("Comp12 is Occupied?:  ", comp12_occupied)
        #  print("Comp12 Contours: ", len(approximations))
        #cv2.imshow("Blurred Image", blurredImage)
        # this is the action to show those images
        #cv2.imshow("Image", img)
    return occupied


# img = cv2.imread("classroom_image_with_WHITE_TRIANGLES.jpg")
# img = cv2.imread("classroom_image_with_WHITE_TRIANGLES_Two_Students_comp12_comp14.jpg")
img = cv2.imread("classroom_image_with_WHITE_TRIANGLES_Four_Students_comp22_comp25_comp32_comp35.jpg")

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

arrayOfImages = [comp12, comp13, comp14,
                comp21, comp22, comp23, comp24, comp25,
                comp31, comp32, comp33, comp34, comp35, comp36]
results = [findPeople(img) for img in arrayOfImages]
print(results)