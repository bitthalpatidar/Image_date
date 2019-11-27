from PIL import Image
from resizeimage import resizeimage
import pytesseract
import argparse
import cv2
import os

path1 = "/home/bitthal/Downloads/tesseract-python/images/"
path2 = '/home/bitthal/Downloads/Receipts/'


listing = os.listdir(path1)
file2 = open("MyFile.txt", "r+")
i=0
for file in listing:
    image = cv2.imread(path1 + file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 255, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    filename = "{}.png".format(os.getpid())
    date='01/03/19'
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    file2.write(text)
    #print(file2.readable())
    #file1.writelines(L)
    #print(file2.readlines())
    flag=False
    for line in file2.readlines():
        print(line)
        if date in line:
            print("output is",date)
            cv2.imshow("Image", image)
            cv2.waitKey(0)


    os.remove(filename)
    print("image complete=",i)
    i=i+1


file2.close()

    #cv2.imshow("Image", image)
    # show the output images
    #cv2.imshow("Image", image)
    #cv2.imshow("Output", gray)
    #cv2.waitKey(0)
