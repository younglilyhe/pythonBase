class MusicPlayer(object):
    """
    # 元组参数，字典参数
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 2.为对象分配空间
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance

    # 只有返回对象的引用才会执行初始化方法
    def __init__(self):
        print("播放器初始化")
    """

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init__flag = False

    def __new__(cls, *args, **kwargs): \
            # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        """需求：让初始化动作只被执行一次"""
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init__flag:
            return
        # 2.如果没有执行过，再执行初始化动作
        print("初始化播放器")

        # 3.修改类属性的标记
        MusicPlayer.init__flag = True



# 创建播放器对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
