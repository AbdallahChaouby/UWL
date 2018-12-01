number1= input("Enter first number ")
number2= input("Enter second number ")
result= number1 + number2
print("The result for the wrong one would be:" +result)
#This wont work because python views these as different strings, putting the
#numbers next to each other. A correct way to do it is:
number1= int(input("Enter first number "))
number2= int(input("Enter first number "))
result = number1+number2
print("This is the answer for the right one: ",+result)
