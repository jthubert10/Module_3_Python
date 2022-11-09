# Import CSV module
import csv

# Establish path to CSV file
import_path = 'Z:/TCC_Data_Analytics/Module_3_Python/PyBank/Resources/budget_data.csv'

# Establish variables
months_list = []
change_list = []
total_months = 0
total_profit_loss = 0
previous_month_change = 0
current_month_change = 0
profit_loss_change = 0


# Open CSV file and count rows in
with open(import_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        #Calculate total months, using total row count since both columns are the same length
        total_months += 1

        # Caculate net profit but totaling all values in the second column and store values in profit list
        current_month_change = int(row[1])
        total_profit_loss += current_month_change

        if (total_months == 1):

            previous_month_change = current_month_change
            continue

        else:
            profit_loss_change = current_month_change - previous_month_change
            months_list.append(row[0])
            change_list.append(profit_loss_change)
            previous_month_change = current_month_change
    
        # Calculate average change in profit over the entire period
        change_average = sum(change_list)/len(months_list)


        # Find greatest increase over the entire period with date
        greatest_increase = max(change_list)
        greatest_index = change_list.index(greatest_increase)
        greatest_date = months_list[greatest_index]

        # Find greatest decrease over the entire period with date
        greatest_decrease = min(change_list)
        least_index = change_list.index(greatest_decrease)
        least_date = months_list[least_index]

# Print to terminal
print("Financial Analysis")
print("----------------------")
print(f"Total Months:  {total_months}")
print(f"Average Change:  ${str(round(change_average,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})")


# Write to .txt file
lines = ["Financial Analysis", "----------------------", f"Total Months:  {total_months}", f"Average Change:  ${str(round(change_average,2))}",
         f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})", f"Greatest Decrease in Profits: {least_date} (${str(greatest_decrease)})"]
with open('Z:\TCC_Data_Analytics\Module_3_Python\PyBank\Analysis\pybank_output.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')