total_amount = 0
bank_action = None
#These are the variables used in the program

while(bank_action != "Finish"):
#a while loop that allows the user to input their bank transactions

    bank_action = input()
    #user input for transaction

    if bank_action != "Finish":
    #error checking to make sure the loop doesn't run when the user tries to quit

        bank_action = bank_action.split()
        #splits the bank action to make it easier to read

        #below: determining what command to do and what to do with the amount given
        if str(bank_action[0]) == "Deposit":
            total_amount = total_amount + int(bank_action[1])
        elif str(bank_action[0] == "Withdraw"):
            total_amount = total_amount - int(bank_action[1])

print("Total Amount: $", total_amount)
#printing result