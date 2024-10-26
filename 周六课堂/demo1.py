print("开启python之门，一起探索吧！")

def fibonaci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonaci(num - 1) + fibonaci(num - 2)

print(fibonaci(7))

import datetime as dt
today = dt.datetime.today()
print(today)

user = input("输入用户名:")
pwd = input("输入密码:")

print(f"用户名是：{user},密码是：{pwd}")

