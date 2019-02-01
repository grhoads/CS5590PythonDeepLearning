list = ["1", "4", "0", "6", "9"]
print(list)

placeHolder = list[2]

list[1:2] = list[0:2]
list[0] = placeHolder
del(list[3])

print(list)