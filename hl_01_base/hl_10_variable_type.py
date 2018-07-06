# 列表
a = [1, 2, 3]
print(id(a))
a.append("4")
print(a)
print(id(a))
a.remove(2)
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
a = [2, 4, 6]
print(id(a))


print()

# 字典
dict = {"name": "xiaoming"}
print(id(dict))
dict["age"] = 25
print(dict)
print(id(dict))
dict.pop("name")
print(dict)
print(id(dict))
dict["name"] = "xiaoxiaoming"
print(dict)
print(id(dict))
dict = {"name": "xiaohong"}
print(dict)
print(id(dict))


# 字典的key
d = {}
d[1] = "Integer"
d["name"] = "String"
d[(1,)] = "Tuple"
print(d)


