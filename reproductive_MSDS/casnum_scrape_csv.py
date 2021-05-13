import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/List_of_CAS_numbers_by_chemical_compound"

# csv파일, writer 만들기
f = open("reproduct_MSDS.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 항목 이름 넣기
column_names = ["Chemical formula", "Synonyms", "CAS number", "원본"]
writer.writerow(column_names)

# parser에 넣기
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")


tables = soup.find_all("table", attrs={"class":"wikitable"})
for table in tables:
    rows = table.find_all("tr")
    for idx, row in enumerate(rows, 1):
        if idx == 1: 
            continue
        columns = row.find_all("td")
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)


f.close()