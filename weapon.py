from ability import Ability
import random

class Weapon(Ability):

    def attack(self):
        half_damage = self.max_damage//2
        attack_amount = random.randint(half_damage, self.max_damage)
        return attack_amount


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  nunchucks = Weapon("Ninja", 100)
  print(nunchucks.name)
  print(nunchucks.attack())