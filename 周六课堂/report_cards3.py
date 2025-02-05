stu1_name = input("请输入学生的姓名:")
stu1_score1 = input("请输入该同学科目1 的成绩：")
stu1_score2 = input("请输入该同学科目2 的成绩：")
stu1_sco1 = float(stu1_score1)
stu1_sco2 = float(stu1_score2)

stu1_to_scr = stu1_sco1 + stu1_sco2
stu1_avg_score = stu1_to_scr/2

print("        ***期末成绩单***       ")
print("姓名    科目1    科目2    总成绩    平均分")
print("----------------------------------------")
print(stu1_name,"    ",stu1_sco1,"  ",stu1_sco2,'    ',stu1_to_scr,'    ',stu1_avg_score)
print("----------------------------------------")
