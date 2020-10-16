from imgRename_1 import imgRename_function
from removeDark_2 import removeDark_function
from timeFilter_3 import timeFilter_function
from dailyAVG_L2_4 import dailyAVG_L2_function
from snowThreshold_5 import snowThreshold_function
#from Oneday_summary_L3_ST_6 import Oneday_summary_L3_ST_function
from mergeAnnualCSV_7 import mergeAnnualCSV_function
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
    pathname = input("Enter pathname of where the images are stored:") 

    #changed to renaming typ Röbäcksdalen DONE
    if input("Do You Want To Continue with Renaming the images? [y/n]") == "y":
        imgRename_function(pathname)

    # removeDark path to Dark folder was changed for it to work for me, added counter to how many images were removed DONE
    if input("Do You Want To Continue with Removing Dark images? [y/n]") == "y":
        removeDark_function(pathname)
    '''
    #path to 10TO14 was changed for it to work for me, added counter, images are filtered in a new folder, but not removed from the original file. DONE MAYBE?
    if input("Do You Want To Continue with timeFilter? [y/n]") == "y":
        timeFilter_function(pathname)
'''
    #path to Temp and other folder was changed for it to work for me. DONE MAYBE?
    if input("Do You Want To Continue with Removing Calculating daily averages? [y/n]") == "y":
        dailyAVG_L2_function(pathname)
    
    #changed path, TypeError line 67 changed cv2.fillPoly, added counter,  seems like all pictures are removed and placed in snowy?
    if input("Do You Want To Continue with Removing snow? [y/n]") == "y":
        snowThreshold_function(pathname)
    
    #changed pathname and doy, not working atm,
    if input("Do You Want To Continue with Creating a 1-day summary? [y/n]") == "y":
        pathname2 = input("Enter pathname of where you would like to store the results of the one day summary:") 
        Oneday_summary_L3_ST_function(pathname2)

    #oneayday summary must work for this one to be able to work
    if input("Do You Want To Continue with merging Annual CSV? [y/n]") == "y":
        pathname3 = input("Enter path definition for .csv files:") 
        mergeAnnualCSV_function(pathname3)

    #oneayday summary must work for this one to be able to work
    if input("Do You Want To Continue with merging ROIcsv? [y/n]") == "y":
        mergeROIcsv_function
      
if __name__ == '__main__':
    main()