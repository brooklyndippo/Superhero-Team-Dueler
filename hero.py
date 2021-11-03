import random

class Hero:
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
      total_power = self.current_health + opponent.current_health

      #calculate the odds of each winning
      hero_odds = self.current_health/total_power*100
      opp_odds = opponent.current_health/total_power*100
      print(hero_odds)
      print(opp_odds)

      winning_num = random.randint(0,100)
      #if the random 1-100 number is less than percent chance of hero1 winning, make winner
      if winning_num < hero_odds:
          print(f'{self.name} defeats {opponent.name}.')
      else:
          print(f'{opponent.name} defeats {self.name}.')



#run test code only in this file
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 450)
    hero2 = Hero("Dumbledore", 200)
    hero1.fight(hero2)

