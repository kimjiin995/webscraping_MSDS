from scraping import *
from excel_load import *

# 엑셀 workbook 로드하기
file_name = "reproductive_MSDS_원본추가.xlsx"
(wb, ws) = load_wb(file_name)

# 안전보건공단 홈페이지 브라우저 열기
url = "https://msds.kosha.or.kr/MSDSInfo/kcic/msdssearchAll.do"
browser = create_browser(url)

# 카스넘 검색해서 생식독성 데이터 가져오기 반복
for no in range(268, ws.max_row):
   
    # 엑셀에 있는 카스넘 불러오기
    casnum = bring_casnum(ws, no)
    
    # 데이터 가져오기
    data = scrape_reproduct_data(browser, casnum)
    
    # 엑셀에 데이터 넣기
    insert_data(ws, data, no)
    print(f"[{no}] {casnum} : {data} ")
   
    # 검색페이지로 이동
    browser.get(url)
    
    # unit 마다 엑셀 저장
    unit = 3
    if no % unit == 0:
        wb.save(file_name)
        print(f"<{no}번 까지 저장 되었습니다.>")


# 마지막 엑셀 저장
wb.save(file_name)
print(f"<스크래핑이 완료 되었습니다.(총 {no}번)>")


