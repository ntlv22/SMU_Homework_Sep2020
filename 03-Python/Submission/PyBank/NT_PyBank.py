#import library
import os
import csv

#joining path
budget_data = r"03-Python/Submission/PyBank/Resources/budget_data.csv"

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    #print(f"Header: {csv_header}")

    # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenueChange = []

    for i in range(1, len(P)):
        revenueChange.append((int(P[i]) - int(P[i-1])))

    # calculate average revenue change
    revenueAverage = sum(revenueChange) / len(revenueChange)

    # calculate total length of months
    totalMonths = len(months)

    # greatest increase in revenue
    greatestIncrease = max(revenueChange)

    # greatest decrease in revenue
    greatestDecrease = min(revenueChange)

summaryString = f"""Finanical Analysis
-------------------------
Total Months: {totalMonths}
Total: ${str(sum(P))}
Average Change: ${round(revenueAverage, 2)}
Greatest Increase in Profits: {str(months[revenueChange.index(max(revenueChange))+1])} (${greatestIncrease})
Greatest Decrease in Profits: {str(months[revenueChange.index(min(revenueChange))+1])} (${greatestDecrease})
"""
print(summaryString)
#write summary string
with open("bank_results.txt", "w") as file1:
    file1.write(summaryString)