"""
Created on Thu Jul 23 12:25:19 2020
This python code removes all night/dark images based on file size to the respective folders created
automatically. Users are supposed to change filesize as per the station: For instance Asa: 1000.0, 
Skogaryd: 350.0. The size threshold was based on experiments and can differ from station to station. 
@author: Shangharsha
"""
#################################################################################################
#Module Declaration
#################################################################################################

import glob
import os
import shutil

#################################################################################################
def removeDark_function(pathname):
    
    #Define path of source images
    thePath = pathname
    print (pathname)
    #################################################################################################
    #Automatic folder creation, path definition for copying dark images to a separate folder
    #################################################################################################

    #Try-except block is to pass overwrite directories if exists
    folders = ['Dark']
    for folder in folders:
        try:
            os.mkdir(os.path.join(thePath, folder))
        except:
            pass

    #Path definition for storing dark images   
    
    # Changed from dest_dark = thePath +  '\\Dark' 
    dest_dark = thePath + '/Dark'
    

    #################################################################################################

    print ('Filtering out dark images......')

    #Iterating all images
    #Change the path to folder storing images other than filtered
    for img in sorted(glob.glob(os.path.join(thePath, "*.jpg"))):
        
        #Extracting image file name
        dt_info = os.path.basename(img)
        
        #Extracting file size for each image
        fileSize =  os.path.getsize(img)/float(1024)
        
    #################################################################################################
    #Check to move all night images to its respective destination folder
    #################################################################################################        
        #All the images with file size less than 0.9mb are termed as dark images
        if (fileSize <= 350.0):
            shutil.move(img, dest_dark) 
        
    #################################################################################################

    print ('Dark images are filtered out successfully in the defined path.')

    ################################################################################################# 