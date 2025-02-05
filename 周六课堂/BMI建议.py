weitht = input("请输入体重(千克):")
weitht = float(weitht)

height = input("请输入身高(米):")
height = float(height)

bmi = weitht / height / height

if 20 <= bmi <= 25:
    print("正常")
elif bmi < 20:
    print("偏瘦")
elif bmi > 25:
    print("偏胖")