# class laophone:
#     __pinpai = None
#     __dianhua = ""
#
#     def setPinpai(self,pinpai):
#         self.__pinpai = pinpai
#
#     def setDianhua(self,dianhua):
#         self.__dianhua = dianhua
#
# class xinphone(laophone):
#     __yuyin = None
#     def __init__(self,yuyin):
#        self.__yuyin = yuyin
#
#     def setYuyin(self,yuyin):
#         self.__yuyin = yuyin
#     def getYuyin(self):
#         return self.__yuyin
#     def setPinpai(self):
#         print("品牌为：华为的手机很好用。。。")
#
#
#
# p = xinphone("语音拨号中。。。。")
# p.setDianhua = "147258"
# print(p.getYuyin())
# print("正在给",p.setDianhua,"打电话。。。。。")
# p.setPinpai()


class cook:
    __name = None
    __age = None
    # __zhengfan = None


    def setNmae(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self,age):
        return self.__age
    def Zhengfan(self):
        print("放米，放水，开火，蒸饭")

class cooker(cook):
    __chaocai = None
    def Chaocai(self):
        print("炒菜的方法是xxxxxxx")
class chushi(cooker):
    __zhengfaner = None
    __chaocaier = None

    def __init__(self,zhengfaner,chaocaier):
        super().__init__(self,zhengfaner,chaocaier)
        self.__zhengfaner = zhengfaner
        self.__chaocaier = chaocaier


    def setZhengfaner(self,zhengfaner):
        self.__zhengfaner = zhengfaner
    def getZhengfaner(self):
        return self.__zhengfaner
    def setChaocaier(self,chaocaier):
        self.__chaocaier = chaocaier
    def getChaocaier(self):
        return self.__chaocaier

p = chushi("洗米然后蒸饭","切菜扒拉")
print(p)
p.Zhengfan()
p.Chaocai()
