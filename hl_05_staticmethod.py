class Dog(object):
    @staticmethod
    def run():

        # 不需要访问实例属性/方法和类属性/方法
        print("小狗要跑...")


# 通过类名，调用静态方法 - 不需要创建对象
Dog.run()


class Game (object):
    # 类属性：历史最高分
    top_score = 0

    def __init__(self, name):
        # 实例属性：在初始化方法内部实现
        self.player_name = name

    @staticmethod
    def show_help():
        # 既不访问类属性/方法也不访问实例属性/方法，所以用实例方法
        print("显示游戏帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        # 要访问类属性/方法，所以用类方法
        print("显示历史最高分：%d" % cls.top_score)

    def start_game(self):
        # 要访问实例属性/方法，所以用实例方法
        print("开始当前玩家 %s 的游戏" % self.player_name)


Game.show_help()
Game.show_top_score()
game = Game("xiaoming")
game.start_game()

