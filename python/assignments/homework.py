import hashlib

def askForItems():
    print("How many items do you have to add to your list")
    itemCount = input()
    if itemCount.isdigit():
        return int(itemCount)
    else:
        print("Looks like you had an error, please try again.")
        askForItems()

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    username = str(hashlib.sha256(username.encode('utf-8')).hexdigest())
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    if password == "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9" and username == "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9":
        print('Welcome!')
        break
    else:
        print('Access denied. Try again.')
        count += 1
else: print('Unable to login at this time!')

print(" Please Begin to Enter Each receipt for calculation")
numberOfReceiptItems = 0
numberOfReceiptItems = askForItems()
receiptList = []
listGenCounter = 0
while numberOfReceiptItems < listGenCounter:
    print("Enter your line item")
    receiptList = input('Line Item')


