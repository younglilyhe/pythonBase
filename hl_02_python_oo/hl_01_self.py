class Cat:

    def __init__(self):
        print("这是一个初始化方法")

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)

# 使用类名（）创建
Tom = Cat()