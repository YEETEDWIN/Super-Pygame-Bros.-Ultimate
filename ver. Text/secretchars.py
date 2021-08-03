#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import random, time, sys
from player import Player
from operator import add, mul, sub, truediv
import json

# Cijo class
class Celements(Player):
  def __init__(self):
    Player.__init__(self, "Celements")
    self.moves.pop("attack")
    self.moves.pop("heal")
    self.moves["jump and kick"] = self.attack
    self.moves["random smash"] = self.rand_smash
    self.moves["iceflake"] = self.iceflake
    self.moves["flaming food"] = self.hot_food

  def rand_smash(self, enemy):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    choice = ['water','flame','earth','grass']
    chosen = []
    choosers1 = random.choice(letters)
    choosers2 = random.choice(letters)
    choosers3 = random.choice(letters)
    chosen.append(choosers1)
    chosen.append(choosers2)
    chosen.append(choosers3)
    element = random.choice(choice)
    if element == 'water':
      water = ['w','a','t','e','r']
      water.extend(chosen)
      random.shuffle(water)
      water2 = ''.join(water)
      print("")
      print(water2)
      print("")
      quest = input("Which type of element can be made with these letters\n>")
      if quest == 'water':
        print("Correct answer!")
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(10,20)
        self.attack(enemy, damage)
    if element == 'flame':
      flame = ['f','l','a','m','e']
      flame.extend(chosen)
      random.shuffle(flame)
      flame2 = ''.join(flame)
      print("")
      print(flame2)
      print("")
      quest = input("Which type of element can be made with these letters\n>")
      if quest == 'flame':
        print("Correct answer!")
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(10,20)
        self.attack(enemy, damage)
    if element == 'earth':
      earth = ['e','a','r','t','h']
      earth.extend(chosen)
      random.shuffle(earth)
      earth2 = ''.join(earth)
      print("")
      print(earth2)
      print("")
      quest = input("Which type of element can be made with these letters\n>")
      if quest == 'earth':
        print("Correct answer!")
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(10,20)
        self.attack(enemy, damage)
    if element == 'grass':
      grass = ['g','r','a','s','s']
      grass.extend(chosen)
      random.shuffle(grass)
      grass2 = ''.join(grass)
      print("")
      print(grass2)
      print("")
      quest = input("Which type of element can be made with these letters\n>")
      if quest == 'grass':
        print("Correct answer!")
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(10,20)
        self.attack(enemy, damage)

  def iceflake(self, enemy):
    if random.random() <= 0.1:
      self.attack(enemy, 70)
    else:
      self.attack(enemy, 20)
  
  def hot_food(self, enemy):
    choice = input("Do you want to eat it ('eat') or burn your opponent ('burn')?\n>")
    if choice != 'eat' and choice != 'burn':
      while True:
        print("Invalid input.")
        choice = input(">")
        if choice == 'eat' or choice == 'burn':
          break
    if choice == 'eat':
      if random.random() <= 0.75:
        heal = random.randint(20,50)
        heal *= self.energy
        self.health += round(heal) 
        print(self.name, "healed self", heal)
      else:
        heal = random.randint(20,30)
        heal *= self.energy
        self.health += round(heal) 
        print(self.name, "healed self", heal)
    if choice == 'burn':
      if random.random() <= 0.75:
        damage = random.randint(20,50)
        self.attack(enemy, damage)
      else:
        damage = random.randint(20,30)
        self.attack(enemy, damage)


# Himagno class
class Lazemagnum(Player):
  def __init__(self):
    Player.__init__(self, "Lazemagnum")
    self.moves.pop("attack")
    self.moves["laser punch"] = self.attack
    self.moves["magnum whip"] = self.magnum_whip
    self.moves["flame spinning laser"] = self.spinning_laser
    self.moves["flaming beam"] = self.invis_laser
    self.plasma = 0

  def magnum_whip(self, enemy):
    print("Anwser correctly to increase plasma and damage the enemy")
    num = random.randint(2,20)
    num2 = random.randint(1,12)
    operators = {"+": add, "-": sub, "*": mul, "/": truediv}
    keys = list(operators)
    operator = random.choice(keys)
    quest = int(input("What is {} {} {} equal to?".format(num,operator, num2)))
    if quest == (operators[operator](num, num2)):
      print("You increased your plasma!")
      self.plasma += 20
      damage = 10+self.plasma
      self.attack(enemy, damage)
    else:
      damage = 10+self.plasma
      self.attack(enemy, damage)


# Raphael class
class Sanic(Player):
  def __init__(self):
    Player.__init__(self, "Sanic")
    self.moves.pop("attack")
    self.moves.pop("heal")
    self.moves["run!"] = self.run_meme
    self.moves["gotta go fast"] = self.gofast_meme
    self.moves["cumon step it up!"] = self.sanic_meme
    self.moves["super sanic"] = self.super_sanic
    self.memes_used = 0
    self.times_used = 0
    self.sanic_mode = False
    self.sanicgod_mode = False

  def run_meme(self, enemy):
    print("RUN! du, du, du, du, du, du, du, du, du, du, du, du, du, du")
    time.sleep(1)
    sys.stdout.write("\033[F") #back to previous line 
    sys.stdout.write("\033[K") #clear line
    print("'Meme continues...'")
    chance = 20 + self.memes_used*3
    meme_chance = random.randint(1,chance)
    self.attack(enemy, meme_chance)
    self.memes_used += 1
  
  def gofast_meme(self, enemy):
    self.memes_used += 1
    print("Gotta go fassst, gotta goo faast!")
    time.sleep(2)
    sys.stdout.write("\033[F") #back to previous line 
    sys.stdout.write("\033[K") #clear line
    print("'Meme continues...'")
    code = ["⚫️","⎻",""]
    symbol1 = random.choice(code)
    symbol2 = random.choice(code)
    symbols = symbol1+symbol2
    print("Below shall be a morse code... Anwser with the correct letter (if none type Nothing)")
    quest = input(symbols+'\n>')
    if symbols == "":
      if quest == "Nothing":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⚫️⎻":
      if quest == "A":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⎻":
      if quest == "T":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⎻⎻":
      if quest == "M":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⚫️":
      if quest == "E":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⎻⚫️":
      if quest == "N":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)
    elif symbols == "⚫️⚫️":
      if quest == "I":
        damage = random.randint(30,40)
        self.attack(enemy, damage)
      else:
        damage = random.randint(1,10)
        self.attack(enemy, damage)

  def sanic_meme(self, enemy):
    if self.sanic_mode:
      choice = 40 + self.memes_used*5
      damage = random.randint(20,choice)
      self.attack(enemy, damage)
      self.memes_used += 1
    elif self.sanicgod_mode:
      choice = 40 + self.memes_used*7
      damage = random.randint(30,choice)
      self.attack(enemy, damage)
      self.memes_used += 1
    else:
      damage = random.randint(20,35)
      self.attack(enemy, damage)
      self.memes_used += 1

  def super_sanic(self, enemy):
    self.sanic_mode = True
    self.health += 40
    print("I am now super SANIC mode!")
    self.times_used += 1
    if self.times_used >= 3:
      self.moves["super sanic god"] = self.sanic_god
      print('You earned the "super sanic god" form')
      self.moves.pop("super sanic")

  def sanic_god(self, enemy):
    self.sanicgod_mode = True
    self.health += 150
    self.energy += 1.2
    self.attack(enemy, 30)
    print("I am now super SANIC GOD mode!")
    self.moves.pop("super sanic god")


# Goku class
class Goku(Player):
  def __init__(self):
    Player.__init__(self, "Goku")
    self.moves.pop("attack")
    self.moves.pop("heal")
    self.moves["ki blast - 100"] = self.blast
    self.moves["regeneration"] = self.heal
    self.moves["charge"] = self.charge
    self.moves["energy wave - 250"] = self.wave
    self.moves["kamehameha - 400"] = self.kamehameha
    self.moves["spirit bomb - 250"] = self.bomb
    self.moves["dragon fist - 300"] = self.fist
    self.moves["super saiyan - 650"] = self.saiyan
    self.movescount = 0
    self.saiyan_mode = True
    self.saiyanblue_mode = False
    self.ki_decrease = 0
    self.questionsList = []
    self.questionsIndex = 0

  def blast(self, enemy, damage=-1):
    self.movescount += 1
    ki = 100
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if damage == -1:
        damage = random.randint(20, 40)
      damage *= self.energy
      damage = round(damage)
      enemy.health -= damage
      print(self.name, "did", damage, "damage to", enemy.name)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def charge(self, enemy):
    self.movescount += 1
    ki = 0
    ki -= self.ki_decrease
    if self.ki >= ki:
      if self.saiyanblue_mode:
        increase = random.randint(250,450) + self.ki_decrease
        self.ki += increase
      else:
        self.ki -= ki
        increase = random.randint(100,250) + self.ki_decrease
        self.ki += increase
  
  def wave(self, enemy):
    self.movescount += 1
    ki = 250
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      damage = random.randint(30,50)
      self.attack(enemy, damage)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def kamehameha(self, enemy):
    self.movescount += 1
    ki = 400
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if self.saiyan_mode:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(80,200)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
      else:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(30,90)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def bomb(self, enemy):
    self.movescount += 1
    ki = 250
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      damage = random.randint(40,70)
      self.attack(enemy, damage)
      self.attack(self, 45)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def fist(self, enemy):
    self.movescount += 1
    ki = 0
    ki -= self.ki_decrease
    if self.ki >= ki:
      if self.saiyan_mode:
        self.ki -= ki
        quest = input("Are you worthy of taking the dragon's power (yes = y and no = n)\n>")
        if quest == "n":
          damage = random.randint(35,50)
          self.attack(enemy, damage)
        elif quest == "y":
          data = json.loads(open("Text Wars/data.json", "r", encoding="utf-8"))
          t = data["question"]
          self.attack(enemy)
      else:
        print("You were not on super saiyan mode!")
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def saiyan(self, enemy):
    self.movescount += 1
    ki = 650
    if self.ki >= ki:
      if self.movescount >= 3:
        self.moves.pop("ki blast - 100")
        self.moves.pop("energy wave - 250")
        self.moves.pop("kamehameha - 400")
        self.moves.pop("spirit bomb - 250")
        self.moves.pop("dragon fist - 300")
        self.moves.pop("super saiyan - 650")
        self.moves["super saiyan blue - 700"] = self.saiyan_blue
        self.moves["ki blast - 50"] = self.blast2
        self.moves["kamehameha - 350"] = self.kamehameha2
        self.moves["spirit bomb - 200"] = self.bomb2
        self.moves["dragon fist - 250"] = self.fist2
        self.saiyan_mode = True
        self.ki -= ki
        self.ki_decrease = 50
        self.energy += 0.3
      else:
        print("You only had played {} moves. You need to play 3 moves. You got another 100 ki for wasting your move".format(self.ki))
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100
  
  def blast2(self, enemy, damage=-1):
    self.movescount += 1
    ki = 100
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if damage == -1:
        damage = random.randint(20, 40)
      damage *= self.energy
      damage = round(damage)
      enemy.health -= damage
      print(self.name, "did", damage, "damage to", enemy.name)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def kamehameha2(self, enemy):
    self.movescount += 1
    ki = 400
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if self.saiyan_mode:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(80,200)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
      else:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(30,90)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def bomb2(self, enemy):
    self.movescount += 1
    ki = 250
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      damage = random.randint(40,70)
      self.attack(enemy, damage)
      self.attack(self, 45)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def fist2(self, enemy):
    self.movescount += 1
    ki = 300
    ki -= self.ki_decrease
    if self.ki >= ki:
      if self.saiyan_mode:
        self.ki -= ki
        quest = input("Are you worthy of taking the dragon's power (yes = y and no = n)")
        if quest == "n":
          damage = random.randint(35,50)
          self.attack(enemy, damage)
        elif quest == "y":
          questions = {
            {'What is the name of Universe 7\'s God of Destruction?','beerus'},
            {'Who created the Dragon Balls?','kami'},
            {''}
            }
          question = random.choice(questions)
          print(question)
          quest2 = input("")
          self.attack(enemy)
      else:
        print("You were not on super saiyan mode!")
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def saiyan_blue(self, enemy):
    ki = 700
    if self.ki >= ki:
      if self.movescount >= 8:
        self.moves.pop("ki blast - 50")
        self.moves.pop("kamehameha - 350")
        self.moves.pop("spirit bomb - 200")
        self.moves.pop("dragon fist - 250")
        self.moves.pop("super saiyan blue - 700")
        self.moves["mastered ultra instinct - 1600"] = self.instinct
        self.moves["ki blast"] = self.blast3
        self.moves["kamehameha - 300"] = self.kamehameha3
        self.moves["dragon fist - 200"] = self.fist3
        self.saiyanblue_mode = True
        self.ki -= ki
        self.ki_decrease += 50
        self.energy += 0.3
      else:
        print("You only had played {} moves. You need to play 8 moves. You got another 100 ki for wasting your move".format(self.ki))
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def blast3(self, enemy, damage=-1):
    self.movescount += 1
    ki = 100
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if damage == -1:
        damage = random.randint(20, 40)
      damage *= self.energy
      damage = round(damage)
      enemy.health -= damage
      print(self.name, "did", damage, "damage to", enemy.name)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def kamehameha3(self, enemy):
    self.movescount += 1
    ki = 400
    ki -= self.ki_decrease
    if self.ki >= ki:
      self.ki -= ki
      if self.saiyan_mode:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(80,200)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
      else:
        if random.random() <= 0.35:
          print("KAME-HAME-HAAAAA")
          damage = random.randint(30,90)
          self.attack(enemy, damage)
        else:
          print("KAME-HAME-... I forgot the last bit")
          damage = random.randint(1,45)
          self.attack(enemy, damage)
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def fist3(self, enemy):
    self.movescount += 1
    ki = 300
    ki -= self.ki_decrease
    if self.ki >= ki:
      if self.saiyan_mode:
        self.ki -= ki
        quest = input("Are you worthy of taking the dragon's power (yes = y and no = n)")
        if quest == "n":
          damage = random.randint(35,50)
          self.attack(enemy, damage)
        elif quest == "y":
          questions = {
            {'What is the name of Universe 7\'s God of Destruction?','beerus'},
            {'Who created the Dragon Balls?','kami'},
            {''}
            }
          question = random.choice(questions)
          print(question)
          quest2 = input("")
          self.attack(enemy)
      else:
        print("You were not on super saiyan mode!")
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100

  def instinct(self, enemy):
    ki = 1600
    if self.ki >= ki:
      if self.movescount >= 15:
        self.ki -= ki
        self.energy += 0.3
      else:
        print("You only had played {} moves. You need to play 15 moves. You got another 100 ki for wasting your move".format(self.ki))
        self.ki += 100
    else:
      print("You only had {} ki for yourself. You got another 100 ki for wasting your move".format(self.ki))
      self.ki += 100


# Katsuhiko class
class OnePunchMan(Player):
  def __init__(self):
    Player.__init__(self, "One Punch Man")
    self.moves.pop("attack")
    self.moves.pop("heal")
    self.moves["normal punch"] = self.attack
    self.moves["serious side hops"] = self.heal
    self.moves["consecutive normal punches"] = self.attack_many
    self.moves["serious punch"] = self.ser_punch
    self.moves["serious headbutt"] = self.ser_butt

  def attack_many(self, enemy):
    damage = random.randint(20, 40)
    damage = damage*2.5
    round(damage)
    self.attack(enemy, damage)

  def ser_punch(self, enemy):
    if random.random() >= 0.7:
      self.attack(enemy, 50)
    else:
      self.attack(enemy, 30)
  
  def ser_butt(self, enemy):
    self.attack(enemy, 70)
    self.attack(self, 15)
