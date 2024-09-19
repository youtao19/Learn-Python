import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("I Love You"))
print(my_utils.str_util.substr("Nice to meet YOU",2,6))



file_util.append_to_file('test_append.txt',"现在正在测试")
file_util.print_file_info('test_append.txt')