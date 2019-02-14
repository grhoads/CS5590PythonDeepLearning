student_list = [( 'John', ('Physics', 80)) , ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
#The list given in project description

sorted_dict = {}
#initializing a dictionary to sort the list into

for i in student_list:
#looping through list of touples for sorting

    temp_student = str(i).split()
    temp_student[0] = temp_student[0].replace("(", "")
    temp_student[0] = temp_student[0].replace(",", "")
    temp_student[2] = temp_student[2].replace("))",")")
    #cleaning up some of the unwanted characters

    for j in range(0,2):
    #more cleanup
        temp_student[j] = temp_student[j].replace("'","")

    if temp_student[0] in sorted_dict:
    #Where the magic happens. If Else that checks for a repeat key and then adds the class and student or just the student depending on duplicate entries
        sorted_dict[temp_student[0]] = sorted_dict[temp_student[0]] + temp_student[1] + temp_student[2]
    else:
        sorted_dict[temp_student[0]] = temp_student[1] + temp_student[2]

print(sorted_dict)
#Printing to display the newly sorted dictionary