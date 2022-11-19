# Graduate school ranking in U.S.
- Parse **U.S. News** Graduate Schools' ranking (CE &amp; CS)
  - CE : Computer Engineering
    - https://premium.usnews.com/best-graduate-schools/top-engineering-schools/computer-engineering-rankings
  - CS : Computer Science
    - https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings
- Parse **QS** ranking (MSBA)
  - MSBA : Master of Science in Business Analytics
    - https://www.topuniversities.com/university-rankings/business-masters-rankings/business-analytics/2023

## Requirements
- Enroll [U.S. News College Compass](https://www.usnews.com/usnews/store/college_compass) `Need to pay`

## Get Started
1. Save [this](https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-engineering-schools&specialty=computer-engineering&_mode=table&_page=1) to `page{n}.json` files.

2. Load whole contents in [here](https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings?_sort=rank-asc) with scrolling to an end, Copy tables, and Save it to txt file.

3. Load whole contents in [here](https://www.topuniversities.com/university-rankings/business-masters-rankings/business-analytics/2023) with *Results per page* to maximum number, Copy tables, and Save it to txt file.

4. Run parsers
```python
python usnews_ce.py

python usnews_cs.py

python qs_msba.py
```
