import xlrd
import pandas as pd
import numpy as np
loc=("IPL22.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
# for i in sheet.nrows:
#     print(i)
print(sheet.cell_value(1,1))
ipl=pd.read_excel(loc)
for i in range(0,sheet.nrows):
    print(sheet.cell_value(i,2))
print(ipl)
print(type(ipl))
print(l)