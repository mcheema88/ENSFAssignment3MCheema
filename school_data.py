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

# Okay first step I am taking is just opening all my data that I have access to
# We can manipulate and format it afterwards -> I just want it accesible to I can play with it

completeData = pd.read_csv('Assignment3Data.csv') 

# now because I am starting with schoolcode -> I want all the school codes as an array.
schoolCodesData = completeData['School Code'].to_numpy()
schoolNamesData = completeData['School Name'].to_numpy()



# You may add your own additional classes, functions, variables, etc.


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here

    # Prompt for user input
    

    while True :
        schoolCode = input("Please enter the high school name or school code: ")
        if schoolCode.isdigit():
            schoolCode = int(schoolCode)
        if schoolCode in schoolCodesData or schoolCode in schoolNamesData:
            break
        else :
            print("You must enter a valid school name or code")
    #print(schoolCode)
    #print('\n')
    #print(schoolCodesData)


    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

