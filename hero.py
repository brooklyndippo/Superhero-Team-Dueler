import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    # add OFFENSIVE abilities
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    # add DEFENSIVE abilities
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block   

    def take_damage(self, damage):
        defense = self.defend()
        if defense < damage:
            self.current_health -= (damage - defense)
        return self.current_health

    #match up opponents for fight
    def fight(self, opponent):
        total_power = self.current_health + opponent.current_health

        if self.abilities == [] and opponent.abilities == []:
            print('DRAW')
            return

        #run the fighting while both heros are still alive
        while self.is_alive() == True and opponent.is_alive() == True:
            print('fighting')
            self.take_damage(opponent.attack())
            #print(f'slf: {self.current_health}')
            opponent.take_damage(self.attack())
            #print(f'opp: {opponent.current_health}')

        #print the results once one or both players are dead
        if self.current_health <= 0 and opponent.current_health <= 0:
            print('DRAW')

        elif self.current_health > opponent.current_health:
            print(f'{self.name} defeats {opponent.name}.')

        else:
            print(f'{opponent.name} defeats {self.name}.')

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True



#run test code only in this file
if __name__ == "__main__":
    slf = Hero("Grace Hopper")
    opp = Hero("Dumbledore")
    ability = Ability('snort', 30)
    opp.add_ability(ability)
    slf.add_ability(ability)
    print(slf.abilities)
    slf.fight(opp)
