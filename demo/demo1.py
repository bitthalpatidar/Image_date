from PIL import Image
from resizeimage import resizeimage
import pytesseract
import argparse
import cv2
import os
import glob
i=0
path1 = "/home/bitthal/Downloads/tesseract-python/images/"
path2 = '/home/bitthal/Downloads/Receipts/'
file2 = open("MyFile1.txt", "r+")
#for img in glob.glob("/home/bitthal/Downloads/Receipts/*.jpeg"):
for img in glob.glob("/home/bitthal/Downloads/tesseract-python/images/*.jpeg"):
    cv_img = cv2.imread(img)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "{}.jpeg".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    file2.write(text)
    file2.write("===============================================================================")
    os.remove(filename)
    #print(text)
    print("====image complete===and show====",i)
    i+=1
    #cv2.imshow("image",cv_img)
    #cv2.waitKey(0)
    #file2.write(("============================================================"))
    number="01/03/19"
    if number in text:
        print("out put data is=====",number)
file2.close()