# =====importing libraries===========
from datetime import date
import datetime
import os

# ======= Defining Functions =======


def admin_menu():
    while True:
        menu = input(
            """Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
st - Statistics
gr - Generate reports
e - Exit
: """
        ).lower()

        # Calling on functions after selecting the corresponding menu option
        if menu == "r":
            reg_user(menu)

        elif menu == "a":
            add_task(menu)

        elif menu == "va":
            view_all(menu)

        elif menu == "vm":
            view_mine(menu)

        elif menu == "st":
            total_stats(menu)

        elif menu == "gr":
            generate_report(menu)

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


def non_admin_menu():
    while True:
        menu = input(
            """Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: """
        ).lower()

        # Calling on functions after selecting the corresponding menu option
        if menu == "a":
            add_task(menu)

        elif menu == "va":
            view_all(menu)

        elif menu == "vm":
            view_mine(menu)

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have made a wrong choice, Please Try again")


def reg_user(selection):
    # Opening user.txt as append and referencing it as f_out
    with open("user.txt", "a") as f_out:
        # Using while loop and if statements to check if new user is already in the credentials dictionary or not and outputting the correct response
        while True:
            new_user = input("Please enter the name of the new user: ")
            if new_user in credentials:
                print("This user already exists, please try another name")

            if new_user not in credentials:
                new_password = input(f"Please enter the password for {new_user}: ")
                break
            # Using while loop to check that the passwords match
        while True:
            confirm_password = input(f"Please re-enter the password for {new_user}: ")
            # Using if statement to check that both passwords match and writing to file
            if confirm_password == new_password:
                f_out.write("\n" + new_user + ", " + new_password)

                print(f"{new_user} has been added, they can now access the system")

                break

            else:
                print("The passwords did not match, please try again")


def add_task(selection):
    # Opening tasks.txt as append and assigning it as f_out
    with open("tasks.txt", "a+") as f_out:
        task_user = input("Please enter the name of the user that will undertake this task: ")

        task_title = input("What is the title of the task?\n")

        task_description = input("What will the task include?\n")

        task_date = input("Please enter the due date for the task in (dd Month YYYY) format: ")

        date_added = date.today()

        date_output = date_added.strftime("%d %B %Y")

        completed = "No"
        # Writing task to tasks.txt if required format
        f_out.write(
            "\n" + task_user + ", " + task_title + ", " + task_description + ", " + task_date + ", " + date_output + ", " + completed
        )

        print("The new task has been added, please select another option:")


def view_all(selection):
    # Opening tasks.txt as read and assigning it as f
    with open("tasks.txt", "r") as f_read:
        tasks = f_read.readlines()
        assigned_tasks = []
        # Using for statement and enumerate to iterate through the tasks in the file and assign a task id, adding it to a new dictionary.
        for count, task in enumerate(tasks, 1):
            task = task.strip().split(", ")
            assigned_task = {
                "id": count,
                "task": task[1],
                "assigned_to": task[0],
                "date_assigned": task[4],
                "due_date": task[3],
                "task_complete": task[5],
                "description": task[2],
            }
            assigned_tasks.append(assigned_task)
        # Using a for loop to print the tasks in a user-friendly manner
        for task in assigned_tasks:
            print("\u2500" * 100)
            print(
                f"Task ID:\t\t {task['id']}\n"
                f"Task:\t\t\t {task['task']}\n"
                f"Assigned to:\t\t {task['assigned_to']}\n"
                f"Date Assigned:\t\t {task['date_assigned']}\n"
                f"Due date:\t\t {task['due_date']}\n"
                f"Task Complete?\t\t {task['task_complete']}\n"
                f"Task Description:\n {task['description']}"
            )
            print("\u2500" * 100)


def view_mine(selection):
    # Using with to open tasks.txt as read and assigning it as f
    with open("tasks.txt", "r") as f_read:
        tasks = f_read.readlines()
        assigned_tasks = []
        # Using for statement and enumerate to iterate through the tasks in the file and assign a task id, adding it to a new dictionary.
        for count, task in enumerate(tasks, 1):
            task = task.strip().split(", ")
            if user_name == task[0]:
                assigned_task = {
                    "id": count,
                    "task": task[1],
                    "assigned_to": task[0],
                    "date_assigned": task[4],
                    "due_date": task[3],
                    "task_complete": task[5],
                    "description": task[2],
                }
                assigned_tasks.append(assigned_task)
        # Using a for loop to print the tasks in a user-friendly manner
        for task in assigned_tasks:
            print("\u2500" * 100)
            print(
                f"Task ID:\t\t {task['id']}\n"
                f"Task:\t\t\t {task['task']}\n"
                f"Assigned to:\t\t {task['assigned_to']}\n"
                f"Date Assigned:\t\t {task['date_assigned']}\n"
                f"Due date:\t\t {task['due_date']}\n"
                f"Task Complete?\t\t {task['task_complete']}\n"
                f"Task Description:\n {task['description']}"
            )
            print("\u2500" * 100)

        task_id = input("Enter the task ID you want to edit or enter -1 to exit: ")

        if task_id == "-1":
            print("Returning to main menu")
            pass
        elif task_id:
            # Using for loop to iterate through tasks in newly created dictionary and check if it is complete, if not then asks user to edit specified information
            for task in assigned_tasks:
                if task["task_complete"].lower() == "yes":
                    print("You cannot edit tasks that are already complete, returning to main menu")
                elif int(task_id) == task["id"]:
                    print(f"Editing task {task_id}: {task['task']}")
                    task["assigned_to"] = input("Enter the username you wish the task to be assigned to: ")
                    task["due_date"] = input("Enter the updated due date or enter the current one to keep it the same: ")
                    task["task_complete"] = input("Is the task complete? (Yes/No): ")
                    break
                else:
                    print("Invalid task ID!")

            with open("tasks.txt", "w") as f_write:
                # Using for loop to iterate through tasks, if user_name isnt the same as the name assigned in the task write back to file
                for line in tasks:
                    task = line.rstrip()
                    if user_name != task.split(", ")[0]:
                        f_write.write(task + "\n")
                # Using for loop to iterate through tasks, checking if user has more than one task to see if it needs newline and writing newly updated information to file
                for i, task in enumerate(assigned_tasks):
                    task_line = f"{task['assigned_to']}, {task['task']}, {task['description']}, {task['due_date']}, {task['date_assigned']}, {task['task_complete']}"
                    if i < len(assigned_tasks) - 1:
                        task_line += "\n"
                    f_write.write(task_line)


def total_stats(selection):
    task_file = "task_overview.txt"
    user_file = "user_overview.txt"

    if os.path.exists(task_file):
        with open("task_overview.txt", "r") as f_read:
            for line in f_read.readlines():
                print(line)

    else:
        generate_report(selection)

    if os.path.exists(user_file):
        with open("user_overview.txt", "r") as f_read:
            for line in f_read.readlines():
                print(line)

    else:
        generate_report(selection)


def generate_report(selection):
    today = datetime.datetime.now()
    # Using with to open file as read and assigning it f_read
    with open("tasks.txt", "r") as f_read:
        unsorted_tasks = f_read.readlines()
        completed_tasks = 0
        incomplete_tasks = 0
        task_total = len(unsorted_tasks)
        overdue_task = 0
        # Using for loop to iterate through the tasks in file and if statements to sort tasks in to complete and incomplete
        for task in unsorted_tasks:
            tasks = task.strip().split(", ")
            if tasks[5].lower() == "yes":
                completed_tasks += 1
            else:
                incomplete_tasks += 1
            # Using if statement to check if the current date is greater than the one within the task using strptime()
            if today > datetime.datetime.strptime(tasks[3], "%d %B %Y") and tasks[5].lower() == "no":
                overdue_task += 1
        # Calculating the percentages
        incomplete_percent = (incomplete_tasks / task_total) * 100
        overdue_percent = (overdue_task / task_total) * 100
        # Writing to task_overview.txt the following information
        with open("task_overview.txt", "w") as file:
            file.write(
                f"Task Overview\n"
                f"Total tasks: {task_total}\n"
                f"Completed tasks: {completed_tasks}\n"
                f"Incomplete tasks: {incomplete_tasks}\n"
                f"Overdue tasks: {overdue_task}\n"
                f"Percentage of Incomplete tasks: {round(incomplete_percent, 2)}%\n"
                f"Percentage of Overdue tasks: {round(overdue_percent, 2)}%"
            )
    # Using with to open fil as read and assigning it f_read
    with open("user.txt", "r") as f_read:
        unsorted_users = f_read.readlines()
        total_users = len(unsorted_users)
        # Using for loot to iterate through the tasks in file and if statements to sort though tasks in to required outputs
        for user in unsorted_users:
            users = user.strip().split(", ")
            user_names = {"name": users[0]}
            user_tasks = 0
            user_completed = 0
            user_incomplete = 0
            user_overdue = 0

            for task in unsorted_tasks:
                tasks_user = task.strip().split(", ")
                if user_names["name"] == tasks_user[0]:
                    user_tasks += 1

                    if tasks_user[5].lower() == "yes":
                        user_completed += 1
                    elif tasks_user[5].lower() == "no":
                        user_incomplete += 1

                    if today > datetime.datetime.strptime(tasks_user[3], "%d %B %Y") and tasks_user[5].lower() == "no":
                        user_overdue += 1
            # Using if statement to check if user tasks is 0 or not to avoid error dividing by zero
            if user_tasks > 0:
                user_percentage = (user_tasks / task_total) * 100
                user_completed_percentage = (user_completed / user_tasks) * 100
                user_incomplete_percentage = (user_incomplete / user_tasks) * 100
                user_overdue_percentage = (user_overdue / user_tasks) * 100
            else:
                user_percentage = 0
                user_completed_percentage = 0
                user_incomplete_percentage = 0
            # Writing required information to file
            with open("user_overview.txt", "a") as f_out:
                f_out.write(
                    f"User Overview\n"
                    f"Total users registered: {total_users}\n"
                    f"Total tasks: {task_total}\n"
                    f"User: {user_names['name']}\n"
                    f"Tasks assigned to user: {user_tasks}\n"
                    f"Percentage of tasks assigned to user: {round(user_percentage, 2)}%\n"
                    f"Completed user tasks: {round(user_completed_percentage, 2)}%\n"
                    f"Incomplete user tasks: {round(user_incomplete_percentage, 2)}%\n"
                    f"Overdue user tasks: {round(user_overdue_percentage)}%\n"
                    "\n"
                )

        print("Report generated!")


# ====Login Section====
credentials = dict()

with open("user.txt", "r") as f:
    # Using for to iterate through the lines in user.txt
    for line in f:
        if not line.strip():
            continue
        # Using .rstrip to strip "\n" and .split to seperate the strings in the dictionary
        username, password = line.rstrip("\n").split(", ", 1)
        # Add entry to credentials for username and password
        credentials[username] = password

while True:
    user_name = input("Please enter your username: ")
    # Using if statement to loop through keys in dictionary and checking if user entry is there
    if user_name not in credentials:
        print("That's not a recognised username, please try again")

        continue
    # Retrieve password for given user - if username not in credentials, it returns None
    pass_word = credentials.get(user_name)
    # Ensure lookup was successful - if key does not exist pass_word will be none
    if pass_word is None:
        print("This user does not exist")

        continue
    # Using if to check if pass_word is not what user entered
    if pass_word != input("Please enter your password: "):
        print("Password is not correct, please try again!")

        continue

    print(f"Welcome, {user_name}. What would you like to do?")
    # Using if to check if user_name is admin and loading the correct menu
    if user_name != "admin":
        non_admin_menu()

    elif user_name == "admin":
        admin_menu()

    break


# For task_overview.txt and user_overview.txt the wording of the task is a little confusing when asking that the text files
# should output data in a user-friendly, easy to read manner, I wasn't sure if you are asking me to make the .txt file easy to
# read or the information easy to read like in the view_all function so I've created the .txt files as if they were to be viewed by the user.
