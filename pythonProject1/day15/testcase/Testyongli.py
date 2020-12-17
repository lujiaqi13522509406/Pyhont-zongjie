import unittest
import day14.moban
class TestBank(unittest.TestCase):
    def testtakeMoney(self):
        account = "admin"
        password = "admin"
        money = 1000

        sum = 0

        day14.moban.bank["张三"] = {"account":"admin","password":"admin","money":2000}

        s = day14.moban.bank_takeMoney(account,password,money)

        print(s)

        self.assertIs(sum,s)




    def testtakeMoney1(self):
        account = "admin1"
        password = "admin"
        money = 1000

        sum = 0

        day14.moban.bank["张三"] = {"account":"admin","password":"admin","money":2000}

        s = day14.moban.bank_takeMoney(account,password,money)

        print(s)

        self.assertIs(sum,s)



    def testtakeMoney2(self):
        account = "admin"
        password = "admin1"
        money = 1000

        sum = 0

        day14.moban.bank["张三"] = {"account":"admin","password":"admin","money":2000}

        s = day14.moban.bank_takeMoney(account,password,money)

        print(s)

        self.assertIs(sum,s)



    def testtakeMoney3(self):
        account = "admin"
        password = "admin"
        money = 3000

        sum = 0

        day14.moban.bank["张三"] = {"account":"admin","password":"admin","money":2000}

        s = day14.moban.bank_takeMoney(account,password,money)

        print(s)

        self.assertIs(sum,s)
