class Animal(object):
    def run(self):
        print('animal is running...')


class dog(Animal):
    def run(self):
        print('dog is running..')

class cat(Animal):
    def run(self):
        print('cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

class totoise(Animal):
    def run(self):
        print('totoise is running slowly...')
