class Runnable(object):
    def run(self):
        print('Running....')

class Flyable(object):
    def fly(self):
        print('Flying')
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class dog(Mammal,Runnable):
    pass

class bat(Mammal,Flyable):
    pass

class parrot(Bird):
    pass
class Ostrich(Bird):
    pass


