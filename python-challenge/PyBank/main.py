import os
import csv

# csvpath = os.path.join('.','Resouces','budget_data.csv')

#csvpath = os.path.join('python-challenge' ,'PyBank','Resources','budget_data.csv')

csvpath = os.path.join("C:\\","DataAnalytics","CU-VIRT-DATA-PT-06-2024-U-LOLC","python-challenge","PyBank","Resources","budget_data.csv")

#csvpath = 'python-challenge\PyBank\Resources\budget_data.csv'

total_month = 0
total_earning = 0
previous_earning = 0
total_change = 0
ProfitLost_List = []
Change_List = []
Month_List =[]

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     next(csvreader)
 
     for row in csvreader:
          total_count = len(row[0])
          total_month = total_month + 1
    
          ProfitLost_List.append(row[1]) 
          Month_List.append(row[0])

      
for x in range(1, len(ProfitLost_List)):
     Change_List.append(int(ProfitLost_List[x]) - int(ProfitLost_List[x-1]))
     #print(Change_List[x-1])
          
for i in Change_List:
      total_change = total_change + int(i)


print(f'Financial Analysis')

print('---------------------------------------')



Max_Value = max(Change_List)
Max_Index = Change_List.index(Max_Value)
print(Max_Value)
print(Max_Index)
Min_Value = min(Change_List)
Min_Index = Change_List.index(Min_Value)
print(Min_Value)
print(Min_Index)
print(Month_List[Min_Index+1])
print(Month_List[Max_Index+1])



