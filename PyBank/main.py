# Create files across operating systems
import os
# Module for reading csv files
import csv

# Create variables
total_months = 0
total_rev = 0 # Total revenue for period
prior_month_rev = 0 # Prior month's revenue
this_month_rev = 0 # This month's revenue
revenue_change = 0
revenue_changes = []
months = []

csvpath = os.path.join("..", "PyBank", "budget_data.csv")



# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # find monthly changes in revenue
    for row in csvreader:
        total_months = total_months + 1
        months.append(row[0])
        this_month_rev = int(row[1])
        total_rev = total_rev + this_month_rev
        if total_months > 1:
            revenue_change = this_month_rev - prior_month_rev
            revenue_changes.append(revenue_change)
        prior_month_rev = this_month_rev

# find monthly results
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (total_months - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# print summary
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: $ {total_rev}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

# save txt summary
with open("PyBankResults.txt", "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Total Months: {total_months}" + "\n")
    text.write(f"Total Revenue: ${total_rev}" +"\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")




            
