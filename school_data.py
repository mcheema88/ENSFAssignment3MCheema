# school_data.py
# Marley Cheema with provided code from ENSF 692 Dr. Sarah Shah. hh
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

years = ["2013" , "2014" , "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]

completeDataSet = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

completeDataSet = [year_XXXX.reshape(20,3) for year_XXXX in completeDataSet]

completeDataSet3D = []

for i in range(20):
    respectiveSchoolData = []
    for year_XXXX in completeDataSet:
        respectiveSchoolData.append(year_XXXX[i])
    completeDataSet3D.append(respectiveSchoolData)

completeDataSet3D = np.array(completeDataSet3D) #this is the complete data set.




#I am creating dictionaries for each year -> and there key will be a value corresponding to a specific depth in my 3D array

schoolNameList = ["Centennial High School", "Robert Thirsk School", "Louise Dean School",
                "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School",
                "Western Canada High School", "Central Memorial High School", "James Fowler High School",
                "Ernest Manning High School", "William Aberhart High School", "National Sport School",
                "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbook High School",
                "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School",
                "John G Diefenbaker High School", "Lester B. Pearson High School"]

schoolCodeList = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 9836, 9847, 9850, 9856,
                  9857, 9858, 9860, 9865]

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




def ThreeDimensionalArrayCreatorAndFormatter(TwoDimensionalArray):
    threeDimensionalArray = []
    for i in range(20):
        respectiveSchoolData = []
    for year_XXXX in TwoDimensionalArray:
        respectiveSchoolData.append(year_XXXX[i])
    threeDimensionalArray.append(respectiveSchoolData)
    threeDimensionalArray = np.array(threeDimensionalArray)
    return threeDimensionalArray



def totalEnrollmentPerYear(TwoDimensionalArray):
    totalEnrollmentList = []
    i = 0
    for row in TwoDimensionalArray:
        totalEnrollment = int(np.nansum(row))
        print("Total enrollment for", years[0],  ":" , totalEnrollment)
        i = i + 1
        totalEnrollmentList.append(totalEnrollment)
    
    totalEnrollmentList = np.array(totalEnrollmentList)
    return totalEnrollmentList

def medianFor500PlusEnrollments(TwoDimensionalArray):

    mask = TwoDimensionalArray > 500

    if TwoDimensionalArray[mask].any():
        print("For all enrollments over 500, the median value was: ", int(np.median(TwoDimensionalArray[mask])))
    else:
        print("No enrollments over 500.")


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
    

def main():

    print("ENSF 692 School Enrollment Statistics")

    print("Shape of full data array:  ", completeDataSet3D.shape)
    
    #print(completeDataSet3D) used this in the early stages, just to double check that I liked out my final 3D array looked like and values were correct

    print("Dimensions of full data array:  ", completeDataSet3D.ndim)

    # Print Stage 1 requirements here

    # Prompt for user input
    

    while True :
        schoolNameOrCode = input("Please enter the high school name or school code: ")
        if schoolNameOrCode.isdigit():
            schoolNameOrCode = int(schoolNameOrCode)
        if schoolNameOrCode in schoolAssignmentDictionaryDepth :
            break
        else :
            print("You must enter a valid school name or code")

    print("\n***Requested School Statistics***\n")

    #print(schoolCode)
    #print('\n')
    #print(schoolCodesData)

    #print("\n")
    #print(schoolAssignmentDictionaryDepth[schoolCode]) 

    inputDepth = int(schoolAssignmentDictionaryDepth[schoolNameOrCode])

    
    print("\nSchool Name: ", schoolNameList[inputDepth], ", School Code: ", schoolCodeList[inputDepth])

    schoolDataForInput = completeDataSet3D[inputDepth] #creation of a 2D array based on input

        # Print Stage 2 requirements here
   
    
    grade10EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,0]))
    grade11EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,1]))
    grade12EnrollmentMeanForInput = int(np.nanmean(schoolDataForInput[:,2]))


    print("Mean enrollment for Grade 10:  ", grade10EnrollmentMeanForInput)
    print("Mean enrollment for Grade 11:  ", grade11EnrollmentMeanForInput)
    print("Mean enrollment for Grade 12:  ", grade12EnrollmentMeanForInput)

    maxEnrollmentForInput = int(np.nanmax(schoolDataForInput))
    minEnrollmentForInput = int(np.nanmin(schoolDataForInput))

    print("Highest enrollment for a single grade:  ", maxEnrollmentForInput)
    print("Lowest enrollment for a single grade:  ", minEnrollmentForInput)

    #print statements baked into the method when call so no need -> simplified main dosent need 10 indiviudal print statements
    totalEnrollmentForInputArray = totalEnrollmentPerYear(schoolDataForInput)
    

    total10YearEnrollmentForInput = int(np.nansum(totalEnrollmentForInputArray))
    meanTotal10YearEnrollmentForInput = int(np.nanmean(totalEnrollmentForInputArray))
    

    print("Total ten year enrollment:  ", total10YearEnrollmentForInput )
    print("Mean total enrollment over 10 years:  ",meanTotal10YearEnrollmentForInput )
    
    medianFor500PlusEnrollmentsForInput = medianFor500PlusEnrollments(schoolDataForInput)


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    
    meanEnrollment2013 = int(np.nanmean(completeDataSet3D[:,0,:]))
    print("Mean enrollment for 2013:  ", meanEnrollment2013)

    meanEnrollment2022 = int(np.nanmean(completeDataSet3D[:,9,:]))
    print("Mean enrollment for 2022:  ", meanEnrollment2022)

    graduatingClassOf2022 = int(np.nansum(completeDataSet3D[:,9,2]))
    print("Total graduating class of 2022:  ", graduatingClassOf2022)

    highestEnrollmentInAnyGrade = int(np.nanmax(completeDataSet3D))
    print("Highest enrollment for a single grade:  ", highestEnrollmentInAnyGrade)

    lowestEnrollmentInAnyGrade = int(np.nanmin(completeDataSet))
    print("Lowest enrollment for a single grade:  ", lowestEnrollmentInAnyGrade)

if __name__ == '__main__':
    main()

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
