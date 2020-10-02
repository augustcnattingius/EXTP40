"""
Created on Tue Sep  1 11:35:12 2020
This python script merges the level 3 .csv file for multiple regions of interest.
@author: Shangharsha
"""

#################################################################################################
#Module Declaration
#################################################################################################

import pandas as pd
import glob
import os

#################################################################################################

#Folder path definition for .csv files
thePath = r'E:\Internship\Final\Abisko\L3'

#List out all the .csv files in the file path
all_files = glob.glob(thePath + "/*.csv")

#################################################################################################
#Empty list to store each .csv file as a dataframe
tempList = []

count = 0
#Iterating through the .csv files in defined path
for filename in all_files:
    
    #Read the base name of files
    baseName = os.path.basename(filename).split('_')[0]
    
    if count == 0:
        
        #Read first .csv file
        df = pd.read_csv(filename, index_col=None, header=0)
    
        #Extract the first 'TimeStamp' from the dataframe
        #startDate = datetime.datetime.strptime(df['Timestamp'].iloc[0], "%m/%d/%Y").strftime("%Y-%m-%d")
        startDate = df['TIMESTAMP'].iloc[2].replace('-', '')
        
        #Append all the dataframe to the empty list
        tempList.append(df)
    
    else:
        
        #Read the remaining .csv file
        df = pd.read_csv(filename, index_col=None, header=0)
        
        #Extract all the columns except the first two columns as a separate dataframe
        df2 = df[df.columns[3:]]
        #df2 = df[df.columns[2:]] #ONLY FOR ABISKO
        
        #Append all the dataframe to the empty list
        tempList.append(df2)
        
    count += 1
    
#################################################################################################
    
#Extract the last 'Timestamp' from the last dataframe
#endDate = datetime.datetime.strptime(df['Timestamp'].iloc[-1], "%m/%d/%Y").strftime("%Y-%m-%d")
endDate = df['TIMESTAMP'].iloc[-1].replace('-', '')

#Concatenate all the dataframe in a list to a single combined dataframedf
frame = pd.concat(tempList, axis=1) #axis=1 means column wise appending 

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
