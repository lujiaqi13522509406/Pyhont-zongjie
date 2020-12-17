import random
#银行库
bank = {}  # username : {password,money......}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}
welcome = '''
***********************************
*      中国工商银行账户管理系统       *
***********************************
*               选项              *
'''

welcome_item = '''*              {0}.{1}             *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("**********************************")



# 通过账号获取账户信息
def findByAccount(account):
    for i in bank.keys():
        if bank[i]["account"] == account:
            return i
    return None

def bank_takeMoney(account,password,money):
    uname = findByAccount(account)
    if uname != None:
        if bank[uname]["password"] == password:
            if bank[uname]["money"] < money:
                return 3
            else:
                bank[uname]["money"] -= money
                return 0
        else:
            return 2
    else:
        return 0
