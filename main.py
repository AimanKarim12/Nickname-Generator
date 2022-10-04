#NICKNAME GENERATOR
import random

randomname = ["Crusher", "Quick Silver", "Twinkle-Toes", "The Assasin", "The Crafter", "The Destroyer", "The Great", "Guardian Of Light", "Frost-Walker", "Demon-Slayer", "The Elementalist"]
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")

loop = True
while loop: 

    #PRINT MAIN MENU
    print("MAIN MENU" , "(" , firstname, lastname , ")")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")

    select = input ("Enter Selection (1-6): ")

      #CHANGE NAME
    if select == "1":
      print("CHANGE NAME")
      firstname = input("What is your first name? ")
      lastname = input("What is your last name? ")
      
      #RANDOM
    elif select == "2":
      print("RANDOMIZE NICKNAME")
      print(firstname, random.choice(randomname), lastname)
      
      #ALL NICKNAMES
    elif select == "3":
      print("ALL NICKNAMES")
      for x in randomname:
        print(firstname, x, lastname)

      #ADD
    elif select == "4":
      print("ADD A NAME")
      y = input("ENTER A NAME TO ADD: ")
      if y in randomname:
        print("NAME ALREADY EXISTS")
      else:
        print(y, "HAS BEEN ADDED")
        randomname.append(y)

      #REMOVE
    elif select == "5":
      print("REMOVE A NAME")
      removename = input("ENTER A NAME TO REMOVE: ")
      if removename not in randomname:
        print("NAME DOES NOT EXIST")
      else:
        randomname.remove(removename)
        print("NAME HAS BEEN REMOVED")

      #EXIT
    elif select == "6":
      print("EXIT")
      loop = False