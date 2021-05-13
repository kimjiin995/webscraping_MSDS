from excel_load import *

(wb, ws) = load_wb()

# 엑셀에 있는 카스넘 불러오기
casnum_list = bring_casnum(ws)
