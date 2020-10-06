from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open("SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg")
#print (im.size)

checkCount = 0
extraCheck = 50
error = True
firstPix = im.getpixel((im.width-1, im.height-1))
while checkCount < extraCheck or error == True:
  tempwidth = im.width - 1 - checkCount
  tempheight = im.height - 1
  temppix = (tempwidth, tempheight)
  if im.getpixel(temppix) != firstPix: 
    print('no error')
    error == False
  checkCount = +1

w = im.width - 1
h = im.height - 1

rowCount = 0
colCount = 0
while error == True: #if we know there are errors => start changing
  print('error true')
  if im.getpixel(w, h - rowCount) == firstPix: #if first pixel to the right is wrong we know the row needs to be fixed
    while colCount < (im.width - 1) or im.getpixel(w - colCount, h-rowCount) != firstPix: #make sure not out of bounds or remove correct photos
      im.putpixel(im.getpixel(w - colCount, h-rowCount),(255,255,255))
      colCount = + 1
      #thatPix = (255, 255, 255) #ändra till numpy.nan senare
  else:
    error = False
    
  colCount = im.width - 1
  rowCount = + 1

im.show()