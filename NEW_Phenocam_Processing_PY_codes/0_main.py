from imgRename_1 import imgRename_function
from removeDark_2 import removeDark_function
from timeFilter_3 import timeFilter_function
from dailyAVG_L2_4 import dailyAVG_L2_function
#from snowThreshold_5 import snowThreshold_function
#from Oneday_summary_L3_ST_6 import Oneday_summary_L3_ST_function
#from mergeAnnualCSV_7 import mergeAnnualCSV_function
#from mergeROIcsv import mergeROIcsv_function

def main():

#There is also demand for being able
#to track the success of the processing: how many images were processed, how many were modified, by
#how much, for how many images did the processing fail, etc. All this needs to be reported.
#Furthermore, a way to flag images that need manual processing needs to be included. 
#Also, automaton of metadata in the form of quality flags telling the quality of the processed
#förslag: Ask for path as user input, call functions with path as parameter
#main method calling all phenocam processings-functions in order

    #made the individual classes into functions so that they could be called from this main-fuction.
    #In order to import the functions I had to renamame the classes since they could not start with a number.

    #Enter the pathname of where the images are stored
    pathname = input("Enter path") 

    #IndexError in imgRename, so had to change it for it to work for me, changes are documented in imgRename
    #if input("Do You Want To Continue with Renaming the images? [y/n]") == "y":
        #imgRename_function(pathname)

    # removeDark path to Dark folder was changed for it to work for me
    #if input("Do You Want To Continue with Removing Dark images? [y/n]") == "y":
        #removeDark_function(pathname)

    #path to 10TO14 was changed for it to work for me
    #if input("Do You Want To Continue with timeFilter? [y/n]") == "y":
        #timeFilter_function(pathname)

     #path to Temp was changed for it to work for me. IndexError when splitting doy.
    if input("Do You Want To Continue with Removing Calculating daily averages? [y/n]") == "y":
        dailyAVG_L2_function(pathname)

    #if input("Do You Want To Continue with Removing snow? [y/n]") == "y":
    #if input("Do You Want To Continue with Creating a 1-day summary? [y/n]") == "y":
        #Oneday_summary_L3_ST_function
    #if input("Do You Want To Continue with merging Annual CSV? [y/n]") == "y":
        #mergeAnnualCSV_function
    #if input("Do You Want To Continue with merging ROIcsv? [y/n]") == "y":
        #mergeROIcsv_function
        
if __name__ == '__main__':
    main()