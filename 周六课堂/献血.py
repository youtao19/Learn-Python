gender = input("请输入性别:")
weight = input("请输入体重:")
age = input("请输入年龄:")


if gender == '女':
    if int(weight) >= 45 and 18 <= int(age) <= 55:
        print("该女士可以献血")
    else:
        print("该女士不可以献血")
else:
    if int(weight) >= 50 and 18<=int(age)<=60:
        print('该男士可以献血')
    else:
        print("该男士不可以献血")