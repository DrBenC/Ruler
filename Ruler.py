from os import system, name
from time import sleep as slp
import random

def d(n):
    return random.randint(1, n)

def cls(): 
    if name == 'nt': 
        _ = system('cls') 

def OpenScreen():
    print("You have been invested with absolute power over the resources of your country.\n")
    country = input("What was the name of that country, again? :")
    ruler = input("And how should we refer to you, your Grace? :")
    print("Thank you - "+ruler+" of "+country)
    return country, ruler

country, ruler = OpenScreen()
morale = 50
soldiers = 500
gold = 500
date = 1

def HUD():
    cls()
    global morale
    global soldiers
    global gold
    global date
    print("-- "+str(morale)+" morale -- "+str(soldiers)+" soldiers -- "+str(gold)+" gold -- Day "+str(date)+" --\n")
    print("\n")
    print("\n")
    print("It is day "+str(date)+" under your rule.\n")

def FirstScreen():
    global morale
    global date
    HUD()
    a = d(20)
    #print (a)
    if a > 8:
        print("It is a beautifully sunny day.")
        morale = morale + 2
    else:
        print("It rains heavily.")
        morale = morale - 2
    date += 1
    
def SecondScreen():
    HUD()
    global morale
    global soldiers
    global date
    global ruler
    a = d(20)
    if a > 0:
        print ("A farmer petitions you for aid for the village of Blackstone, which is being held hostage by bandits.")
        farmer_second = input("How many soldiers do you send to aid him?: ")
        
        while farmer_second.isdigit() == False or int(farmer_second) < 0 or int(farmer_second) > soldiers:
            farmer_second = input("Please put a valid number: ")
                    
        if int(farmer_second) == 0:
            print("You refuse his plea. It does a citizen good to take care of things themselves sometimes.")
            morale -= 10
        else:
            print("You send "+str(farmer_second)+" soldiers to help the man. He thanks you.")
            morale += 5
            soldiers -= int(farmer_second)
    date += 1
    return farmer_second

def ThirdScreen():
    HUD()
    global morale
    global soldiers
    global date
    global ruler
    global gold
    global farmer_second
    a = d(20)
    if int(farmer_second)+a > 30:
        print("The tax collector returns from the surrounding villages. He brings a hoard of gold.")
        gold += 100
    else:
        print("The tax collector returns from the surrounding villages. He was robbed of his funds on the way.")
    date+= 1
        
def FourthScreen():
    HUD()
    global morale
    global soldiers
    global date
    global ruler
    global gold
    global farmer_second
    if int(farmer_second) == 0:
        print("Merchants are complaining about losses due to unsafe roads.")
        print("They are requesting a royal loan of 200 gold to keep their business going.")
        merchants = input("Do you give it to them? (y/n) :")
        while merchants != "y" and merchants != "n":
            merchants = (input("Do you give the merchants the loan? (y/n): "))
        if merchants == "y":
            gold -= 200
            print("They thank you and hurry off to invest the money.")
            merchants_l = 1
        elif str(merchants) == "n":
            print("They leave quietly, obviously unhappy with your rule.")
            morale -= 30
            merchants_l = 0
        
    else:
        print("No-one petitions you today.")
        merchants_l = 0
    date += 1
    return merchants_l
    
def FifthScreen():
    HUD()
    slp(1)
    global morale
    global soldiers
    global date
    global ruler
    global gold
    global farmer_second
    
        
FirstScreen()
slp(1)
farmer_second = SecondScreen()
slp(1)
ThirdScreen()
slp(1)
merchants_loan = FourthScreen()
slp(1)
FifthScreen()
slp(2)

