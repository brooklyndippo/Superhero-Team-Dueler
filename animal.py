class Animal:
    def __init__ (self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')


class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def jump(self):
        print(f'{self.name} is jumping.')

animal = Animal ('Larry')
frog = Frog ('Frank')

#the following should work:
animal.eat()
animal.drink()
frog.eat()
frog.drink()
frog.jump()

#the following should throw an error:
animal.jump()