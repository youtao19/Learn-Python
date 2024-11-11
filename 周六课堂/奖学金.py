sco1 = int(input("输入单科成绩："))
sco2 = int(input("输入总成绩："))

if int(sco1) >= 90 and int(sco2) >= 185:
    print("一等奖学金")
elif int(sco1) >= 85 and int(sco2) >= 175:
    print("二等奖学金")
elif int(sco1) >= 80 and int(sco2) >= 165:
    print("三等奖学金")

