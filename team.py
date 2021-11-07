import random

class Team:
    def __init__(self, name=''):
        self.name = name
        self.heroes = list()
    
    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0: 
                kd = hero.kills / hero.deaths
                print (f'{hero.name} Kills/Deaths: {kd*100}%')
            else:
                print (f'{hero.name} Kills: {hero.kills}')

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        #Battle the teams against each other

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            hero.fight(opponent)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if not hero.is_alive():
                living_heroes.remove(hero)
            if not opponent.is_alive():
                living_opponents.remove(opponent)


