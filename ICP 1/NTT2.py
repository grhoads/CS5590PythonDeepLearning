userNum1 = int(input("Enter a number: "))
userNum2 = int(input("Enter another number: "))

userChoice = input("Would you like to add/subtract/multiply/divide: ")
result = 0

if userChoice == 'add':
    result = userNum1+userNum2
elif userChoice == 'subtract':
    result = userNum1-userNum2
elif userChoice == 'multiply':
    result = userNum1*userNum2
elif userChoice == 'divide':
    result = userNum1/userNum2

print("Here is your result:", result)
