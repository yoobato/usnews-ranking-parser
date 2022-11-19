import csv
import json

# README
# Made msba_page{i}.json from https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-business-schools&specialty=business-analytics&_mode=table&_page=1
# In Nov 20, 2022
#   # of schools : 43
#   # of pages : 5 (10 schools per page)

RESULT_CSV_FILEPATH = './usnews_msba_result.csv'


schools = []

print('[START] JSON Parse')
for i in range(1, 6):
    json_filename = f'msba_page{i}.json'

    with open(f'./{json_filename}') as f:
        json_data = json.load(f)
    sub_schools = json_data['data']['items']

    print(f'Parse {json_filename}... {len(sub_schools)} schools')
    schools += sub_schools

print(f'[END] JSON Parse / total {len(schools)} schools')

print(f'[START] Create {RESULT_CSV_FILEPATH}')
with open(RESULT_CSV_FILEPATH, 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(['#', 'Rank', 'Name', 'City', 'Avg GMAT', 'Tuition'])

    num = 1
    for school in schools:
        row = [
            num,
            int(school['ranking']['display_rank']),
            school['name'],
            f"{school['city']}, {school['state']}",
            int(school['schoolData']['b_test_score']) if school['schoolData']['b_test_score'] else ''
        ]

        if school['schoolData']['v_ft_tuition']:
            tuitions = school['schoolData']['v_ft_tuition']

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
