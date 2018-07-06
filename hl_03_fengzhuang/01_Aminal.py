class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def sleep(self):
        print("sleep")

    def play(self):
        print("play")


class Dog(Animal):
    def bark(self):
        print("bark")

class XTQ(Dog):
    def bark(self):
        print("XTQbark")



xtq = XTQ()
xtq.bark()
