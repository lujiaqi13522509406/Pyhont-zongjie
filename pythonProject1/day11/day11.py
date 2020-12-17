# class person:
#     __username = ""
#     __age = None
#     def setUsername(self,u):
#         self.__username=u
#
#     def setAge(self,a):
#         if a == None:
#             print("年龄非法！")
#         elif a > 120 or a < 0:
#             print("年龄非法！")
#         else:
#             self.__age = a
#     def show(self):
#         print("我叫",self.__username,"，我的年龄为:",self.__age)
# p = person()
#
# p.setUsername("李晓帅")
# p.setAge(22)
# p.show()
class Dog:
    __color = None
    __speed = None
    __belong = None

    def __init__(self,a,b,c):
        self.__color = a
        self.__speed = b
        self.__belong = c

    def setColor(self,a):
        self.___color = a
    def getColor(self):
        return self.__color

    def setSpeed(self,b):
        self.__speed = b
    def getSpeed(self):
        return self.__speed

    def setBelong(self,c):
        self.__belong = c
    def getBelong(self):
        return self.__belong

d=Dog("黑色","犬科","50km/h")

print("我家有一只狗，它是",d.getColor(),"的，它属于",d.getSpeed(),"，它的奔跑速度最快可以达到",d.getBelong())