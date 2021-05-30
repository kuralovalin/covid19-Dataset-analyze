#Probability and Statistics
# Alina Kuralova
# Covid Dataset Analyze 


import pandas as pd
import numpy as np
import statistics
import sys

# in order to write to a file


def write_file():
    with open('output.txt', 'w') as f:
        sys.stdout = f
        part1()
        f.close()


# Question 1
# lists all counties on the dataset
def part1():
    fileName = 'owid-covid-data.xlsx'
    df = pd.read_excel(fileName, sheet_name='Sheet1', usecols="C")
    states = df.to_numpy()
    #numpy.set_printoptions(threshold=sys.maxsize)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~ Probability and Statistics ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Homework # 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   Alina Kuralova ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   171044094 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print('\n ~~~~~~~ Question 1 ~~~~~~~ \n')
    print('Counties of the dataset:\n')
    for_parts=[]
    indeces=[]
    for i in range(len(states)):  # checks whether next word is equal or not
        if i+1 != len(states):
            if states[i] != states[i+1]:
                print(*states[i])            # prints accordingly
                for_parts.append(states[i])
                indeces.append(i)
    print(*states[i])
    for_parts.append(states[i])
    indeces.append(i)
    print("In TOTAL ---> ", len(for_parts), "Countries")
    #part 2
    part2(states,fileName)
    
    #part 3
    print('\n ~~~~~~~ Question 3 ~~~~~~~ \n')
    print('How many cases are confirmed for each country so far?:\n')
    part11(for_parts, indeces, "E", fileName)
    
    #part 4
    print('\n ~~~~~~~ Question 4 ~~~~~~~ \n')
    print('Total death confirmed for each country so far:\n')
    part11(for_parts, indeces, "H", fileName)

    # part 5
    print('\n ~~~~~~~ Question 5 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the reproduction rates for each country?\n")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 

    part5_13(for_parts, indeces, "Q",fileName)

    # part 6
    print('\n ~~~~~~~ Question 6 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the icu patients\n" )
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "R", fileName)

    # part 7
    print('\n ~~~~~~~ Question 7 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the hosp patients\n ")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "T",fileName)

    # part 8
    print('\n ~~~~~~~ Question 8 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the weekly icu\n ")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "V",fileName)

    # part 9
    print('\n ~~~~~~~ Question 9 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the weekly hospital admissions for each ecounty?\n")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "X",fileName)

    # part 10
    print('\n ~~~~~~~ Question 10 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of new tests per day for each country?\n")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "Z",fileName)

    # part 11
    print('\n ~~~~~~~ Question 11 ~~~~~~~ \n')
    print('Total tests conducted for each country so far:\n')
    part11(for_parts, indeces, "AA",fileName)

    #part12
    print('\n ~~~~~~~ Question 12 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the positive rates of the tests for each country?\n")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "AF",fileName)

    #part 13
    print('\n ~~~~~~~ Question 13 ~~~~~~~ \n')
    print("What are the average, minimum, maximum and variation values of the tests per case for each country?\n")
    print("Country ------ Min ----- Max ------ Average ------ Variation ") 
    part5_13(for_parts, indeces, "AG",fileName)

    #part 14
    print('\n ~~~~~~~ Question 14 ~~~~~~~ \n')
    print('Vaccinated by at least one dose:\n')
    part11(for_parts, indeces, "AJ",fileName)

    #part 15

    print('\n ~~~~~~~ Question 15 ~~~~~~~ \n')
    print('Fully vaccinated :\n')
    part11(for_parts, indeces, "AK",fileName)

    #part 16
    print('\n ~~~~~~~ Question 16 ~~~~~~~ \n')
    print('How many vaccinations are administered in each country so far?:\n')
    part11(for_parts, indeces, "AI",fileName) 

# Question 2
def part2(states,fileName):
    df = pd.read_excel(fileName, sheet_name='Sheet1', usecols="D")
    dates = df.to_numpy()
    print('\n ~~~~~~~ Question 2 ~~~~~~~ \n')  
    dates = dates.tolist()
    oldest = min(dates)
    index = dates.index(oldest)
    country = states[index]
    print('Earliest date data in dataset:\n')
    print(*(country + ' --> ' + oldest))     


def part11(for_part4, indeces4, coll,fileName):
    df = pd.read_excel(fileName, sheet_name='Sheet1', usecols=coll)
    soFar = df.to_numpy()
    df = pd.DataFrame(soFar)
    df = df.fillna(-1)
    soFar = df.to_numpy()
    j=0
    arrCheck = []
    for i in range(len(soFar)): 
        if i+1 != len(soFar):
            if i < indeces4[j] and soFar[i] != -1:
                arrCheck.append(soFar[i])

            if i == indeces4[j] and soFar[i] != -1:
                arrCheck.append(soFar[i])
                total = max(arrCheck, default="EMPTY")
                print(*(for_part4[j] + ' -->'), total)
                arrCheck.clear()
                j += 1
            if i == indeces4[j] and soFar[i] == -1:
                total = max(arrCheck, default="EMPTY")
                print(*(for_part4[j] + ' -->'), total)
                arrCheck.clear()
                j += 1

    if i == indeces4[j] and soFar[i] != -1:
        arrCheck.append(soFar[i])
        total = max(arrCheck, default="EMPTY")
        print(*(for_part4[j] + ' -->'), total)
        arrCheck.clear()
    if i == indeces4[j] and soFar[i] == -1:
        total = max(arrCheck, default="EMPTY")
        print(*(for_part4[j] + ' -->'), total)
        arrCheck.clear()


        


# Question 5
def part5_13(for_part5, indeces5, col,fileName):
    df = pd.read_excel(fileName, sheet_name='Sheet1', usecols=col) 
    dataset = df.to_numpy()

    df = pd.DataFrame(dataset)
    df = df.fillna(-1)
    toWork = df.to_numpy()
  
    sum=0
    temp_arr=[]
    j=0
    for i in range(len(toWork)):
        if i+1 != len(toWork):
          
            if i < indeces5[j] and toWork[i] != -1:

                sum = sum + toWork[i]
                temp_arr.append(toWork[i])

            if i == indeces5[j] and toWork[i] != -1:
                sum = sum + toWork[i]
                temp_arr.append(toWork[i])

                min_repod = min(temp_arr, default="EMPTY")
                max_repod = max(temp_arr, default="EMPTY")

                if len(temp_arr) != 0:          #error check
                    ave_repod = sum / len(temp_arr)
                    if len(temp_arr) > 1:
                        dataVar = map(int, temp_arr)
                        variation = statistics.variance(dataVar)
                print(*(for_part5[j] + "   "), min_repod, "   ", max_repod, "   ", ave_repod, "   ", variation )     
            

                temp_arr.clear()

                j += 1
                sum = 0

            if i == indeces5[j] and toWork[i] == -1:
                if sum != 0:            #error check
                    min_repod = min(temp_arr, default="EMPTY")
                    max_repod = max(temp_arr, default="EMPTY")

                    if len(temp_arr) != 0:
                        ave_repod = sum / len(temp_arr)
                        if len(temp_arr) > 1:
                            dataVar = map(int, temp_arr)
                            variation = statistics.variance(dataVar)
                    
                    print(*(for_part5[j] + "   "), min_repod, "   ", max_repod, "   ", ave_repod, "   ", variation ) 
                

                temp_arr.clear()
                j += 1
                sum = 0


    if i == indeces5[j] and toWork[i] == -1:
        if sum != 0:
            min_repod = min(temp_arr, default="EMPTY")
            max_repod = max(temp_arr, default="EMPTY")

            if len(temp_arr) != 0:
                ave_repod = sum / len(temp_arr)
                if len(temp_arr) > 1:
                    dataVar = map(int, temp_arr) 
                    variation = statistics.variance(dataVar)
            print(*(for_part5[j] + "   "), min_repod, "   ", max_repod, "   ", ave_repod, "   ", variation  ) 
        
        temp_arr.clear()



    if i == indeces5[j] and toWork[i] != -1:
        sum = sum + toWork[i]
        temp_arr.append(toWork[i])

        min_repod = min(temp_arr, default="EMPTY")
        max_repod = max(temp_arr, default="EMPTY")
        if len(temp_arr) != 0:
            ave_repod = sum / len(temp_arr) 
            if len(temp_arr) > 1:
                dataVar = map(int, temp_arr)     
                variation = statistics.variance(dataVar)
        print(*(for_part5[j] + "   "), min_repod, "   ", max_repod, "   ", ave_repod, "   ", variation  ) 



# Driver Code
# Question 1
write_file()















