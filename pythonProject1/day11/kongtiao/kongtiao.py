# class bear:
#     __brand = None
#     __price = None
#     __kaiji = None
#     __guanji = None
#
#     def __init__(self,a,b):
#         self.__brand = a
#         self.__price = b
#
#     def setBrand(self,a):
#         self.__brand = a
#     def getBrand(self):
#         return self.__brand
#     def setPrice(self,b):
#         self.__price = b
#     def getPrice(self):
#         return self.__price
#     def setKaiji(self):
#         print("空调开机了。。。。。")
#     def setGuanji(self,d):
#         self.__guanji = d
#
# c = bear("美的","3500")
# c.setKaiji()
# c.setGuanji = int(input("请设置自动关机时间:"))
# if c.setGuanji < 0 or c.setGuanji > 60:
#     print("时间输入不在范围之内！！")
# else:
#     print("空调将在",c.setGuanji,"分钟后自动关闭。")
#
# print("品牌为",c.getBrand(),"价格为",c.getPrice())


class  student:
    __name = None
    __age = None

c = student()
c.name = "李晓帅"
c.age = "22"
print("大家好！我叫",c.name,"我今年",c.age,"岁了")