import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("I Love You"))
print(my_utils.str_util.substr("Nice to meet YOU",2,6))

file_util.append_to_file("文件写入写出综合案例\\test_append.txt","添加成功")
file_util.print_file_info("文件写入写出综合案例\\test_append.txt")