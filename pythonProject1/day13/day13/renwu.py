from day13.day13.yichang import AgeException
class person:
    __name = None
    __age = None
    def __init__(self,name,age):
        self.__name = name
        if age > 0:
            print("正确！")
        else:
            raise AgeException("年龄输入错误！")
        self.__age = age
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age


b = person("张三",0)


