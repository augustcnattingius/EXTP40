"""
Created on Fri Feb 21 16:07:04 2020
This code uses the user defined time threshold for filtering out phenocamera images.
@author: Shangharsha
"""

#################################################################################################
#Module Declaration
#################################################################################################

import glob
import os
import shutil
from datetime import datetime

#################################################################################################
#Get time now. This computes total elapsed time for running the code.
#################################################################################################
start = datetime.now()

#################################################################################################

#################################################################################################
#Automatic folder creation, path definition for copying and pasting images 
#################################################################################################

#Path definition for source images
imgSrc = r'E:\Internship\Final\Lonnstorp\SWE-LON-SFA-AGR-P03\L1\2020'

#Automatically creating folders in the directory to store filtered images
#Try-except block is to pass overwrite directories if exists
folders = ['10TO14']
for folder in folders:
    try:
        os.mkdir(os.path.join(imgSrc, folder))
    except:
        pass

#Path definition for saving filtered images 
dest = imgSrc + '\\10TO14'

#################################################################################################
#Filter out PhenoCam images within user defined time frame
#################################################################################################

#Iterating all images and saving it in a new folder
for img in sorted(glob.glob(os.path.join(imgSrc, '*.jpg'))):
    
    #Extracting image file name
    dt_info = os.path.basename(img)
     
    #Day of Year information (DOY) extraction from image file name
    ymdt = dt_info.split('_')[-1]
    
    #TimeStamp information extraction from file name
    hour = int(ymdt.split('.')[0][0:2])

    #Condition to check the time of image acquisition for a given image
    if (hour >= 10) and (hour <= 14):
        
        #Copy the images to destination folder
        shutil.copy(img, dest)

#################################################################################################
        
#################################################################################################
#Find out the total elapsed time and print out on the screen
#################################################################################################

end = datetime.now()
time_taken = end - start

print ('\n')
print ('Time elapsed: {}'.format(time_taken)) 
print ('Images between user defined time thresholds are filtered successfully.')

#################################################################################################