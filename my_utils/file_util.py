"""
函数：print_file_info(file_name)，接收传入文件的路径，打印文件的全部内
容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
函数：append_to_file(file_name，data)，接收文件路径以及传入数据，将
追加写入到文件中
"""


def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="utf-8")
        context = f.read()
        print(context)
    except Exception as e:
        print(f"发生了异常,{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f = open(file_name,"a",encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    append_to_file("文件写入写出综合案例\\bill.txt","追加成功4")
    print_file_info("文件写入写出综合案例\\bill.txt")