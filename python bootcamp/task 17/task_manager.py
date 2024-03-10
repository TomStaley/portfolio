# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


#====<Create Functions>====

def reg_user() -> None:
    '''Adds a user to user.txt, and is called when the user selects "r".'''
    # - Request input of a new username
    new_username = input("New Username: ")

    # - Check if the username already exists
    if new_username in username_password.keys():
        print("That username already exists!")
        return

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")
    return


def add_task() -> None:
    '''Adds a task to tasks.txt, and is called when the user selects "a".'''
    task_username = input("Name of person assigned to task: ")

    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()

    #Add the data to the file task.txt and Include 'No' to indicate if the task is complete.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    update_tasks(task_list)

    return


def view_all() -> None:
    '''View all tasks in tasks.txt, called when the user selects "va".'''
    task_list = retrieve_tasks()
    print()

    #Loops through each task a displays the info
    for task_number, t in enumerate(task_list, 1):
        display_task(t, task_number)


def view_mine() -> None:
    '''View all tasks belonging to a user, called when the user selects "vm".'''
    task_list = retrieve_tasks()
    #using an enumerate to count each task. This includes tasks for other users.
    #tasks from other users CAN'T be selected
    task_no_list = []
    print()

    #loops through each task, checks the username, and then displays the info
    for task_number, t in enumerate(task_list, 1):
        task_no_list.append(task_number)
        if t['username'] == curr_user:
            display_task(t, task_number)

    #edit options
    vm_select_task(task_no_list, task_list)


def display_task(t, task_number):
    '''Formats task data into a readable format'''
    disp_str = f"Task ID: \t {task_number}\n"
    disp_str += f"Task: \t\t {t['title']}\n"
    disp_str += f"Assigned to: \t {t['username']}\n"
    disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: \n {t['description']}\n"
    disp_str += f"Completed? \t {t['completed']}\n"
    disp_str += "-------------------------------------------------------------------\n"
    print(disp_str)


def vm_select_task(task_no_list, task_list):
    '''Used within view_mine(), selects a task from the list and applys changes'''

    #select a task
    task_select = int(input("Would you like to select a specific task? (Select using task ID, -1 to go back to menu) "))
    if task_select == -1:
        return
    if task_select not in task_no_list:
        print("that is not a valid task ID! Returning to menu...")
        return

    task_edit = str(input("Would you like to mark this task as complete (1), or edit this task (2)? "))

    for task_number, t in enumerate(task_list, 1):
        if task_number == task_select:

            #mark as complete
            if task_edit == "1":
                task_complete(t, task_list)

            #edit the task
            elif task_edit == "2":

                #check if completed
                if t['completed'] is True:
                    print("\nCan't edit task because it's already complete!")
                    return

                edit_task(t, task_list)

            else:
                print("That is not a valid input!")
                return
            return
    task_list = retrieve_tasks()
    return


def task_complete(t, task_list):
    '''Used to complete a task.'''
    t['completed'] = not t['completed']
    update_tasks(task_list)


def edit_task(t, task_list):
    '''Used to choose edit options for a task.'''
    task_edit2 = str(input("You can edit who the task belongs to (1) or the duedate (2): "))

    #edit the task's user - note: currently doesn't check if the new user is in user.txt
    if task_edit2 == "1":
        task_edit_user(t, task_list)

    #edit the duedate
    elif task_edit2 == "2":
        task_edit_duedate(t, task_list)

    else:
        print("That is not a valid input!")
        return


def task_edit_user(t, task_list):
    '''Used to edit a tasks user.'''
    new_user = str(input("Who is the new user? "))
    t['username'] = new_user
    update_tasks(task_list)


def task_edit_duedate(t, task_list):
    '''Used to edit a tasks due date.'''
    while True:
        try:
            new_due = input("What is the new due date (YYYY-MM-DD)? ")
            new_due_time = datetime.strptime(new_due, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    t['due_date'] = new_due_time
    update_tasks(task_list)


def update_tasks(task_data) -> None:
    '''Used to update task data in tasks.txt, takes task_list as a parameter.'''
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_data:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Tasks successfully updated.")


def retrieve_tasks() -> list:
    '''Used to retrive the list of tasks from tasks.txt.'''
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    task_list = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = True if task_components[5] == "Yes" else False

        task_list.append(curr_t)

    return task_list


def retrieve_users() -> dict:
    '''Retrieves a dictionary  of user names and passwords.'''

    #read in user data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    # Convert to a dictionary
    username_password = {}
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password
    return username_password


def gen_reports():
    '''Generates reports for the user.'''
    gen_task_over()
    gen_user_over()


def gen_user_over():
    '''Generates user_overview.txt, which contains an overview of user data.'''

    #get updated user and task lists
    username_password = retrieve_users()
    task_list = retrieve_tasks()

    #get todays date
    curr_date = date.today()

    #Total Number of users
    total_users = len(username_password)

    #Total number of tasks
    total_tasks = len(task_list)

    out_str = f'''
    Total Number of users:  {total_users}
    Total number of tasks:  {total_tasks}

-------------------------------------------------------------------
'''

    #for each user:
    for u in username_password:

        #The user in this iteration
        temp_user = u

        #Total number of tasks assigned to that user
        total_user_tasks = 0

        #Percentage of the total number of tasks assigned to the user
        percent_user_t_total = 0

        #Percentage of the tasks assigned to the user that have been completed
        total_user_t_done = 0
        percent_user_t_done = 0

        #Percentage of the tasks assigned to the user that are incomplete
        total_user_t_not = 0
        percent_user_t_not = 0

        #percentage of the tasks assigned to the user that are incomplete and overdue
        total_user_t_over = 0
        percent_user_t_over = 0

        for t in task_list:
            if t['username'] == u:
                total_user_tasks += 1
                if t['completed'] is True:
                    total_user_t_done += 1
                elif t['completed'] is False:
                    total_user_t_not += 1
                    if t['due_date'].date() < curr_date:
                        total_user_t_over += 1

        #Prevent divide by zero
        if total_user_tasks == 0:
            pass
        else:
            #Maths to work out percentages
            percent_user_t_total = (total_user_tasks / total_tasks) * 100
            percent_user_t_done = (total_user_t_done / total_user_tasks) * 100
            percent_user_t_not = (total_user_t_not / total_user_tasks) * 100
            percent_user_t_over = (total_user_t_over / total_user_tasks) * 100

        out_str_temp = f'''
User:                                                   {temp_user}

Total number of tasks assigned:                         {total_user_tasks}
Percentage of the total number of tasks assigned:       {percent_user_t_total}
Percentage of the tasks assigned that are complete:     {percent_user_t_done}
Percentage of the tasks assigned that are incomplete:   {percent_user_t_not}
Percentage of the tasks assigned that are overdue:      {percent_user_t_over}

-------------------------------------------------------------------
'''
        out_str += out_str_temp

    with open("user_overview.txt", 'w') as user_ov_file:
        user_ov_file.write(out_str)     


def gen_task_over():
    '''Generates task_overview.txt, which contains an overview of task data.'''

    #get updated task list
    task_list = retrieve_tasks()

    #get todays date
    curr_date = date.today()

    #total tasks
    total_tasks = len(task_list)

    #total complete tasks
    total_tasks_done = 0

    #total incomplete tasks
    total_tasks_not = 0

    #total overdue tasks
    total_tasks_over = 0

    #percentage of tasks incomplete
    percent_tasks_not = 0

    #percentage of tasks overdue
    percent_tasks_over = 0

    #math to work out totals and percentages
    for t in task_list:
        if t['completed'] == True:
            total_tasks_done += 1
        elif t['completed'] == False:
            total_tasks_not += 1
            if t['due_date'].date() <= curr_date:
                total_tasks_over += 1
    percent_tasks_not = (total_tasks_not / total_tasks) * 100
    percent_tasks_over = (total_tasks_over / total_tasks) * 100

    out_str = f'''
    Total number of tasks:  {total_tasks}
    Total tasks completed:  {total_tasks_done}
    Total tasks incomplete: {total_tasks_not}
    Total tasks overdue:    {total_tasks_over}

    Percentage of tasks incomplete: {percent_tasks_not}%
    Percentage of tasks overdue:    {percent_tasks_over}%

-------------------------------------------------------------------
'''
    #generates report for each task
    for t in task_list:
        disp_str = f'''
Task:               {t['title']}
Assigned to:        {t['username']}
Date Assigned:      {t['assigned_date']}
Due Date:           {t['due_date']}
Completed?          {t['completed']}
Task Description: 
    {t['description']}
-------------------------------------------------------------------
'''
        out_str += disp_str

    with open("task_overview.txt", 'w') as task_ov_file:
        task_ov_file.write(out_str)


##MAIN CODE

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

task_list = retrieve_tasks()

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

username_password = retrieve_users()

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        reg_user()

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        add_task()

    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
        view_all()

    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        view_mine()

    elif menu == 'gr':
        gen_reports()
        print("Reports generated!")

    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        #Updates the info for users a tasks from the txt files
        task_list = retrieve_tasks()
        username_password = retrieve_users()
        
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
