f = None

try:
    f = open('文件写入写出综合案例\\test_append.txt')
    content = f.read()
    print(content)
    f.close()
except Exception as e:
    print(e)
