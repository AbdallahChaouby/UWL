count=0
while count < 5:
    password = input ("Please enter password: ")
    if password == 'changeme':
        print("Welcome")
        break
    else:
        print ("Wrong password, try again")
        count += 1
print("Access denied, please press enter to exit and contact security to reset your password")
input("Press enter to exit")


