import csv
import json

# README
# Made page{i}.json from https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-engineering-schools&specialty=computer-engineering&_mode=table&_page=1
# In Nov 17, 2022
#   # of schools : 146
#   # of pages : 15 (10 schools per page)

RESULT_CSV_FILEPATH = './usnews_ce_result.csv'


schools = []

print('[START] JSON Parse')
for i in range(1, 16):
    json_filename = f'page{i}.json'

    with open(f'./{json_filename}') as f:
        json_data = json.load(f)
    sub_schools = json_data['data']['items']

    print(f'Parse {json_filename}... {len(sub_schools)} schools')
    schools += sub_schools

print(f'[END] JSON Parse / total {len(schools)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name', 'City', 'Avg GRE Quant', 'Tuition'])

    num = 1
    for school in schools:
        row = [
            num,
            int(school['ranking']['display_rank']),
            school['name'],
            f"{school['city']}, {school['state']}",
            int(school['schoolData']['avg_quant_gre']) if school['schoolData']['avg_quant_gre'] else ''
        ]

        if school['schoolData']['complete_tuition'] and len(school['schoolData']['complete_tuition']) > 1:
            tuitions = school['schoolData']['complete_tuition'][1:]

            tmp_tuitions = []
            for tuition in tuitions:
                tmp_tuitions.append(' '.join(tuition))
            
            row.append(' / '.join(tmp_tuitions))
        else:
            row.append('')
        
        writer.writerow(row)
        num += 1

        print(f'{row[0]} - {row[2]}')
    
print(f'[END] {RESULT_CSV_FILEPATH} created')
