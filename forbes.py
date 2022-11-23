import csv
import re

# README
# Made forbes_ori.txt from https://www.forbes.com/top-colleges
# In Nov 23, 2022
#   # of schools : 498

# ex)
# 1.
# Massachusetts Institute of Technology
# MA
# Private not-for-profit
# $53,162
# $10,070
# $173,700
# 2.
# Stanford University
# CA
# Private not-for-profit
# $54,547
# $11,765
# $173,500
# ...
ORIGINAL_TXT_FILEPATH = './forbes_ori.txt'

RESULT_CSV_FILEPATH = './forbes_result.csv'

print('[START] TXT Parse')
with open(ORIGINAL_TXT_FILEPATH, 'r') as f:
    # Read file without new line character and empty lines
    lines = list(filter(None, f.read().splitlines()))

print(f'[END] TXT Parse / total {int(len(lines) / 7)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name', 'State', 'Type'])

    num = 1
    for i in range(0, len(lines), 7):
        # Lines (i = Rank, i+1 = Name, i+2 = State, i+3 = Type)
        # ex) '1.', 'Massachusetts Institute of Technology', 'MA', 'Private not-for-profit'
        rank = lines[i].strip()[:-1]
        name = lines[i + 1].strip()
        state = lines[i + 2].strip()
        type = lines[i + 3].strip()
        
        writer.writerow([num, rank, name, state, type])
        
        print(f'{num} - {name}')

        num += 1
    
print(f'[END] {RESULT_CSV_FILEPATH} created')
