from day13.day13.yichang import JineException
class yinhang:
    __jine = None

    def setJine(self,jine):
        self.__jine = jine
    def getJine(self):
        return self.__jine
    def compare(self,a):
        if self.__jine >= a.getJine():
            print("正常取出！")
        else:
            raise JineException("金额不足异常！！")


p = yinhang()
p.setJine(3000)

p1 = yinhang()
p1.setJine(int(input("请输入您要取出的金额:")))

p.compare(p1)














