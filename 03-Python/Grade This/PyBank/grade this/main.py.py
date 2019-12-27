import os
import csv
#importing the data
budget_data = os.path.join("Resources", "budget_data.csv")

file_to_output = os.path.join("Resources", "financial_analysis.txt")
#making boxes for the data to be sorted in

change = []
avgchange = []
gincrease = []
gdecrease = []


total_net = 0
total_months = 0
change = 0 
first_row = 0 

greatest_increase_month = ""
greatest_increase = 0
greatest_decrease_month = ""
greatest_decrease = 0

# #reading the file
# with open(budget_data) as csvfile:
#     csvreader = csv.reader(csvfile)
    
#     for row in csvreader:
        
        
#         # # .append
#         # #counting the months
       
#         # change = len[Profit_Loss - (Profit_Loss - 1)]
        
        
with open(budget_data,) as csvfile:
    csvreader = csv.DictReader(csvfile)
    total_net = []


   # Enumerate() method adds a counter to an iterable and 
   # returns it in a form of enumerate object. 
   # This enumerate object can then be used directly in 
   # for loops or be converted into a list of tuples using 
   # list() method.
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        total_net.append(value)
        total_months = total_months + 1    
        #avgchange = float(sumtotal) / float(total_months) * 100



with open(file_to_output, "w") as txt_file:
    sumnet = sum[total_net]
    budget_output = (
        f"Total Months: {total_months}\n"
        f"Total Net: {sumnet}\n"
            )
        
    
        # if change > greatest_increase:
        #      greatest_increase = change
        #      greatest_increase_month = date

        # if change < greatest_decrease:
        #      greatest_decrease = change
        #      greatest_decrease_month = date
    #budget_output = (
     #f"Financial Analysis\n"
     #f"Total Months: {total_months}\n"
    # f"Total:{}.format(sum(total_net))\n"
     #f"Average Change:{avgchange}\n"
     #f"Greatest Increase in Profits:{greatest_increase}(str{greatest_increase_month})\n"
     #f"Greatest Decrease in Profits:{greatest_decrease} (str{greatest_decrease_month})\n"
    # f"--------------------------------------------------\n"

    #)
    txt_file.write(budget_output)
