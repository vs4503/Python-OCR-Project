# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:50:48 2024

@author: vaibh
"""

import cv2 as cv
import easyocr
import pytesseract
import numpy as np
import pandas as pd
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'path//to//tesseract.exe'

webCam = cv.VideoCapture(0)

while True:
    try:
        check,frame = webCam.read()

        #boolean value to see if video stream is still running
        print(check)
        #Frame captured
        print(frame)

        cv.imshow('Capturing', frame)

        #Waits the defined amount of milliseconds before closing the window
        #If 0 provided -> waits until any key is pressed.
        key = cv.waitKey(1)

        if key == ord('s'):
            final_Image = cv.imwrite('sample3.png', frame) 
            #Closes capturing device
            webCam.release()
            break

        elif key == ord('q'):
            webCam.release()
            print("Camera Off")            
            cv.destroyAllWindows()
            break  
     
    except(KeyboardInterrupt):
        print("Forced Camera turn off")
        webCam.release()
        cv.destroyAllWindows()
        break

dlImage = cv.imread('sample3.png')

if dlImage is None:
    print("Error: Could not load image.")
    exit()

cv.imshow('Initial Image', dlImage)
cv.waitKey(2000)

#Preprocessing Function

#Approach 1
canny = cv.Canny(dlImage, 250, 300)

cv.imshow('Image', canny)
cv.waitKey(4000)

# Apply binary threshold
_, thresh = cv.threshold(canny, 150, 255, cv.THRESH_BINARY)

# Invert the image
thresh = cv.bitwise_not(thresh)

cv.imshow('Image', thresh)
cv.waitKey(4000)

# Display the processed image
cv.imshow('Processed Image', thresh)
cv.waitKey(2000)
    
text = pytesseract.image_to_string(thresh)
print(text)

#---------------------------------------------

#Approach 2
gray = cv.cvtColor(dlImage, cv.COLOR_RGB2GRAY)

blurred = cv.GaussianBlur(gray, (5,5), 0)

thresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)

cv.imshow('Image', thresh)
cv.waitKey(2000)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
dilate = cv.dilate(thresh, kernel, iterations=1)
erode = cv.erode(thresh, kernel, iterations=1)

cv.imshow('Image', erode)
cv.waitKey(4000)

text = pytesseract.image_to_string(erode)
print(text)

contours, _ = cv.findContours(erode, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x,y,w,h) = cv.boundingRect(contour)
    cv.rectangle(dlImage, (x,y), (x+w,y+h), (0, 255, 0), 2)

# Display the processed image
cv.imshow('Processed Image', dlImage)
cv.waitKey(4000)

#--------------------------------------------------------
    
#Approach 3

dlImage = cv.imread('sample3.png')

if dlImage is None:
    print("Error: Could not load image.")
    exit()
    
grayImage = cv.cvtColor(dlImage, cv.COLOR_RGB2GRAY)

blur = cv.medianBlur(grayImage, 3)

thresh = cv.threshold(blur, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

reader = easyocr.Reader(['en'])

result = reader.readtext(thresh, paragraph=False)

dataframe = pd.DataFrame(result)

print("The text is: " + dataframe[1])









