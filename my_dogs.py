from dog import Dog

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)


my_chonky_dog = Dog('Lola', 'Bulldog')
my_borkin_dog = Dog('Harold', 'Chihuahua')
my_long_dog = Dog('Nigel', 'Doxen')

my_long_dog.rollover()
my_chonky_dog.sit()

my_borkin_dog.bark()
print(f'- says {my_borkin_dog.name}')