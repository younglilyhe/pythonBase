"""字典中的CRUD"""
"""
lily_dict = {"name": "lily",
             "gender": False,
             "age": 25
             }
print(lily_dict)
print(lily_dict.keys())
print(lily_dict.values())
print(lily_dict.items())
print(lily_dict["name"])
lily_dict["height"] = 160
lily_dict["long_hair"] = True
lily_dict["name"] = "lilyhe"
lily_dict["age"] = 24
print(lily_dict)

temp_dict = {"name": "lily",
             "gender": False,
             "age": 25,
             "weight": 45
             }
lily_dict.update(temp_dict)
print(lily_dict)
lily_dict.pop("weight")
print(lily_dict)
for k in lily_dict:
    print("%s - %s " % (k, lily_dict[k]))
    
print(lily_dict.clear())


# string的模拟
name_string = "lily and tongs"
print(len(name_string))
print(name_string.count("lily"))
print(name_string.index("lily"))
space = " \t\n\r"
print(space.isspace())

print(name_string.startswith("lily"))
print(name_string.endswith("tongs"))
print(name_string.find("and"))
print(name_string.replace("lily", "others"))
print(name_string)

poem = ["\t昔人已乘黄鹤去，此地空余黄鹤楼。",
        "黄鹤一去不复返，白云千载空悠悠。",
        "晴川历历汉阳树，芳草萋萋鹦鹉洲。\t\n",
        "日暮乡关何处是？烟波江上使人愁。"]
print(poem)
for poem_str in poem:
    # print(poem_str.strip().center(25))
    print("|%s|" % (poem_str.center(50).strip()))
"""

poem_str = "昔人已乘黄鹤去\t此地空余黄鹤楼\t黄鹤一去不复返\t\n白云千载空悠悠\t晴川历历汉阳树\t\t芳草萋萋鹦鹉洲"
print(poem_str)
poem_list = poem_str.split()  # split()返回一个列表,默认是将空白字符作为字符
print(poem_list)
result = " ".join(poem_list)
result1 = ",".join(poem_list)
print(result)
print(result1)

poem = ["昔人",
        "黄鹤一去",
        "晴川历历汉阳树，芳草萋萋鹦鹉洲。",
        "日暮乡关何处是？烟波江上使人愁。"]
for poem_str1 in poem:
    print(poem_str1.ljust(10))
    print(poem_str1.rjust(20, " "))


    
