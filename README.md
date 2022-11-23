# Graduate school ranking in U.S.
- Parse **U.S. News** Graduate Schools' ranking (CE, CS, MSBA)
  - CE : Computer Engineering
    - https://premium.usnews.com/best-graduate-schools/top-engineering-schools/computer-engineering-rankings
  - CS : Computer Science
    - https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings
  - MSBA : Business Anlaytics MBA
    - https://premium.usnews.com/best-graduate-schools/top-business-schools/business-analytics-rankings
- Parse **QS** ranking (MSBA)
  - MSBA : Master of Science in Business Analytics
    - https://www.topuniversities.com/university-rankings/business-masters-rankings/business-analytics/2023
- Parse **Forbes** ranking
  - https://www.forbes.com/top-colleges

## Requirements
- Enroll [U.S. News College Compass](https://www.usnews.com/usnews/store/college_compass) `Need to pay`

## Get Started
1. Save [this](https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-engineering-schools&specialty=computer-engineering&_mode=table&_page=1) to `page{n}.json` files.

2. Load whole contents in [here](https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings?_sort=rank-asc) with scrolling to an end, Copy tables, and Save it to txt file.

3. Save [this](https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-business-schools&specialty=business-analytics&_mode=table&_page=1) to `msba_page{n}.json` files.

4. Load whole contents in [here](https://www.topuniversities.com/university-rankings/business-masters-rankings/business-analytics/2023) with *Results per page* to maximum number, Copy tables, and Save it to txt file.

5. Load whole contents in [here](https://www.forbes.com/top-colleges), Copy tables (every page), and Save it to txt file.

6. Run parsers
```python
python usnews_ce.py

python usnews_cs.py

python usnews_msba.py

python qs_msba.py

python forbes.py
```
