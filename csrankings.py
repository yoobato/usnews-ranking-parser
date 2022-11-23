import csv
import re

# README
# Made csrankings_ori.txt from https://csrankings.org/#/index?all&us
# In Nov 17, 2022
#   # of schools : 185

# ex)
# 1    	► Carnegie Mellon University  closed chart	19.9	160
# 2   	► Univ. of Illinois at Urbana-Champaign  closed chart	14.7	112
# ...
ORIGINAL_TXT_FILEPATH = './csrankings_ori.txt'

RESULT_CSV_FILEPATH = './csrankings_result.csv'

print('[START] TXT Parse')
with open(ORIGINAL_TXT_FILEPATH, 'r') as f:
    # Read file without new line character and empty lines
    lines = list(filter(None, f.read().splitlines()))

print(f'[END] TXT Parse / total {len(lines)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name'])

    num = 1
    for line in lines:
        # Split by \t
        # ex) '1', 'Carnegie Mellon University'
        elements = line.split('\t')
        rank = int(elements[0].strip())
        name_text = elements[1]
        name = name_text.replace('►', '').replace('closed chart', '').strip()

        writer.writerow([num, rank, name])
        
        print(f'{num} - {name}')

        num += 1

print(f'[END] {RESULT_CSV_FILEPATH} created')
