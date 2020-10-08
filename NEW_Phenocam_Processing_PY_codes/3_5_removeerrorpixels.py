# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os.path
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(script_dir,"pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"))
im.show()
newIm = im.load()
width, height = im.size

checkCount = 0
extraCheck = 25
error = True

w = width - 1
h = height - 1

rowCount = 0
colCount = 0
while error is True and rowCount <= h: #if we know there are errors => start changing
  firstPix = im.getpixel((w, h-rowCount))
  #check first if there actually are errors on that row
  while checkCount < extraCheck:
    print("check 1")
    tempwidth = width - 1 - checkCount
    tempheight = height - 1
    temppix = (tempwidth, tempheight)
    if im.getpixel(temppix) != firstPix: 
      print('no error')
      error == False
    checkCount = checkCount + 1

  while error is True and (colCount <= w or im.getpixel((w - colCount, h - rowCount)) == firstPix): #something is odd here
    newIm[(w - colCount), (h-rowCount)] = (255, 0, 0) #doesn't really work with transparancy but it changes the pixel to plack
    colCount = colCount + 1
  
  colCount = width - 1
  rowCount = rowCount + 1

im.show()
