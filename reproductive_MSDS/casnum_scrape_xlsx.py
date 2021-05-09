import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 위키피디아 카스번호 리스트
url = "https://en.wikipedia.org/wiki/List_of_CAS_numbers_by_chemical_compound"

# 항목 이름 넣기
wb = Workbook()
ws = wb.active
column_names = ["NO.", "Chemical formula", "Synonyms", "CAS number", "원본"]
ws.append(column_names)

# parser에 넣기
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 데이터 찾고 엑셀에 넣기
no = 1
tables = soup.find_all("table", attrs={"class":"wikitable"})
for table in tables:
    rows = table.find_all("tr")
    for idx, row in enumerate(rows, 1):
        if idx == 1: 
            continue
        columns = row.find_all("td")
        data = [column.get_text().strip() for column in columns]

        # 번호와 함께 넣기
        data.insert(0, no)
        ws.append(data)
        no += 1

# 엑셀 저장하기
wb.save("reproductive_MSDS.xlsx")