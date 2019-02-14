user_input = input("Type any sequence of characters:\n")
#asking for the string to be used

x=0
y=1
#placeholder variables for seperating the input

inputstring = []
#empty list that will store each individual character of the input

for j in range(0,len(user_input)):
#putting input into inputstring list by splitting the input up by characters
    for i in user_input[x:y]:
        inputstring.append(i)
        x=x+1
        y=y+1


count = 0
temp_string = []
#initializing a count that will help parse the inputstring list and a temp_string list that will hold the result

string_list = []

for i in inputstring:
    if i in temp_string:
        string_list.append(temp_string)
        temp_string = []
        temp_string.append(i)

    else:
        temp_string.append(i)
string_list.append(temp_string)

result = []
for i in string_list:
    if len(i)>len(result):
        result = i

final = ""
for i in result:
    final = final + i

print("Longest substring without repeating characters followed by length:")
print(final, ",", len(final))