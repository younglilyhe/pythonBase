'''
import random
one = 1
two = 2

print("Hello Python")

test1 = input("test1 ")
test2 = input("test2 ")
test3 = int(test1) * int(test2)
print(test3)

name = "何莉"
print("I am %s " % name)

number1 = 1.5
number2 = 5
number3 = 7.5
print("This is %.2f,%.3f,%.4f" % (number1, number2, number3))
print("百分数：%.0f%%" % (number1 *100))

random1 = random.randint(1, 10)
print(random1)

i = 1
while i <= 5:
    print(i)
    i = i + 1
print(i)

i = 0
while i < 10:
    if i == 5:
        # break
        i += 1
        continue
    print(i)
    i += 1
print("over")


row = 1
while row <= 5:
    print("*" * row)
    row += 1

row = 1
while row <= 5:
    col = 1
    print("第 %d 行 " % row, end="")
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    row += 1


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

print("1 2 3")
print("10 20 30\n")

print("1\t2\t3")
print("10\t20\t30")
'''

