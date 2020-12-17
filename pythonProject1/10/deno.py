'''
   1.安装与导入xlrd模块



'''
import xlrd

data = xlrd.open_workbook("D:\\编程\\a.xlsx")
# 2.从工作簿里面选中选项卡
sheet = data.sheet_by_name("123")
#3.
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows = sheet.nrows
cols = sheet.ncols
f = open("321.txt","w",encoding="utf-8")
a = []
#4.遍历所有数据

for i in range(rows):
    a = []
    for j in range(cols):
        a.append(str(sheet.cell_value(i,j)).replace(".0",""))
    string = ",".join(a)
    f.write(string + "\n")












