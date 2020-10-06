from PIL import Image
from PIL import ImageFile
import numpy as np
ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open(r"/Users/emelieulin/Desktop/EXTP40/pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1200.jpg")
#print (im.size)

checkCount = 0
extraCheck = 25
error = True
firstPix = im.getpixel((im.width-1, im.height-1))

while checkCount < extraCheck:
  print('first check')
  tempwidth = im.width - 1 - checkCount
  tempheight = im.height - 1
  temppix = (tempwidth, tempheight)
  if im.getpixel(temppix) != firstPix: 
    print('no error')
    error == False
  checkCount = checkCount + 1

w = im.width - 1
h = im.height - 1

rowCount = 0
colCount = 0
img = im.load()

while error is True: #if we know there are errors => start changing
  print ('second check')
  if im.getpixel((w, h - rowCount)) == firstPix: #if first pixel to the right is wrong we know the row needs to be fixed
    while colCount < (im.width - 1) or im.getpixel(w - colCount, h - rowCount) != firstPix: #make sure not out of bounds or remove correct photos
      im[w - colCount, h-rowCount] = float(np.nan)
      colCount = colCount + 1
      #thatPix = (255, 255, 255) #ändra till numpy.nan senare
  else:
    error = False
    
  colCount = im.width - 1
  rowCount = rowCount + 1

im.show()