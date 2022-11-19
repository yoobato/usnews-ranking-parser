import csv
import re

# README
# Made qs_msba_ori.txt from https://www.topuniversities.com/university-rankings/business-masters-rankings/business-analytics/2023
# In Nov 20, 2022
#   # of schools : 61

# ex)
# 1
# MIT (Sloan)Master of Business Analytics
# Cambridge (MA), United States
# 93.5
# 2
# UCLA (Anderson)Master of Science in Business Analytics
# Los Angeles (CA), United States
# 93.4
# ...
ORIGINAL_TXT_FILEPATH = './qs_msba_ori.txt'

RESULT_CSV_FILEPATH = './qs_msba_result.csv'

print('[START] TXT Parse')
with open(ORIGINAL_TXT_FILEPATH, 'r') as f:
    # Read file without new line character and empty lines
    lines = list(filter(None, f.read().splitlines()))

print(f'[END] TXT Parse / total {int(len(lines) /4)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name', 'City'])

    num = 1
    for i in range(0, len(lines), 4):
        # Lines (i = Rank, i+1 = Name, i+2 = City, i+3 = Score(Unused))
        # ex) '1', 'MIT (Sloan)Master of Business Analytics', 'Cambridge (MA), United States', '93.5'
        rank = lines[i]
        name = lines[i + 1]
        city_text = lines[i + 2]
        city = city_text.replace(', United States', '')

        writer.writerow([num, rank, name, city])
        
        print(f'{num} - {name}')

        num += 1
    
print(f'[END] {RESULT_CSV_FILEPATH} created')
