"""
Created on Wed Jul 15 13:05:54 2020
This code renames the .jpg images for stations: Asa, Lonnstorp, Robacksdalen, Skogaryd, Tarfala &
Svartberget. Users are supposed to pass the file path for reading the original images and they'll
be renamed. Only one station files can be renamed at once. Uncomment only the linesfor renaming a 
single station. 
@author: Shangharsha
"""


#################################################################################################
#Module Declaration
#################################################################################################

import glob
import os
import datetime

#################################################################################################
#Path Definition for source images
#################################################################################################

def imgRename_function(pathname):
    
#Source images 
   
    srcImgdir = pathname

    #################################################################################################
    #################################################################################################

    #Iterating through the .jpg files in source directory
    for img in sorted(glob.glob(os.path.join(srcImgdir, "*.jpg"))):
        
        #Extracting image file name
        oldimgName = os.path.basename(img)
        '''
        ##############################################################################################
        #Renaming Asa Station .jpg files
        ##############################################################################################
        
        newimgName = oldimgName.replace('Asa', 'SWE-ASA-NYB-FOR-P01')
        os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))   
        
        ##############################################################################################
        ##############################################################################################
        '''
        '''
        ##############################################################################################
        #Renaming Skogaryd Station .jpg files (Valid only for SWE-SRC-STD-FOR-P01)
        ##############################################################################################
        
        newimgName = oldimgName.replace('Skogaryd', 'SWE-SRC-STD-FOR-P01')
        os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))   
        
        ##############################################################################################
        ##############################################################################################
        '''

        ##############################################################################################
        #Renaming Skogaryd .jpg files (SWE-SRC-CEN-FOR-P01, SWE-SRC-CEN-FOR-P02, SWE-SRC-CEN-FOR-P03)
        ##############################################################################################
        
        #Don't forget to change the first string of newimgName variable as per the site
        #Splitting the image file name to extract the year, month, day, hour, minute information
        splitted = oldimgName.split('_')
        yy = splitted[1].split('-')[0]
        mm = splitted[1].split('-')[1]
        dd = splitted[1].split('-')[2]
        hhmm = splitted[2].split('.')[0]
        
        #Concatenating ddmmyy for calculating day of year
        sdate = dd + '-' + mm + '-' + yy
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = 'SWE-SRC-CEN-FOR-P01' + '_' + yy + mm + dd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = 'SWE-SRC-CEN-FOR-P01' + '_' + yy + mm + dd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = 'SWE-SRC-CEN-FOR-P01' + '_' + yy + mm + dd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        
        '''
        ##############################################################################################
        #Renaming Lonnstorp .jpg files (SWE-LON-SFA-AGR-P01, SWE-LON-SFA-AGR-P02, SWE-LON-SFA-AGR-P03)
        ##############################################################################################
        #First type of Naming convention in Lonnstorp i.e. '20180320_1603_SWE-LON-SFA-P01'
        
        #Splitting the image file name to extract the year, month, day, hour, minute information
        splitted = oldimgName.split('_')
        yymmdd = splitted[0]
        hhmm = splitted[1]
        baseName = splitted[2].split('.')[0]
        
        #Concatenating ddmmyy for calculating day of year
        sdate = splitted[0][6:8] + '-' + splitted[0][4:6] + '-' + splitted[0][0:4]
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = baseName + '_' + yymmdd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = baseName + '_' + yymmdd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = baseName + '_' + yymmdd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))

        '''
        '''
        ############################################################################################################
        #2nd Type of Naming convention in Lonnstorp i.e. 'SWE-LON-SFA-AGR-P02_2019-04-08_09-00-01'
        
        #Splitting the image file name to extract the year, month, day, hour, minute information
        splitted = oldimgName.split('_')
        baseName = splitted[0]
        yy = splitted[1].split('-')[0]
        mm = splitted[1].split('-')[1]
        dd = splitted[1].split('-')[2]
        hh = splitted[2].split('-')[0]
        minute = splitted[2].split('-')[1]
        
        #Concatenating ddmmyy for calculating day of year
        sdate = dd + '-' + mm + '-' + yy
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = baseName + '_' + yy + mm + dd + '_' + '00' + str(dayOfYear) + '_' + hh + minute + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = baseName + '_' + yy + mm + dd + '_' + '0' + str(dayOfYear) + '_' + hh + minute + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = baseName + '_' + yy + mm + dd + '_' + str(dayOfYear) + '_' + hh + minute + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        '''
        '''
        #############################################################################################################
        #3rd Type of Naming Convention in Lonnstorp i.e. 'SWE-LON-SFA-AGR-P02_2020-01-28T1000'
        
        #Remove the 'T' character from original image file name
        tRemoved = oldimgName.replace('T', '_')
        
        #Splitting the image file name based on '_' character
        splitted = tRemoved.split('_')
        
        #Extract the base name
        baseName = splitted[0]
        
        #Extract year, month, day, hour, minute information
        temp = splitted[1].split('-')
        yymmdd = ''.join(temp) #Join all strings from 'temp' list
        hhmm = splitted[2].split('.')[0]
        
        #Concatenating dd-mm-yy for calculating day of year
        sdate = temp[2] + '-' + temp[1] + '-' + temp[0]
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = baseName + '_' + yymmdd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = baseName + '_' + yymmdd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = baseName + '_' + yymmdd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        '''
        '''
        ##############################################################################################
        #Renaming Svartberget station .jpg files
        ##############################################################################################
        #Splitting the image file name to extract the year, month, day, hour, minute information
        splitted = oldimgName.split('T')
        yy = splitted[0][6:10]
        mm = splitted[0][11:13]
        dd = splitted[0][14:16]
        hhmm = splitted[1].split('.')[0]
        
        #Concatenating ddmmyy for calculating day of year
        sdate = dd + '-' + mm + '-' + yy
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = 'SWE-SVB-SVB-FOR-P01' + '_' + yy + mm + dd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = 'SWE-SVB-SVB-FOR-P01' + '_' + yy + mm + dd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = 'SWE-SVB-SVB-FOR-P01' + '_' + yy + mm + dd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        '''
        '''
        ##############################################################################################
        #Renaming Tarfala station .jpg files
        ##############################################################################################
        #Splitting the image file name to extract the year, month, day, hour, minute information
        splitted = oldimgName.split('_')
        yy = splitted[1].split('-')[0][0:4]
        mm = splitted[1].split('-')[0][4:6]
        dd = splitted[1].split('-')[0][6:8]
        hhmm = splitted[1].split('-')[1].split('.')[0]
        
        #Concatenating ddmmyy for calculating day of year
        sdate = dd + '-' + mm + '-' + yy
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = 'SWE-TRS-LAE-GRA-P01' + '_' + yy + mm + dd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = 'SWE-TRS-LAE-GRA-P01' + '_' + yy + mm + dd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = 'SWE-TRS-LAE-GRA-P01' + '_' + yy + mm + dd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        '''
        '''
        ##############################################################################################
        #Renaming Robacksdalen station .jpg files
        ##############################################################################################
        #Naming Convention that station follows i.e. 'SWE-RBD-RBD-AGR-P01_2019-04-11T1430'
        
        #Remove the 'T' character from original image file name
        tRemoved = oldimgName.replace('T', '_')
        
        #Splitting the image file name based on '_' character
        splitted = tRemoved.split('_')
        
        #Extract the base name
        baseName = splitted[0]
        
        #Extract year, month, day, hour, minute information
        temp = splitted[1].split('-')
        yymmdd = ''.join(temp) #Join all strings from 'temp' list
        hhmm = splitted[2].split('.')[0]
        
        #Concatenating dd-mm-yy for calculating day of year
        sdate = temp[2] + '-' + temp[1] + '-' + temp[0]
        
        #Converting date in string format to date format
        adate = datetime.datetime.strptime(sdate,"%d-%m-%Y")
        
        #Computing day of year information for each image based on date it was acquired
        dayOfYear = adate.timetuple().tm_yday
        
        if dayOfYear < 10:
            #Concatenating all variables to define the new file name for the images
            newimgName = baseName + '_' + yymmdd + '_' + '00' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        elif dayOfYear >= 10 and dayOfYear < 100:
            newimgName = baseName + '_' + yymmdd + '_' + '0' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
            
        else:
            newimgName = baseName + '_' + yymmdd + '_' + str(dayOfYear) + '_' + hhmm + '.jpg'
            os.rename(os.path.join(srcImgdir, oldimgName), os.path.join(srcImgdir, newimgName))
        '''
        
    #################################################################################################
    #################################################################################################

    print ('\n')
    print ('Images are renamed successfully as per the standards of SITES Spectral.')

    #################################################################################################