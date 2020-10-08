"""
Created on Tue Sep  1 10:26:43 2020
This python script merges the annual .csv file that contains the time series of GCC & RCC.
@author: Shangharsha
"""

#################################################################################################
#Module Declaration
#################################################################################################

import pandas as pd
import glob
import os

def mergeAnnualCSV_function():
    #################################################################################################
    #Folder path definition for .csv files
    thePath = r'E:\Internship\Final\Abisko\L3\ROI1\all'

    #List out all the .csv files in the defined path
    all_files = glob.glob(thePath + "/*.csv")

    #################################################################################################
    #Empty list to store each .csv file as a dataframe
    tempList = []

    count = 0
    #Iterating through the .csv files in defined path
    for filename in all_files:
        
        #Read the base name of files
        baseName = os.path.basename(filename).split('_')[0]
        
        #Read all the .csv file
        df = pd.read_csv(filename, index_col=None, header=0)
        
        if count == 0:
            #Extract the first 'TimeStamp' from the dataframe
            #startDate = datetime.datetime.strptime(df['Timestamp'].iloc[0], "%m/%d/%Y").strftime("%Y-%m-%d")
            startDate = df['TIMESTAMP'].iloc[2].replace('-', '')
            
            #Append the 1st dataframe to the list
            tempList.append(df)
        
        else:
            #Delete row at index position 0 & 1
            dfMod = df.drop([df.index[0] , df.index[1]])
            
            #Append the dataframe to the empty list
            tempList.append(dfMod)
            
        count += 1
        
    #################################################################################################
        
    #Extract the last 'Timestamp' from the last dataframe
    #endDate = datetime.datetime.strptime(df['Timestamp'].iloc[-1], "%m/%d/%Y").strftime("%Y-%m-%d")
    endDate = df['TIMESTAMP'].iloc[-1].replace('-', '')

    #Concatenate all the dataframe in a list to a single combined dataframedf
    frame = pd.concat(tempList, axis=0, ignore_index=True) #axis=0 means appending to the end 

    #Station Name and Location
    stn = baseName.split('-')[1]
    loc = baseName.split('-')[2]
    camNo = baseName.split('-')[-1]

    #Define folder path to save the merged dataframe
    savePath = thePath + '\\' + 'SITES_' + camNo + '-' + 'GCC-RCC_' + stn + '_' + loc + '_' + startDate + '-' + endDate + '_' + 'L3_daily.csv'

    #Export the merged dataframe as a .csv file
    frame.to_csv(savePath, index = False)

    #################################################################################################
    #################################################################################################