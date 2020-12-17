# def devide(a,b):
#     if b == 0:
#         raise IndexError("被除数不能为0")
#     else:
#         print(a/b)
# try:
#     devide(6,0)
# except ZeroDivisionError as e:
#     print("我负责处理第一个异常！！")
# except IndexError as e:
#     print("我负责处理第二个异常！！")
# except Exception as e:
#     print("我负责处理所有异常！！")


class Yonghubucunzai(Exception):
    def __init__(self,a):
        self.a = a


# raise Yonghubucunzai("用户不存在！")

def compare(a,b):
    if a != "李晓帅" and b !="147258":
        raise Yonghubucunzai("用户不存在！")
try:
    compare(1,2)

except ZeroDivisionError as e:
    print("我负责处理第一个异常！！")
except Yonghubucunzai as e:
    print("我负责处理第二个异常！！")
except Exception as e:
    print("我负责处理所有异常！！")