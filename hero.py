import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    # add OFFENSIVE abilities
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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

        #print the results if both players die at the same time
        if self.current_health <= 0 and opponent.current_health <= 0:
            print('DRAW')
            self.add_kill(1)
            opponent.add_kill(1)
            self.add_death(1)
            opponent.add_death(1)

        #if SELF is the winner
        elif self.current_health > opponent.current_health:
            print(f'{self.name} defeats {opponent.name}.')
            self.add_kill(1)
            opponent.add_death(1)

        #if OPPONENT is the winner
        else:
            print(f'{opponent.name} defeats {self.name}.')
            opponent.add_kill(1)
            self.add_death(1)

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    #track game stats for kills and deaths
    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths



#run test code only in this file
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
    #--
    slf = Hero("Grace Hopper", 1000)
    opp = Hero("Dumbledore")
    ability = Ability('snort', 30)
    opp.add_ability(ability)
    slf.add_ability(ability)
    print(slf.abilities)
    slf.fight(opp)
