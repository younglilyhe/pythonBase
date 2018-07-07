class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象数量
    count = 0

    @classmethod
    def show_tool_count(cls):
        """输出使用当前这个类，创建对象的个数"""
        # 访问当前类的属性cls.count
        print("工具对象的数量 %d" % cls.count)    # cls代表当前调用的类。

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool1 = Tool("榔头")
tool1 = Tool("锄头")


# 调用类方法，第一个参数cls，就是只指向哪个类。Tool
Tool.show_tool_count()
