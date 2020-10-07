"""
Created on Fri Feb 21 16:07:04 2020
@author: Shangharsha
This code uses the user defined DN threshold for filtering out snow covered phenocamera images.
This script is based on the analysis of the blue component of an RGB image, because the snow 
surface presents higher reflectance values in the blue wavelength range. 
All thresholds are user defined.  
"""

#################################################################################################
#Module Declaration
#################################################################################################

import glob
import os
import shutil
from cv2 import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime

#################################################################################################
#Get time now. This helps to compute total elapsed time for running the code.
#################################################################################################
start = datetime.now()

#################################################################################################
#Automatic folder creation, path definition for cutting and pasting snowy images for the year
#################################################################################################

#Folder path definition for original images
thePath = r'E:\Internship\2018'

#Automatically creating folders in the directory to store snowy images 
#Try-except block is to pass overwrite directories if exists
folders = ['Snowy']
for folder in folders:
    try:
        os.mkdir(os.path.join(thePath, folder))
    except:
        pass

#Defining the path for saving filtered images
#Always change the base path i.e. 'E:\Internship\snowTest\'
dest = thePath + '\Snowy'

#################################################################################################
#Display Region of Interest (ROI) selection in the image  
#################################################################################################

#Random selection of one image from the image folder to show the extent of ROI
imgDir = thePath + '\\' + random.choice(os.listdir(thePath))

#Loading image from the specified file
img = cv2.imread(imgDir)

#ROI definition for the image
pts1 = np.array([[100, 1400], [100, 250], [2500, 250], [2500, 1400]]) 
cv2.polylines(img, np.int32([pts1]), 1, (0, 0, 255), 10)

#Create a mask with 0 as background having same size like that of original image
mask = np.zeros_like(img)

#Fill the polygon with white colour where we want to apply the mask
cv2.fillPoly(mask, np.int32([pts1]), (255,255,255))

#OpenCV represents image in reverse order BGR; so convert it to appear in RGB mode and plot it
plt.rcParams['figure.figsize'] = (16,8)
plt.figure(0)
plt.axis('on')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#################################################################################################
#Empty lists to store the corresponding vegetation indices value
#################################################################################################

meanRDN = []
meanBDN = []
meanGDN = []
DOY = []

#################################################################################################
#Filter out snow covered PhenoCam images to a separate folder 'Snowy' in the image directory
#################################################################################################

#Iterating through all the images to calculate total DN within given ROI
for img in sorted(glob.glob(os.path.join(thePath, '*.jpg'))):
   
    #Reading image one by one
    cv_img = cv2.imread(img)
    
    #Extracting image file name
    imgName = os.path.basename(img)
    
    #Day of Year information (DOY) extraction from image file name
    dayOfYear = imgName.split('_')[2]
    DOY.append(dayOfYear)
    
    #Apply the mask and extract the image data within mask only
    masked = cv2.bitwise_and(cv_img, mask)
    
    #Splitting RGB image into separate bands
    B, G, R = cv2.split(masked)

    #Finding out mean DN of RGB bands within ROI 
    Rm = np.mean(np.ma.masked_equal(R, 0))
    Gm = np.mean(np.ma.masked_equal(G, 0))
    Bm = np.mean(np.ma.masked_equal(B, 0))
       
    #Appending these values to respective lists storing them
    meanRDN.append(Rm)
    meanBDN.append(Bm)
    meanGDN.append(Gm)
    
    #Applying threshold to filter out snowy images; threshold values can be adjusted
    #Snow surface presents higher reflectance in the blue wavelength range 
    snow = 80
    if (Bm >= snow) :
        shutil.move(img, dest)
        
#Plotting the mean DN values across all 3 channels (i.e. RGB)
#Horizontal line represents the snow threshold value for filtering out snowy images        
plt.figure(1)
plt.rcParams['figure.figsize'] = (16,8)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.grid(True, alpha = 0.3)
plt.plot([int(i) for i in DOY], meanGDN, 'o', color = 'green',  mfc = 'none', markersize = 5, label = 'Mean Green')
plt.plot([int(i) for i in DOY], meanBDN, 'o', color = 'blue', markersize = 5, label = 'Mean Blue')
plt.plot([int(i) for i in DOY], meanRDN, 'o', color = 'red',  mfc = 'none', markersize = 5, label = 'Mean Red')
plt.hlines(snow, 0, 365, colors='k', linestyles='solid', label='Snow Threshold')
plt.xlabel('Day of Year (DOY)', fontsize = 20)
plt.ylabel('Mean Digital Number (DN)', fontsize = 20)
plt.legend(loc = 'best', fontsize = 18)

#################################################################################################
#Find out the total elapsed time and print out on the screen
#################################################################################################

end = datetime.now()
time_taken = end - start

#These line of codes will print out the total elapsed time
print ('\n')
print ('Time elapsed: {}'.format(time_taken))  
#################################################################################################   