num1 = True
num2 = True
num3 = True


for x in range(100,500):
    if int(str(x)[0])%2 == 0:
        num1 = False
    if int(str(x)[1])%2 == 0:
        num2 = False
    if int(str(x)[2])%2 == 0:
        num3 = False
    if num1 and num2 and num3:
        print(x)
    num1 = True
    num2 = True
    num3 = True

