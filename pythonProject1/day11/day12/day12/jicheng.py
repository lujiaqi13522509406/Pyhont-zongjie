# class yidai:
#     lingsheng = None
#     haoma = None
#
#     def call(self,numder):
#         print(self.haoma,"正在给",numder,"打电话。。。。。")
#
#
# class erdai(yidai):
#     place = None
#     picture = None
#     pc = None
#
#
#     def call(self,numder):
#         super().call(numder)
#         print("归属地:",self.place,"，图片:",self.picture,"，备注:",self.pc)
#
#
# phone = erdai()
# phone.haoma = "147258"
# phone.lingheng = "月亮之上"
#
# phone.place = "北京"
# phone.picture = "李晓帅"
# phone.pc = "小帅来电"
# phone.call("15451545154")

# import time
#
# class Animal:
#     __color = None
#     __weight = None
#     __age = None
#
#     def __init__(self,color,weight,age):
#         self.__age = age
#         self.__color = color
#         self.__weight = weight
#
#     def setAge(self,age):
#         self.__age = age
#     def getAge(self):
#         return self.__age
#     def steColor(self,color):
#         self.__color = color
#     def getColor(self):
#         return self.__color
#     def setWeight(self,weight):
#         self.__weight = weight
#     def getWeight(self):
#         return self.__weight
#
#
#
# class cat(Animal):
#     __yanse = None
#
#     def __init__(self,age,color,weight,yanse):
#         super().__init__(age,color,weight)
#         self.__yanse = yanse
#
#     def setYanse(self,yanse):
#         self.__yanse = yanse
#     def getYanse(self):
#         return self.__yanse
#
#     def show(self):
#         for i in range(3):
#             print("喵~")
#             time.sleep(2)
#         print("我是一只猫，我今年",self.getAge(),"岁了，我是",self.getColor(),"的，我的体重是",self.getWeight(),"斤，我的尾巴也是",self.getYanse(),"的")
#
#
#
# d = cat(5,"黑色",10,"黑色")
# d.show()

