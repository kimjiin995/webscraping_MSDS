from scraping_copy import *
from excel_load import *

# 엑셀 workbook 로드하기
# (wb, ws) = load_wb()

# 엑셀에 있는 카스넘 불러오기
# casnum_list = bring_casnum(ws)

# 안전보건공단 홈페이지 브라우저 열기
url = "https://msds.kosha.or.kr/MSDSInfo/kcic/msdssearchAll.do"
browser = create_browser(url)

data = scrape_reproduct_data(browser, "벤젠")

print(data)


