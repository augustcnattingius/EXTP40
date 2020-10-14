# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os.path
import numpy as np
from cv2 import cv2

script_dir = os.path.dirname(os.path.abspath(__file__))
#img = Image.open(os.path.join(script_dir,"pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"))
img = cv2.imread(os.path.join(script_dir,"pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"), 1)
#convert to cv2 np.array ^ because that's what's used later, np.array should be able to have nan values
#OBS note!!!  cv2 save the image in BGR and not RGB, so you have to convert, but a conversion is
#done in stage 4 so I haven't done it here yet

im = img.astype(float)

checkCount = 0
extraCheck = 25
error = True
bigWhile = True
height = im.shape[0]
width = im.shape[1]
w = width - 1
h = height - 1
rowCount = 0
colCount = 0

while bigWhile is True and rowCount <= h: #if we know there are errors => start changing
  firstPix = im[h-rowCount, w]
  #check first if there actually are errors on that row
  while checkCount < extraCheck:
    tempwidth = width - 1 - checkCount
    tempheight = height - 1
    if (im[tempheight, tempwidth]!=firstPix).all(): 
      bigWhile == False
      error = False
    checkCount = checkCount + 1

  #If there are errors => replace that whole row with np.nan
  if error is True:
    im[(h-rowCount), :] = np.nan #tried with only np.nan with no difference
  
  colCount = 0
  rowCount = rowCount + 1


