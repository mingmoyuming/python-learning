import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(1,10)
    def move(self):
        self.x -= 1
        print("我们现在所在的位置是：",self.x,self.y)

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass

class Shark(Fish):
    def  __init__(self):
        Fish.__init__(self)
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有得吃~(　＾∀＾)")
            self.hungry = False
        else:
            print("太多了，吃撑了！")
