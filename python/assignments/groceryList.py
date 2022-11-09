#ask user for their email of phone number
#keep grocery list for user
#make sure I have an empty list
#use a while look to keep collecting grocery
#ask user if they are done to exit loop, maybe look for a keyword in the input to stop the loop. 

def getGroceryItem ():
    print ("What do you want to add to your list?")
    item = input()
    return item

groceryList = []

def groceryListBanner():
    print (
 '''
   _____                                 _      _     _   
  / ____|                               | |    (_)   | |  
 | |  __ _ __ ___   ___ ___ _ __ _   _  | |     _ ___| |_ 
 | | |_ | '__/ _ \ / __/ _ \ '__| | | | | |    | / __| __|
 | |__| | | | (_) | (_|  __/ |  | |_| | | |____| \__ \ |_ 
  \_____|_|  \___/ \___\___|_|   \__, | |______|_|___/\__|
                                  __/ |                   
                                 |___/ 
'''
    )

answer = "initial"
while len(answer) > 0:
    #print(groceryListBanner)
    print("Type in a new item to add it to the list or press enter to quit")
    answer = getGroceryItem()
    print(groceryList)
    if answer != '':
        groceryList.append(answer)

print(groceryList)




