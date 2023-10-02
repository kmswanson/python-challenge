import csv
import os

budget_data = os.path.join("..","Resources","budget_data.csv")
#import data from 'budget_data.csv from resources folder

totalMonths = 0
totalProfitLosses = 0
previousProfitLoss = 0
changes = []
greatestIncrease = ["", 0]
greatestDecrease = ["", 0]
#declare variables and assign values for initial value
#call on the variables and the values stored in the end for output


# 'r'ead the csv file
with open("budget_data.csv", "r") as file:
    csvReader = csv.reader(file)
    
    header = next(csvReader)
    #use to bypass row 1 with header information
    
    for row in csvReader:
        date = row[0]
        profitLoss = int(row[1])
        # use to get the date and profit/loss values from the row
        
        totalProfitLosses += profitLoss
        # calculate the total profit or loss and store the values in profitLoss
        
        if previousProfitLoss != 0:
            change = profitLoss - previousProfitLoss
            changes.append(change)
        #calculate the change in profit/loss and append it to the list
        
            if change > greatestIncrease[1]:
                greatestIncrease[0] = date
                greatestIncrease[1] = change
            #update greatestIncrease value 
            elif change < greatestDecrease[1]:
                greatestDecrease[0] = date
                greatestDecrease[1] = change
            #update greatestDecrease value
        
        previousProfitLoss = profitLoss
        #update the value of previousProfitLoss, initialized at 0 for the next loop
        
        totalMonths += 1
        #counts the total number of months (header row bypassed on line 22)

averageChange = sum(changes) / len(changes)
#average of the changes over the entire period for profit/loss


# prints the results in terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfitLosses}")
print(f"Average Change: ${averageChange:.2f}")
#round the averageChange to two decimal points
print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
#print the results greatestIncrease[0] (date) and greatestIncrease[1] (profit/loss)
print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")
#print the results greatestDecrease[0] (date) and greatestIncrease[1] (profit/loss)


# use the 'w'rite output to save the results to an external .txt file in the same folder
with open("financialAnalysis.txt", "w") as outputFile:
    outputFile.write("Financial Analysis\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Total Months: {totalMonths}\n")
    outputFile.write(f"Total: ${totalProfitLosses}\n")
    outputFile.write(f"Average Change: ${averageChange:.2f}\n")
    outputFile.write(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\n")
    outputFile.write(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n")
    #\n to print to a new line
