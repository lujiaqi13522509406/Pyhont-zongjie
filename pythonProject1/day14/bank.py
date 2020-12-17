from day14.moban import bank
from day14.moban import bank_name
from day14.moban import bank_takeMoney




class bank:
    bank["张三"] = {"account": "admin", "money": 2000,
                  "country": "中国", "province": "安徽省",
                  "street": "幸福大道", "door": "s001", "password": "admin", "bank_name": bank_name}

    def takeMoney:
        account = input("账户")
        password = input("密码")
        tmoney = input("取出金额", "int")

        f = bank_takeMoney(account, password, tmoney)

        if f == 1:
            print("改用户不存在！")
        elif f == 2:
            print("密码错误！")
        elif f == 3:
            print("取款金额不足！")
        elif f == 0:
            print("取款成功！")



































