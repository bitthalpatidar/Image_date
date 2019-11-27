import PIL
from PIL import Image

baseheight = 560
img = Image.open("/home/bitthal/Downloads/tesseract-python/images/0e0dd005.jpeg")
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
img.save("/home/bitthal/Downloads/tesseract-python/images/resized_image.jpg")