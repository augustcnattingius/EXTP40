# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os.path
import numpy as np
from cv2 import cv2

script_dir = os.path.dirname(os.path.abspath(__file__))
#img = Image.open(os.path.join(script_dir,"pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"))
im = cv2.imread(os.path.join(script_dir,"pictures/Asa/SWE-ASA-NYB-FOR-P01_20170107_007_1400.jpg"), 1)

checkCount = 0
extraCheck = 25
error = True
height = im.shape[0]
width = im.shape[1]
w = width - 1
h = height - 1
rowCount = 0
colCount = 0

while error is True and rowCount <= h: #if we know there are errors => start changing
  firstPix = im[h-rowCount, w]
  #check first if there actually are errors on that row
  while checkCount < extraCheck:
    tempwidth = width - 1 - checkCount
    tempheight = height - 1
    if (im[tempheight, tempwidth]!=firstPix).all(): 
      error == False
    checkCount = checkCount + 1

  #while error is True and (colCount <= w and (im[h - rowCount, w - colCount] == firstPix).all()): #something is odd here
  #  im[h-rowCount, w - colCount] = np.nan
  #  colCount = colCount + 1
  im[:, (h-rowCount)] = np.nan

  if(im[w, (h-rowCount)] == np.nan):
    print("success")
  

  colCount = 0
  rowCount = rowCount + 1

