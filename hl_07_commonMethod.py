list_ = ["string", 6]
print(list_[0])
print("string" not in list_)

dict_ = [
    {"name": "张三"},
    {"name": "李四"}
]

find_name = "王五"
for dict_key in dict_:
    if dict_key["name"] == find_name:
        print("%s 找到了" % dict_key["name"])
        break
else:
    print("sorry, %s not found" % find_name)
