# school_data.py
# 
# Author: Marley Cheema with provided code and from ENSF 692 Dr. Sarah Shah.
# Since: June 3rd 2022
# Version 1.0 with many iterations during dev
# Reference to chatgpt for debugging, learning about new cool things in python that could be applicable, and especially with errors and helping find mistakes when outputs were wrong
# this was especially helpful at creating a 3D array in the shape that I wanted as this was my first time using 3D arrays and for inspiration
# however chatGPT was not used for any code generation nor were any specific prompts or data ever given, and the structure and logic is my own.

#really enjoyed this assignment -> I went to William Aberhart and graduated in 2019!! So super cool to be apart of the data in a small way (: ) -> I also love data analysis, right in my wheelhouse !!
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

#This variable was one I created to help simplify print statements throughout the file, and can be seen within "totalEnrollmentPerYear" method.
years = ["2013" , "2014" , "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

#this an initial creation of a variable encompassing all the provided data, as each array within it, is a 1D array with 60 values, this effectively creates an extended list of 1D arrays)
completeDataSet = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

#as completeDataSet is still a list, what this does is reshape each array within the list (year_XXXX), from a 1D array to a 2D array with 20 rows and 3 columns executed and seen through the .reshape function of numpy
completeDataSet = [year_XXXX.reshape(20,3) for year_XXXX in completeDataSet]

#next is an initialization of an empty list which will ultimately serve as the building block for my 3D array which will be used for all analysis.
completeDataSet3D = []

#what this code does is essentially replicates the Assignment3Data.csv format of how the data is presented and creates a 3D list
#this was completed in this manner as originally I had used readcsv through pandas and had my data in this format.
#throughout dev I realized that it was suggested to only use the given_data.py and not the csv, however I still really liked
#the formatting in the csv so I decided to create a 3D array in a similar format from the given_data, ultimately segmenting the 1 dimension of 3
#through seperating data by each schools reflected by depth, then the rows reflect each year and the columns reflect each grade.
for i in range(20): #note I wanted to build a function to do this but found based on declaration order difficult to do so -> a function for this can be seen at the bottom of unused code.
    respectiveSchoolData = []
    for year_XXXX in completeDataSet:
        respectiveSchoolData.append(year_XXXX[i])
    completeDataSet3D.append(respectiveSchoolData)

#this is the most critical variable of all my data -> it's order and arrangement is crucial and is used and referenced in
# the creation of all subsequent variables, with the indexing of the depth of the array corresponding to each school is critical
completeDataSet3D = np.array(completeDataSet3D) #final step turning completeDataSet3D into a true 3 dimensional numpy array with a shape of (20: each school, 10: each year, 3: each grade)

#This is a creation of a list encompassing the names of each school -> the order is critical as it matches and alligns with completeDataSet3D first index, it's depth
schoolNameList = ["Centennial High School", "Robert Thirsk School", "Louise Dean School",
                "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School",
                "Western Canada High School", "Central Memorial High School", "James Fowler High School",
                "Ernest Manning High School", "William Aberhart High School", "National Sport School",
                "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbook High School",
                "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School",
                "John G Diefenbaker High School", "Lester B. Pearson High School"]

#This is the creation of a list encompassing the codes of each school -> it's indexing matches perfectly to schoolNameList -> so the index of each field within that list matches to this list.
schoolCodeList = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 9836, 9847, 9850, 9856,
                  9857, 9858, 9860, 9865]

#This is the creation of the DICTIONARY, and is very critical aspect of the main code
#This dictionary functions to actually make sense of the user input, as the user input matches to key and will be able to output
# a code/result, in this case the output pertains to being able to correctly indexing the completeDataSet3D and access the data within
# the array that pertains to the school that the user wants to see statitics for
#all logic of the code is based off being able to identify the first layer of the completeDataSet3D matrix and the using that data which can occur through this dictionary.
schoolAssignmentDictionaryDepth = { "Centennial High School" : 0, 1224 : 0, 
                                    "Robert Thirsk School" : 1, 1679 : 1,
                                    "Louise Dean School" : 2, 9626 : 2,
                                    "Queen Elizabeth High School" : 3, 9806 : 3, 
                                    "Forest Lawn High School" : 4, 9813 : 4,
                                    "Crescent Heights High School" : 5, 9815 : 5,
                                    "Western Canada High School" : 6, 9816 : 6,
                                    "Central Memorial High School" : 7, 9823 : 7,
                                    "James Fowler High School" : 8, 9825 : 8,
                                    "Ernest Manning High School" : 9, 9826 : 9,
                                    "William Aberhart High School" : 10, 9829 : 10,
                                    "National Sport School" : 11, 9830 : 11,
                                    "Henry Wise Wood High School" : 12, 9836 : 12,
                                    "Bowness High School" : 13, 9847 : 13,
                                    "Lord Beaverbook High School" : 14, 9850: 14,
                                    "Jack James High School" : 15, 9856 : 15,
                                    "Sir Winston Churchill High School" : 16, 9857 : 16,
                                    "Dr. E. P. Scarlett High School" : 17, 9858 : 17,
                                    "John G Diefenbaker High School" : 18, 9860 : 18,
                                    "Lester B. Pearson High School" : 19, 9865 : 19}


#METHODS

#This method serves a specific purpose to return the total enrollment for each year of the given data 2013-2022 for a specific school
#this helps clean up the main and uses a for loop through each row to calculate the enrollment across all 3 grades along with integrating print statements

#@parameters: The paramter for this method is 2D array -> this should be a subset of the completeDataSet3D which uses the index pick a specific depth of the 3D array which correspond 
#to the years data of the specific school of interest

#@return this method returns a list of the length of # of rows of the input array which contains the sum of students for each year for a specific school
#however because this method has print statements within it which execute as soon as the method is called, the return is not crucial but nice to have, and I actually use it in future summations for other requirements to minimize computation but again not critical
#in case it wants to be acessed later.

def totalEnrollmentPerYear(TwoDimensionalArray):
    totalEnrollmentList = []
    i = 0 #this is used to track and index the global variable of the years list so that the correct year is printed
    for row in TwoDimensionalArray:
        totalEnrollment = int(np.nansum(row)) #using the builtin numpy nansum to summarize each row which corresponds to total enrollment of the year for a school based on how my matrices are set up for this assignment.
        print("Total enrollment for", years[0],  ":" , totalEnrollment) #print statement that uses the years list baked within to simplify print statements and allow it to be done within the loop.
        i = i + 1 #increasing i so that the next summation prints the next year and everything matches perfectly.
        totalEnrollmentList.append(totalEnrollment)
    
    totalEnrollmentList = np.array(totalEnrollmentList) #not critical but nice to have
    return totalEnrollmentList #again not critical but nice to have


#This method serves a specific purpose for one of the requirements of the code, to check each grade over all the years for data from a specific
#school and determine whether or not there are 500 students, and then to find the median grade size of all the grades with over 500 student enrolled
#this method uses as MASK which evaluates components of an array through a booleans to essentially build a filter which can be analyzed through numpy computational functions.

#the parameter of this array is a 2D array which should represent all the data for a specific school of interest including years as rows and grades as columns
#this is intended to be sub array of the completeDataSet3D, which isolates a certain depth which corresponds to a school

#the return of this function can be seen as a void in terms of a specific variable, instead the purpose of this function to execute one of two potential print statements, 
# one that either indicates the median value for grades with over 500 students or let the user know that there are no grades with an enrollment of over 500 students.
def medianFor500PlusEnrollments(TwoDimensionalArray):

    mask = TwoDimensionalArray > 500 #creation of the mask which stores the indexes that evaluates for true

    if TwoDimensionalArray[mask].any(): #what this does is determine if there are any indexes stored which means there are values greater than 500
        print("For all enrollments over 500, the median value was: ", int(np.median(TwoDimensionalArray[mask]))) #evaluating for the median of all the values within the array greater than 500 through using the mask as the index
    else: #if this is else it means no values within the inputted array is over 500 -> hence the need for this statement
        print("No enrollments over 500.")

#Main part of the code where all the execution occurs along with the ability to get the user's input

def main():

    #print statement depicting the overview of the program to the user
    print("ENSF 692 School Enrollment Statistics")

    #printing the shape of the 3D array that is the basis of all analysis and was created by me as an instance variable
    print("Shape of full data array:  ", completeDataSet3D.shape)
    
    #print(completeDataSet3D) used this in the early stages, just to double check that I liked out my final 3D array looked like and values were correct

    #Printing the dimensions of the array (i.e how many dimensions it has) through the .ndim function of numpy.
    print("Dimensions of full data array:  ", completeDataSet3D.ndim)

    # Print Stage 1 requirements here
    # Prompt for user input
    
    #How I am prompting the user for input I decided to use a while loop, which will continue to run until an input that is acceptable is given from the user
    while True :

        #input statement which is stored is schoolNameOrCode as either can be entered
        schoolNameOrCode = input("Please enter the high school name or school code: ")
        
        #first check, as all inputs become strings, this is to check if only digits are entered through .isdigit() and converting it to an int
        if schoolNameOrCode.isdigit():
            schoolNameOrCode = int(schoolNameOrCode) #conversion to int so it can be compared
        
        #second if statement, and ultimately how you exit the loop, as both codes and names of schools are in my dictionary
        #and both point to the same index if either are entered and a part of my dictionary it means an acceptable input is put in.
        if schoolNameOrCode in schoolAssignmentDictionaryDepth :
            break
       
       #so if we get to the else it means the user inputted something not apart of the dictionary, and is not a correct input of a school name or code
       #so instead we print the appropriate message
       #now I decided not to do a ValueError as it makes my main more complex unneccesarily and this serves the exact same functionality
       #however a try: and the beggining of the loop a raise ValueError("message"), along with an except ValueError at the end would be the way to do so.
        else :
            print("You must enter a valid school name or code")

    #now we move to the specific school stats based on the user input and computation
    print("\n***Requested School Statistics***\n")

    #as configured intentionally both a school name and its corresponding code point to the same value which strategically represents an index in my created final 3D matrix of all the data
    #this is now simply storing that index to be used for accessing and creating a specific subarray of just the specific school data of interest from the suer
    inputDepth = int(schoolAssignmentDictionaryDepth[schoolNameOrCode])

    #Additionally strategically this index also corresponds to both the same school and code in both my schoolCodeList and schoolNameList, this way they both can be outputted based on the assignment requirements
    print("\nSchool Name: ", schoolNameList[inputDepth], ", School Code: ", schoolCodeList[inputDepth])

    #Now I am officially creating my officially subarray which is the schooldata for the user input
    #as in my 3D array having a shape of (20, 10, 3), the first index of the 3Darray which I refer to as the depth
    #represents each respective school, so by calling from the completeDataSet3D I effectively have a sub array which is only 2D and encompasses the school data
    schoolDataForInput = completeDataSet3D[inputDepth] #creation of a 2D array, and this array will be used for the rest of the specific school stats, it has 10 rows representing each year and 3 columns which represent each grade.

    #as this is a numpy array I can use nanmean (which accounts for nans), to generate the mean enrollment for each grade across years
    #this is achieved by also strategically calling the respective column which is reprsented from the second index, 0 = grade 10 (the first column), 1 = grade 11 and 2 = grade 12
    # using : it just means to account for the values in all the rows, which represents all the years.
    grade10EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,0]))
    grade11EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,1]))
    grade12EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,2]))

    #print statements for the variables above, this technically could all be in 1 line, without the creation of the variables, but I like to do it better this way -> cleaner and more methodical
    print("Mean enrollment for Grade 10:  ", grade10EnrollmentMeanForInput)
    print("Mean enrollment for Grade 11:  ", grade11EnrollmentMeanForInput)
    print("Mean enrollment for Grade 12:  ", grade12EnrollmentMeanForInput)

    #next is determining the max and min enrollment numbers across any year and any grade for the respective school
    #so this is quite simple, I just have to call my entire subarray which is 2D and has all the respective school data and use np.nanmax and np.nanmin as these are numpy arrays
    maxEnrollmentForInput = int(np.nanmax(schoolDataForInput))
    minEnrollmentForInput = int(np.nanmin(schoolDataForInput))

    #print statements again after the creation of the variable, because I like doing it better this way!
    print("Highest enrollment for a single grade:  ", maxEnrollmentForInput)
    print("Lowest enrollment for a single grade:  ", minEnrollmentForInput)

    #This calling the method I explained above outside the main just to clean up the main - can check that comments above this method for explanation of what it does
    # print statements baked into the method when call so no need -> simplified main dosent need 10 indiviudal print statements
    totalEnrollmentForInputArray = totalEnrollmentPerYear(schoolDataForInput) #key is that it is my subarray which is only 2D as the input and the method is designed for this array
    
    #as additionally my totalEnrollmentPerYear method returns an array of each the total enrollment for each year for the respective school
    #I can simply sum this array which I stored above as a variable using np.nansum as it is easier on computation of the code, but I also could just np.nansum my entire subarray for the school - schoolDataForInput
    total10YearEnrollmentForInput = int(np.nansum(totalEnrollmentForInputArray))
    #same thing with the mean, I can use np.mean to find the mean enrollment using the my already computed array, but additionally i could np.mean on my entire subbrarry as well and get the same result -> just thought 
    #this prevents excess computation
    meanTotal10YearEnrollmentForInput = int(np.nanmean(totalEnrollmentForInputArray))
    
    #printing these respective variables afterwards nice and cleanly
    print("Total ten year enrollment:  ", total10YearEnrollmentForInput )
    print("Mean total enrollment over 10 years:  ",meanTotal10YearEnrollmentForInput )
    
    #lastly calling upon my method I created outside the main to determine the median value for the school in grades with over 500 enrolled across all the year for the respective school
    #please check comments above that method for explanation -> masks are used on my data and the input is my 2D subbarray which encompasses the input school data
    #print statements baked into the function.
    medianFor500PlusEnrollmentsForInput = medianFor500PlusEnrollments(schoolDataForInput)



    # Print Stage 3 requirements here
    #Now we are looking at general statistics, so the user input is absolete, just my final created 3D array completeDataSet3D is used
    #and by doing some intentional splicing based on knowledge of my array which of course created based on specific specifications this portion was quite easy
    #based on built computational functions for numpy arrays
    print("\n***General Statistics for All Schools***\n")
    
    #to find the mean enrollment avross all schools in 2013, the first index is for my completeDataSet3D : which means to evaluate every school stored through depth
    #next that is followed by a 0 which means to only look at the first row for each depth and represents 2013 as intended - we want only 2013 mean, and again followed by a 
    # : for the 3rd index of my 3D array which means to look across all grades for the year, and of course using np.nanmean to get the mean of these values of the array we are identifying
    #this is followed by a print statement
    meanEnrollment2013 = int(np.nanmean(completeDataSet3D[:,0,:]))
    print("Mean enrollment for 2013:  ", meanEnrollment2013)

    #this is almost identical logic as 2013 expect the second index for my 3D array is 9 instead of 0 which means to only look at the 10 row for each school representing
    # 2022, and then of course calculating the mean through np.nanmean and printing the output
    meanEnrollment2022 = int(np.nanmean(completeDataSet3D[:,9,:]))
    print("Mean enrollment for 2022:  ", meanEnrollment2022)

    #to find how many student graduated in 2022 I had to go into my 3D array and pull data from each school so the first index is :
    #the second index is 9 which means to pull values from only the 10th row - 2022 and than finally only the third column representing grade through indexing the 3rd spot as 2.
    #than finally to sum all these values which are given through the splicing from the completeDataSet followed by a print statement
    graduatingClassOf2022 = int(np.nansum(completeDataSet3D[:,9,2]))
    print("Total graduating class of 2022:  ", graduatingClassOf2022)

    #This one was straight forward, to find the highest enrollment across all school, all grades and all years, the full 3D set can have the np.nanmax function applied to it
    #this outputs the highest value in the entire array representing the highest enrollment #
    highestEnrollmentInAnyGrade = int(np.nanmax(completeDataSet3D))
    print("Highest enrollment for a single grade:  ", highestEnrollmentInAnyGrade)

    #almost identical logic as above expect for min!
    lowestEnrollmentInAnyGrade = int(np.nanmin(completeDataSet))
    print("Lowest enrollment for a single grade:  ", lowestEnrollmentInAnyGrade)

if __name__ == '__main__':
    main()






#UNUSED/REPLACED CODE -> EARLY ITERATIONS (keeping for continuit/reference)


#Unused/replaced code based on iterative process, wanting to improve segments and ensuring all requirements are met
#however this all also works.


# # Okay first step I am taking is just opening all my data that I have access to
# # We can manipulate and format it afterwards -> I just want it accesible to I can play with it

# completeData = pd.read_csv('Assignment3Data.csv') 

# # now because I am starting with schoolcode -> I want all the school codes as an array.
# schoolCodesData = completeData['School Code'].to_numpy()
# #I also have to check against School Names, so want to store them into an array of their own.
# schoolNamesData = completeData['School Name'].to_numpy()



# # You may add your own additional classes, functions, variables, etc.

# #Okay time to create the 3D array

# completeDataArray = completeData.to_numpy()

# #okay after printing this shape in the main I have realized that it is 2D -> 200 by 10 -> this dosent make sense
# # as there is only 6 columns of useful info -> have to drop the last 4 columns

# completeDataArrayPolished = np.delete(completeDataArray, [6, 7, 8, 9], axis=1)

# #okay sweet after my print statement, it looks good and only has the useful info, now I can move on

# # Now that my data is polished:
# # I want my 3D component to seperate into groups of 10 -> seperating each school's data into it's own layer
# # this will help make analysis easy

# completeDataArrayPolished3D = completeDataArrayPolished.reshape(20, 10, 6)

# def medianFor500PlusEnrollments(TwoDimensionalArray): 

#     EnrollmentClassesWith500Students = []
    
#     for row in TwoDimensionalArray:
#         for val in row:
#             if val > 500:
#                 EnrollmentClassesWith500Students.append(val)
    
#     EnrollmentClassesWith500Students = np.array(EnrollmentClassesWith500Students)

#     if EnrollmentClassesWith500Students.size == 0:
#         outputStatement = "No enrollments over 500."
#         return outputStatement
#     else:
#         return np.median(EnrollmentClassesWith500Students)


# def ThreeDimensionalArrayCreatorAndFormatter(TwoDimensionalArray):
#     threeDimensionalArray = []
#     for i in range(20):
#         respectiveSchoolData = []
#     for year_XXXX in TwoDimensionalArray:
#         respectiveSchoolData.append(year_XXXX[i])
#     threeDimensionalArray.append(respectiveSchoolData)
#     threeDimensionalArray = np.array(threeDimensionalArray)
#     return threeDimensionalArray

