users = { "Kosta" : "Baller", "Liv" : "Pasgis", "Donald" : "Trash Boy"}

def checkUser (username):
    if username in users:
        return True
    else:
        return False

def getUser (username):
    fullname = users[username]
    return fullname

def login ():
    print ("Enter your username:")
    kosta = input()
    username = kosta
    return username

user = login()
validUser = checkUser(user)
if validUser == True:
    print ("Hello " + getUser(user))
    print ("Login Successful, Have a great day!")
if validUser == False:
    print("That username is incorrect, try again ")

while (validUser == False):
    user = login()
    validUser = checkUser(user)

print ("Hello " + getUser(user))
print ("Login Successful, Have a great day!")
