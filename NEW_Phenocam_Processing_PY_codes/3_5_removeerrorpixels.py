# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os.path
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir,"pictures\Asa\SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"))
width, height = im.size

checkCount = 0
extraCheck = 25
error = True
firstPix = im.getpixel((width-1, height-1))
while checkCount < extraCheck:
  print (im.size)
  tempwidth = width - 1 - checkCount
  tempheight = height - 1
  temppix = (tempwidth, tempheight)
  if im.getpixel(temppix) != firstPix: 
    print('no error')
    error == False
  checkCount += 1

w = width - 1
h = height - 1

rowCount = 0
colCount = 0
while error is True: #if we know there are errors => start changing
  print('second check')
  if im.getpixel(w, h - rowCount) == firstPix: #if first pixel to the right is wrong we know the row needs to be fixed
    while colCount < (width - 1) or im.getpixel(w - colCount, h - rowCount) != firstPix: #make sure not out of bounds or remove correct photos
      im[w - colCount, h-rowCount] = float(np.nan) #HERE IS THE PROBLEM
      colCount = colCount + 1
  else:
    error = False
    
  colCount = width - 1
  rowCount += 1

im.show()