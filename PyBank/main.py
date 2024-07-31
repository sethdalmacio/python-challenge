
import csv

file_path = "/Users/ylsstudent/Documents/Data_Analytics_Bootcamp/Module_3_Python/python-challenge/PyBank/Resources/budget_data.csv"

months = []
revenue = []

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    csv_header = next(csvreader)
  
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

changes = []
for i in range(1,len(revenue)):
    change = revenue[i] - revenue[i - 1]
    changes.append(change)


total_months = (len(months))
net_total = sum(revenue)
average_change = round((sum(changes) / len(changes)),2)
max_profit = max(changes)
max_profit_index = changes.index(max_profit)
max_profit_month = months[max_profit_index + 1]

max_loss = min(changes)
max_loss_month = months[changes.index(max_loss) + 1]

print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_profit_month} ${max_profit}")
print(f"Greates Decrease in Profits: {max_loss_month} ${max_loss}")

output_path = "/Users/ylsstudent/Documents/Data_Analytics_Bootcamp/Module_3_Python/python-challenge/PyBank/Analysis/PyBank_Analysis.txt"

with open(output_path, 'w') as file:
    file.write( f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {max_profit_month} ${max_profit}\n"
    f"Greatest Decrease in Profits: {max_loss_month} ${max_loss}\n"
)