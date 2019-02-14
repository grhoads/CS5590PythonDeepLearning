python_list = ["Billy","Joey","Miranda","Katy","Jessica","Daniel"]
web_app_list = ["Miranda","Ron","Billy","Jessica","Xavier","Gavin"]
#Lists representing 2 different school classes, with some differences and similarities to demonstrate program working

print("Type C for List of students common in Python and Web Application, and N for students not common in both classes")
what_list = input("Type P for Only Python List, and W for Only Web Application List\n")
#command prompt to show user their choices for input and viewing lists

if what_list == 'N':
#evaluationg user choice
    print("Showing Students NOT common in both classes")

    print("Python List:")
    for i in python_list:
    #checking for students in python list and printing them as long as they are not common in both lists
        if i not in web_app_list:
            print(i)

    print("Web Application List")
    for i in web_app_list:
    #doing the same as above but printing web app list instead
        if i not in python_list:
            print(i)

elif what_list == 'C':
#evaluating user input

    print("Students in Python and Web Application List")
    for i in python_list:
    #checking both lists against each other to see if the student is in both classes
        for j in web_app_list:
            if i == j:
                print(i)

elif what_list == 'P':
#evaluating user choice

    print("Python List:")
    for i in python_list:
    #simply printing out the students in the python list
        print(i)

elif what_list == 'W':
#evaluationg user choice

    print("Web Application List:")
    for i in web_app_list:
    #simply printing out the students in the web app list
        print(i)



