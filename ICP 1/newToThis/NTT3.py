newString = input("Enter a sentence: ")
numbers = 0
letters = 0
words = 1

for i in newString:
    if i.isupper() or i.islower():
        letters+=1
    elif i.isspace():
        words+=1
    elif i.isdigit():
        numbers+=1

print("Letters:", letters, "Words:", words, "Digits:", numbers)
