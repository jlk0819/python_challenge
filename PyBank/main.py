import os
import csv
csvpath = os.path.join(os.getcwd(),"PyBank","Resources", "budget_data.csv")
#Set variables
month_count = 0
total_profit_loss = 0
monthly_profit_loss = 0
diff_profit_loss = 0
greatest_decrease_profit = 0
greatest_increase_profit = 0
# hold data
months = []
difference = []
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #header row
    header = next(csv_reader)
    
    #months
    month_count += 1
    first_row = next(csv_reader)
    new_profit_loss = int(first_row[1])
    total_profit_loss = int(first_row[1])

    for row in csv_reader:   
        # Profit loss
        months.append(row[0])

        diff_profit_loss = int(first_row[1])-new_profit_loss
        diff_profit_loss +=  monthly_profit_loss
        
        # Calculate the change, then add it to list of changes
        diff_profit_loss = int(row[1])-monthly_profit_loss
        difference.append(diff_profit_loss)

        month_count += 1
    
        #Total net amount of "Profit/Losses over entire period"
        new_profit_loss = new_profit_loss + int(row[1])

#Greatest increase in profits
    greatest_increase_profit = max(difference)
    greatest_index = difference.index(greatest_increase_profit)
    greatest_date = months[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease_profit = min(difference)
    worst_index = difference.index(greatest_decrease_profit)
    worst_date = months[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(difference)/len(difference)


#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(month_count)}")
print(f"Total: ${str(new_profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase_profit)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease_profit)})")

#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(month_count)}")
line4 = str(f"Total: ${str(new_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase_profit)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease_profit)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

