import xlrd
data = xlrd.open_workbook("D:\\编程\\a.xlsx")
sheet = data.sheet_by_name("用户管理")
print("有",sheet.nrows,"行数据！有",sheet.ncols,"列数据！")
rows=sheet.nrows
cols=sheet.ncols

for i in range(rows):
    for j in range(cols):
        print(str(sheet.cell_value(i,j)).replace(".0",""),"\t",end="")
    print()

import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="db",charset="utf8")
cursor = con.cursor()
sql = "insert into person value()"
s = cursor.execute(sql)
print(s)

cursor.close()
con.close()

# class ren:
#     yanjing = 0
#     bizi = 0
#     erduo = 0
#     zuiba = 0
#     yifu = ""
#     kuzi = ""
#     xie = ""
#     def run(self):
#         print("李晓帅在大马路上跑来跑去！像疯了一样！")
# c = ren()
# c.yanjing = 2
# c.bizi = 1
# c.erduo = 2
# c.zuiba = 1
# c.yifu = "黑色"
# c.kuzi = "灰色"
# c.xie = "aj"
#
# c.run()
# print("他有",c.yanjing,"个眼睛，",c.bizi,"一个鼻子，",c.erduo,"只耳朵，",c.zuiba,"张嘴，穿着",c.yifu,"的上衣，",c.kuzi,"的裤子，穿着一双",c.xie)