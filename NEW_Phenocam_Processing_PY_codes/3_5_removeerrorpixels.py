from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open("SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg")
#print (im.size)
#im.show()

checkCount = 0
extraCheck = 50
error = True
firstPix = im.getpixel((im.width-1, im.height-1))
while checkCount < extraCheck or error == True:
  tempwidth = im.width - 1 - checkCount
  tempheight = im.height - 1
  temppix = (tempwidth, tempheight)
  if im.getpixel(temppix) != firstPix: 
    error == False
  checkCount = +1

w = im.width
h = im.height

while error == True:
    
    #if(getpixValue == firstPix):
        #thatPix = (255, 255, 255) #ändra till numpy.nan senare
    #else:
        #error = False

    #if(w == 0):
       # w = width
        #h = height - 1
    #else:
        #w = w - 1

