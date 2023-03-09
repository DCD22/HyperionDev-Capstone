# =====importing libraries===========
'''This is the section where you will import libraries'''

# ====Login Section====
username = []

password = []

with open('user.txt', 'r') as f:

    for line in f:

        data = line.strip()
        data = line.split(", ")

        username.append(data[0])

        password.append(data[1])

    while True:

        user_name = input("Please enter your username: ")

        if user_name in username:

            pass_word = input("Thanks, please enter your password: ")

            if pass_word in password:

                print(f"Welcome, {user_name}. What would you like to do?")

                break

            else:
                print("That password is not correct, please try again")

        else:
            print("That's not a recognised username, please try again")

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass

        with open("user.txt", "a") as f:

            new_user = input("Please enter the name of the new user: ")

            new_password = input(f"Please enter the password for {new_user}: ")

            while True:

                confirm_password = input(f"Please re-enter the password for {new_user}: ")

                if confirm_password == new_password:

                    f.write("\n" + new_user + ", " + new_password)

                    print(f"{new_user} has been added, they can now access the system")

                    break

                else:

                    print("The passwords did not match, please try again")


    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
