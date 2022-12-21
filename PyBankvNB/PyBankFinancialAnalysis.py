# files and dependencies

import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# find total months and total P/L...need to loop and count
months = []
net_total = []

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    
    for row in csv_reader:
        months.append(row[0])
        net_total.append(int(row[1]))
        month_count = len(months)
        total = sum(net_total)


# the changes in "P/L" month to month, then the average change 
# variables for loops
    x = 1
    y = 0

    average_change = (net_total[1]-net_total[0])
    changes = []

    for month in range(month_count-1):
        average_change = (net_total[x] - net_total[y])
        changes.append(int(average_change))
        x+=1
        y+=1
        print(changes)

    avg_mnthly_change = round(sum(changes)/(month_count -1),2)
    print(avg_mnthly_change)

# greatest increase & decrease (date and amount)
max_change = max(changes)
min_change = min(changes)
print(max_change)
print(min_change)

# find index for greatest inc/dec, then associated month
change_i_max = changes.index(max_change)
change_i_min = changes.index(min_change)
max_change_month = months[change_i_max + 1]
min_change_month = months[change_i_min + 1]
print(max_change_month)
print(min_change_month)


# print all values at once
print("PyBank Financial Analysis")
print("--------------------------------------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: ${avg_mnthly_change}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

    
#Write the output to a text file
PyBankFinAnalysis = open("PyBank_Financial_Analysis.txt","w")
 
PyBankFinAnalysis.write("PyBank_Financial Analysis\n")
PyBankFinAnalysis.write("--------------------------------------------\n")
PyBankFinAnalysis.write(f"Total Months: {len(months)}\n")
PyBankFinAnalysis.write(f"Total: ${sum(net_total)}\n")
PyBankFinAnalysis.write(f"Average Change: ${avg_mnthly_change}\n")
PyBankFinAnalysis.write(f"Greatest Increase in Profits: {max_change_month} (${max_change})\n")
PyBankFinAnalysis.write(f"Greatest Decrease in Profits: {min_change_month} (${min_change})\n")

PyBankFinAnalysis.close() 

  
