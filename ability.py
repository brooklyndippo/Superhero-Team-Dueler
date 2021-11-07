import random

class Ability:
    def __init__ (self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack_amount = random.randint(0, self.max_damage)
        return attack_amount


if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  ability = Ability("Debugging Ability", 20)
  print(ability.name)
  print(ability.attack())