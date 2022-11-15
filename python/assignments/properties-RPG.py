import random

propertiesList = { 1 : "Poison Resist" ,  2 : "Strength" , 3 : "Walking Speed" , 4 : "Armor" , 
5 : "Vitality" , 6 : "Mana Siphon" , 7 : "Critical Hit Chance" , 8 : "Critical Hit Damage" , 9 : "Vitality Siphon" }

def propertyValue():
     number = random.randint(50, 1500)
     return number

def giveProperty():
    value = random.choice(list(propertiesList.values()))
    return value

count = 0

while count < 3:
	print(str(giveProperty()) + ' ' + str(propertyValue()))
	count = count + 1