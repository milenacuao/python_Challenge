import os
import csv
csvpath= os.path.join('/','Users','rociocuao','Desktop','Python_challenge','resources','budget_data.csv')


budget_data = []

with open(csvpath) as csvfile:
     reader = csv.DictReader(csvfile)
     
     
     for row in reader:
          budget_data.append({"month": row["Date"],"amount": int(row["Profit/Losses"]),"change":0})
          
total_months = len(budget_data)

previous_amount = budget_data[0]["amount"]
for i in range(total_months):
    budget_data [i]["change"]= budget_data[i]["amount"]-previous_amount
    previous_amount=budget_data[i]["amount"]
    
total_amount = sum(row['amount']for row in budget_data)

total_change=sum (row['change'] for row in budget_data)
average= round(total_change/(total_months-1),2)

get_increase =max(budget_data,key=lambda x:x['change'])
get_decrease =min(budget_data,key=lambda x:x['change'])

print('Financial Analysis')
print('---------------------')
print(f'total Months:{total_months}')
print(f'total ${total_amount}')
print(f'average change: ${average}')
print(f'Greatest increase in profits: {get_increase["month"]}(${get_increase["change"]})')
print(f'greatest decrease in profits:{get_decrease["month"]}(${get_decrease["change"]})')


csvpath = os.path.join('/','Users','rociocuao','Desktop','Python_challenge','analysis','analysis.txt')
     
with open (csvpath,'w') as file:
     file.write('Financial Analysis')
     file.write('---------------------')
     file.write(f'total Months:{total_months}')
     file.write(f'total ${total_amount}')
     file.write(f'average change: ${average}')
     file.write(f'Greatest increase in profits: {get_increase["month"]}(${get_increase["change"]})')
     file.write(f'greatest decrease in profits:{get_decrease["month"]}(${get_decrease["change"]})')
