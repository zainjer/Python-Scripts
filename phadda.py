import random

class Player:
  name = "player"
  level = 0
  classType = "Fighter"


  def __init__(self,name,classType):
    self.name = name
    self.classType = classType
    self.level = random.randrange(1,99,1)

  def attack(p1,p2):
    print("Larai Shuru!\n")
    
    if p1.level > p2.level:
      print(str(p1.level)+" lvl  -VS-  "+str(p2.level)+" lvl")
      print(p1.name+" of Class "+p1.classType+ " Defeated "+p2.name+" of Class "+p2.classType)
    elif p2.level > p1.level:
      print(str(p1.level)+" lvl  -VS-  "+str(p2.level)+" lvl")
      print(p2.name+" of Class "+p2.classType+ " Defeated "+p1.name+" of Class "+p1.classType)
    elif p1.level == p2.level:
      print("Jani WTF?")
      print("The match between"+p1.name+" and "+p2.name+" was tied. What a waste of time :(")
  

while 1:
  print("\n----------Phadda Emulator------------\n")
  
  print("Enter Player1 Name:")
  p1n = input()
  print("Enter Player1 Class:")
  p1c = input()

  print("Enter Player2 Name:")
  p2n = input()
  print("Enter Player2 Class:")
  p2c = input()
  print(" ")

  p1 = Player(p1n,p1c)
  p2 = Player(p2n,p2c)

  p1.attack(p2)

  print(" ")


# p1 = Player("Ammi","Chappal")

# p2 = Player("Abbu","Danda")

# p1.attack(p2)
