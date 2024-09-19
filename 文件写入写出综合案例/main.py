f = open("D:\codes\Python\pythonProject\文件写入写出综合案例\\bill.txt",'r',encoding='utf-8')
f2 = open("D:\codes\Python\pythonProject\文件写入写出综合案例\\bill.txt.bak",'w',encoding='utf-8')
for line in f:
    line = line.strip()
    if line.split(",")[-1] == "测试":
        continue
    f2.write(line)
    f2.write("\n")
f.close()
f2.close()



