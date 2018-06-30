a = 1
print(id(1))
print(id(a))
b = a
print(id(b))
a = 2
print(id(2))
print(id(b))
b = a
print(id(b))


def test():
    result = "hello"
    print("函数要返回的数据的内存地址是 %d" % id(result))
    return result


a = test()
print("%s 的内存地址是 %d" % (a, id(a)))