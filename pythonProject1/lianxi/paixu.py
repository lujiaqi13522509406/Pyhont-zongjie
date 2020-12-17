# import random
import time
#
#
# a=[8,5,2,9,6,3,7,4,1]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[j]>a[i]:
#             c=a[j]
#             a[j]=a[i]
#             a[i]=c
# print(a)
#
#
# #
# a=[8,5,2,9,6,3,7,4,1]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[j]<a[i]:
#            a[i],a[j]=a[j],a[i]
# print(a)
# #
# # 冒泡排序
# w=[9,6,3,8,5,2,7,4,1,15,23,4,854,418,4,1,56496,48,485,4,48,9,8,48,848,48,]
# for i in range(len(w)):
#     for j in range(len(w)-1):
#         if w[j]>w[j+1]:
#             w[j],w[j+1]=w[j+1],w[j]
# print(w)
# #
#
#
# # 求5的倍数的和
# y=[1,20,50,5,13,14,16,80]
# s=0
# for i in range(0,len(y)):
#      if y[i]%5==0:
#          s+=y[i]
# print(s)
#
#
#
# # 出现的次数
# e="this is a dog,that is a monkey!"
# for index,i in enumerate(e):
#     if i in e[:index]:
#         continue
#     print(i,"出现了",e.count(i),"次！")
#
# # 求最大值
# o=[5,2,3,6,9,8,7,4,12,5,6,1,51,851,1,564,165841,641,18564]
# da=o[0]
# xiao=o[0]
# for i in range(len(o)):
#     if o[i]>da:
#         da=o[i]
#     elif o[i]<xiao:
#         xiao=o[i]
# print(da,xiao)
#
#
# s=int(random.random()*50)
# w=0
# while True:
#     p=int(input("请输入一个数:"))
#     w+=1
#     if s>p:
#         print("小了")
#     elif s<p:
#         print("大了")
#     else:
#         print("对了,正确的数是：",s,"猜了",w,"次")
#         break





# li=[1,1,2,3,5,5,6,6,1,5,2,6]
# o=set(li)
# print(o)

#快速出重的方法
# list=[1,3,4,5,2,6,1]
# p=set(list)
# print(p)

#每隔60秒读取数据
# while True:
#     time.sleep(60)
#     with open("a.txt","r",encoding="utf-8") as stream:
#         date = stream.read()
#         with open("b.txt","a",encoding="utf-8") as wstream:
#             wstream.write(date)
#
# li=[1,2,3,4,5,6,7,8,9]
# print(li[::-1])


#质数
# list =[]
# for i in range(2,100):
#     for j in range(2,int(i/2)+1):
#         if not i%j:
#             break
#     else:
#         list.append(i)
# print(list)





class shuibei:
    __xingzhuang  = None
    __gaodu = None
    __rongji = None

    def __init__(self,xingzhuang,gaodu,rongji):
        self.__xingzhuang = xingzhuang
        self.__gaodu = gaodu
        self.__rongji = rongji

    def setXingzhuang(self,xingzhaung):
        self.__xingzhuang = xingzhaung
    def getXingzhuang(self):
        return self.__xingzhuang
    def setGaaodu(self,gaodu):
        self.__gaodu = gaodu
    def getGaodu(self):
        return self.__gaodu
    def setRongji(self,rongji):
        self.__rongji = rongji
    def getRongji(self):
        return self.__rongji

m = shuibei("方形","12cm","0.5L")
m.getXingzhuang()
m.getGaodu()
m.getRongji()
print("这是一个",m.getXingzhuang(),"的水杯，他的高度是",m.getGaodu(),"容积是",m.getRongji())