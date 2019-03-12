import os
import csv
import pandas as pd

path = '/Users/rspxrsp/Documents/GitLab/TECMC201902DATA2/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'
open_path = open(path, mode="r")
reader = csv.reader(open_path, delimiter=',')
row_count = len(list(reader)) - 1

open_path.seek(0)
for column in reader:
    pass

df = pd.read_csv(path)
total = df.iloc[:,1].sum()
total = int(total)

df['Change'] = df.iloc[:,1].diff()
average = df.iloc[:,2].mean()
average = int(average)

max_loss = df.iloc[:,2].min()
max_loss = int(max_loss)

df.columns = ['Date', 'Earning', 'Change']

date_loss = df.loc[df['Change'] == (max_loss)].index
date_loss = df.iloc[date_loss,0]
date_loss = date_loss.real[0]

max_profit = df.iloc[:,2].max()
max_profit = int(max_profit)

date_profit = df.loc[df['Change'] == (max_profit)].index
date_profit = df.iloc[date_profit,0]
date_profit = date_profit.real[0]

new_file = open("Analisis.txt","a")
new_file.write('Financial Analysis\n----------------------------------------------------\nTotal Months: '+str(row_count)+'\nTotal: $ '+str(total)+'\nAverage Change: $ '+str(average)+'\nGreatest Increase in Profits: '+str(date_profit)+' ($ '+str(max_profit)+')'+'\nGreatest Decrease in Profits: '+str(date_loss)+' ($ '+str(max_loss)+')')
new_file.close()