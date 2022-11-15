import random
import os 

clear = lambda: os.system('clear')

propertiesList = { 1 : "Poison Resist" ,  2 : "Strength" , 3 : "Walking Speed" , 4 : "Armor" , 
5 : "Vitality" , 6 : "Mana Siphon" , 7 : "Critical Hit Chance" , 8 : "Critical Hit Damage" , 9 : "Vitality Siphon" }

def propertyValue():
     number = random.randint(50, 1500)
     return number

def giveProperty():
    value = random.choice(list(propertiesList.values()))
    return value

x = 0
print ("Here are your initial values:")

attribute = giveProperty()
points = propertyValue()
skillsDictonary = {1:(str(giveProperty())) + " " + str(propertyValue()), 2: (str(giveProperty()) + " " + str(propertyValue())), 3: (str(giveProperty()) + " " + str(propertyValue()))}
print(skillsDictonary)

print("Are you happy with your selection?")
satisfied = input()
if satisfied == 'Y':
    quit()
if satisfied == 'N':
    print("Which Selection Would You Change?")
    choice = int(input())
    skillsDictonary.update({choice:(str(giveProperty())) + " " + str(propertyValue())})
    print(skillsDictonary)
