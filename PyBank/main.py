import os
import csv

csvpath = os.path.join("C:\\","DataAnalytics","CU-VIRT-DATA-PT-06-2024-U-LOLC","python-challenge","PyBank","Resources","budget_data.csv")

total_month = 0
total_earning = 0
total_change = 0
avg_change = 0
month = 0
ProfitLost_List = []
Change_List = []
Month_List =[]

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     next(csvreader)
 
     for row in csvreader:
          total_count = len(row[0])
          total_month = total_month +1
          ProfitLost_List.append(row[1])
          Month_List.append(row[0])

for y in range(0, len(ProfitLost_List)):  
     total_earning = int(ProfitLost_List[y]) + total_earning
   
for x in range(1, len(ProfitLost_List)):
     Change_List.append(int(ProfitLost_List[x]) - int(ProfitLost_List[x-1]))
          
for i in Change_List:
       total_change = total_change + int(i)
       
month = int(total_month ) - 1
avg_change = round(total_change/month,2)

Max_Value = max(Change_List)
Max_Index = Change_List.index(Max_Value)
Min_Value = min(Change_List)
Min_Index = Change_List.index(Min_Value)

# print("Financial Analysis")
# print("-----------------------------")
# print(f"Total Months: {total_month}")
# print(f"Total: ${total_earning}")
# print(f"Average Change: ${avg_change}")
# print(f"Greatest Increase in Profits: {Month_List[Max_Index+1]} (${Max_Value})")
# print(f"Greatest Decrease in Profits: {Month_List[Min_Index+1]} (${Min_Value})")

line1 ="Financial Analysis"
line2 = "---------------------------------------"
line3 = "Total Months: "
line3a = str(total_month)
line4 = "Total: $"
line4a = str(total_earning)
line5 = "Total Change: $"
line5a = str(avg_change)
line6 =  "Greatest Increase in Profits: "
line6a = Month_List[Max_Index+1]
line6b = str(Max_Value)
line7 =  "Greatest Decrease in Profits: "
line7a = Month_List[Min_Index+1]
line7b = str(Min_Value)
phr1 = "($"
phr2 = ")"

file = open("c:\DataAnalytics\CU-VIRT-DATA-PT-06-2024-U-LOLC\python-challenge\PyBank\Analysis\PyBank_Analysis.txt","a")
file.write(line1 + "\n" + line2 + "\n" + line3 + line3a + "\n" + line4 + line4a + "\n" + line5 + line5a + "\n"
           + line6 + line6a + " " + phr1 + line6b + phr2 + "\n"
           + line7 + line7a + " " + phr1 + line7b + phr2 + "\n")
file.close()     

