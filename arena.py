from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from validate_input import validate_input

class Arena:
    def __init__(self):
        self.team_one = Team('team_one')
        self.team_two = Team('team_two')

    def create_ability(self):
        name = input('What is the ability name?  ')
        max_damage = validate_input('What is the max damage of the ability?  ', int)
        return Ability (name, max_damage)    

    def create_weapon(self):
        name = input('What is the weapon name?  ')
        max_damage = validate_input('What is the max damage of the weapon?  ', int)
        return Weapon (name, max_damage)    

    def create_armor(self):
        name = input('What is the armor name?  ')
        max_block = validate_input('What is the max block of the armor?  ', int)
        return Armor (name, max_block)  

    def create_hero(self):
        hero_name = input("Hero's name:  ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        numOfTeamMembers = validate_input("How many members would you like on team one?\n", int)
        #numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = validate_input("How many members would you like on team two?\n", int)
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # Calculate K/D ratio for team 1:
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f'{self.team_one.name} " average K/D was: {str(team_kills/team_deaths*100)}%')

        # Calculate K/3 ratio for team 2
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f'{self.team_two.name} " average K/D was: {str(team_kills/team_deaths*100)}%')
        print("\n")

        team_one_survivors = list()
        team_two_survivors = list()

        #surviving heroes team 1
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                team_one_survivors.append(hero.name)
                print("survived from " + self.team_one.name + ": " + hero.name)

        #survivng heroes team 2
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                team_two_survivors.append(hero.name)
                print("survived from " + self.team_one.name + ": " + hero.name)

        #declare a WINNER
        if len(team_one_survivors) > len(team_two_survivors):
            print("Team One WINS!")
        else:
            print("Team Two WINS!")



                

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
