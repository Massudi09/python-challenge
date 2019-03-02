# DISCLAIMER : I know this method isn't the best, but that's the way I understand it for the time being

import os
import csv

# path to gather data from
PyBankCSV = '/Users/zeinabmassudi/Desktop/budget_data (1).csv'

# Read in the CSV file
with open(PyBankCSV, 'r') as csvfile:

    # separate data by comma
    csvreader = csv.reader(csvfile, delimiter=',')
    # set and skip header
    header = next(csvreader)
    
    # Set values for Revenue total(Profits/Losses), Month and Average Change 
    revenue = 0
    rowsNum = 0 
    averageChange = 0
    
    #firstTime = True   

    # Parse through the data using for loop
    for i in csvreader:
        
        firstTime = True 
        if firstTime:
            previous = int(i[1])
            firstTime = False
        else:
            current = int(i[1])
            difference = current - previous
            averageChange += (difference/85)
            previous = current
        revenue += int(i[1])
        rowsNum += 1    

    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print (f"Total Months: {rowsNum}")
    print(f"Total: ${revenue}")
    print(f"Average Change: ${averageChange:.2F}")
    
with open(PyBankCSV) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  
    maxValue = max(csvreader, key=lambda column: int(column[1]))
    print("Greatest increase in Profits:" + str(maxValue).strip('[]'))

with open(PyBankCSV) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  
    minValue = min(csvreader, key=lambda column: int(column[1]))
    print("Greatest increase in Profits:" + str(minValue).strip('[]'))


with open("PyBank.txt","w") as out:

    line1 ="Financial Analysis"
    line2 = "---------------------------"
    line3 = f"Total Months: {rowsNum}"
    line4 = f"Total: ${revenue}"
    line5 = f"Average Change: ${averageChange:.2F}"
    line6 = "Greatest increase in Profits:" + str(maxValue).strip('[]')
    line7 = "Greatest increase in Profits:" + str(minValue).strip('[]')
    
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
    
