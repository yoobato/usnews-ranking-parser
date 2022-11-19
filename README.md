# usnews-ranking-parser
Parse U.S. News Graduate Schools' ranking (CE &amp; CS)
 - CE : Computer Engineering
   - https://premium.usnews.com/best-graduate-schools/top-engineering-schools/computer-engineering-rankings
 - CS : Computer Science
   - https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings

### Get Started
1. Save [this](https://premium.usnews.com/best-graduate-schools/api/search?format=json&program=top-engineering-schools&specialty=computer-engineering&_mode=table&_page=1) to `page{n}.json` files.

2. Load whole contents in [here](https://premium.usnews.com/best-graduate-schools/top-science-schools/computer-science-rankings?_sort=rank-asc) with scrolling to an end, Copy tables, and Save it to txt file.

3. Run parsers
```python
python usnews_ce.py

python usnews_cs.py
```
