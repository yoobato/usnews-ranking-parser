import csv
import re

# README
# Made usenews_cs_ori.txt from https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings?_sort=rank-asc
# In Nov 17, 2022
#   # of schools : 202

# ex)
# Massachusetts Institute of Technology
# Cambridge, MA
# #1 in Computer Science
#
# Carnegie Mellon University
# Pittsburgh, PA
# 2 in Computer Science (tie)
#
# ...
ORIGINAL_TXT_FILEPATH = './usnews_cs_ori.txt'

RESULT_CSV_FILEPATH = './usnews_cs_result.csv'

print('[START] TXT Parse')
with open(ORIGINAL_TXT_FILEPATH, 'r') as f:
    # Read file without new line character and empty lines
    lines = list(filter(None, f.read().splitlines()))

print(f'[END] TXT Parse / total {int(len(lines) / 3)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name', 'City'])

    num = 1
    for i in range(0, len(lines), 3):
        # Lines (i = Name, i+1 = City, i+2 = Rank)
        # ex) 'Massachusetts Institute of Technology', 'Cambridge, MA', '#1 in Computer Science'
        name = lines[i]
        city = lines[i + 1]
        rank_text = lines[i + 2]
        rank = re.search(r'#(\d+) in', rank_text).group(1)

        writer.writerow([num, rank, name, city])
        
        print(f'{num} - {name}')

        num += 1
    
print(f'[END] {RESULT_CSV_FILEPATH} created')
