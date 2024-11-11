age = int(input("请输入年龄:"))
leye = float(input("请输入左眼视力:"))
reye = float(input("请输入右眼视力:"))

if 17 <= age <= 24 and leye >= 4.5 and reye >= 4.6:
    print("可以参军")
else:
    print("不可以参军")