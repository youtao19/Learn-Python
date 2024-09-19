f = None

try:
    f = open("test.txt")
    content = f.read()
    print(content)
    f.close()
except Exception as e:
    print(e)

import test_pacage.test

test_pacage.test.hello()
