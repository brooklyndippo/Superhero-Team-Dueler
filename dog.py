# dog.py
class Dog:
  # Required properties are defined inside the __init__ constructor method
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print('dog intialized!')
    self.introduce()

  def bark(self):
    print('Woof!\n')

  def introduce(self):
    print(f'{self.name} is a {self.breed}.\n')

  def sit(self):
    print(f'{self.name} sits.\n')

  def rollover(self):
    print(f'{self.name} rolls over.\n')


