# -*- coding: utf-8 -*-‘
import xlrd
data = xlrd.open_workbook("C:\\Users\\lim\\Desktop\\1.xls")
table = data.sheet_by_name(u"Sheet1")

A = table.row_values(1)
B = table.col_values(1)
# print A,B
allrows = table.nrows  # 获取所有行
allcols = table.ncols   #获取所有列
raw_input_A = raw_input("raw_input: ")
print raw_input_A
for i in range(allcols):
    print table.row_values(i)
    cell_A1 = table.cell_value(1,1).encode('utf-8')
    cell_C4 = table.cell_value(2,3).encode('utf-8')
    #打印某一个单元格的内容 每一行，每一列从0开始计数。
    print table.cell_value(1,1)

cell_A1 = table.row(1)[0].value
