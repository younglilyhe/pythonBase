# define定义九九乘法表的函数
def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")     # 先验证行的正确输出
            # print("1 * 2 = 2   ", end="")   # 再验证整个乘法表的样子
            print("%d * %d = %d" % (col, row, col * row), end="\t")  # 最后整体的乘法表样子,注意齐问题\t
            col += 1
        print("")
        row += 1


name = "lily"


def say_hello():
    """say hello to someone"""

    print("hello 1")
    print("hello 2")
    multiple_table()


"""
print(name)
say_hello()
print(name)
"""


def sum_2_num(num1, num2):
    """define 2 numbers to sum"""
    result = num1 + num2
    # print("%d + %d = %d" % (num1, num2, result))
    return result

"""
sum_result = sum_2_num(10, 20)
print("sum is %d" % sum_result)
"""


def print_line(char, times):
    """print 分隔线"""
    print(char * times)


# print_line("*", 50)


def print_lines(char, times):
    """打印多行分隔线

    :param char: 分隔的字符
    :param times: 分割线重复的次数
    """
    row = 1
    while row <= 5:
        print_line(char, times)
        row += 1


