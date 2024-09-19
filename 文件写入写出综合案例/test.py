f = None

try:
    f = open(r'文件写入写出综合案例\\test_append.txt')
    content = f.read()
    print(content)
    f.close()
except Exception as e:
    print(e)


from test_package import test   
test_package.test.hello()
