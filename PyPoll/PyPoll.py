import os
import csv
import pandas as pd

path = '/Users/rspxrsp/Documents/GitLab/TECMC201902DATA2/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
open_path = open(path, mode="r")
reader = csv.reader(open_path, delimiter=',')
row_count = len(list(reader)) - 1

df = pd.read_csv(path)
votes = df.iloc[:,0].count()

candidate_list = df['Candidate'].tolist()
K_Count = candidate_list.count('Khan')
C_Count = candidate_list.count('Correy')
L_Count = candidate_list.count('Li')
O_Count = candidate_list.count("O'Tooley")

K = float(candidate_list.count('Khan')/votes*100)
C = float(candidate_list.count('Correy')/votes*100)
L = float(candidate_list.count('Li')/votes*100)
O = float(candidate_list.count("O'Tooley")/votes*100)

K = round(K)
C = round(C)
L = round(L)
O = round(O)

K = str(K) + '%'
C = str(C) + '%'
L = str(L) + '%'
O = str(O) + '%'

vote_stats = {K:'Khan', C:'Correy', L:'Li', O:"O'Tooley"}
Winner = vote_stats.get(max(vote_stats))

new_file = open("Election Results.txt","a")
new_file.write("Election Results\n----------------------------\nTotal Votes: " + str(votes) + "\n----------------------------\nKhan: " + str(K) + " (" + str(K_Count) + ")" + "\nCorrey: " + str(C) + " (" + str(C_Count) + ")" + "\nLi: " + str(L) + " (" + str(L_Count) + ")" + "\nO'Tooley: " + str(O) + " (" + str(O_Count) + ")" + "\n----------------------------\nWinner: " + str(Winner) + "\n----------------------------")
new_file.close()