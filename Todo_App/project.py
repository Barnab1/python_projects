#Simple To-Do List Application:

#Goal: Create a command-line and after a basic GUI (using Tkinter) application to manage tasks.
#Skills: Variables, lists, loops, conditional statements, basic file I/O (to save/load tasks).
#Progression: Add features like task prioritization, due dates, and task completion tracking.


# PROJECT DEPTH EXPLANATION 
"""
Functionality and user interaction

    - actions performed by user: add, view, complete as done, delete

    - way user interact with application: Commmand line input

    - type of input : text prompts

    - type of output:  formatted list

    - Tasks should be ordered by description priority

        -Priorities are ('Must do':'M','should do':'S','could do':'C', 'Will not do':'W')

    - How will the user identify which task to mark as complete or delete (by description)

    - What feedback should the user receive after each action? (Confirmation messages when everything is 
    fine, error message when there is a mistake)

Data structures and Storage

    - How will the tasks be stored in memory while the application is running? (List of dictionaries)

    - information to store for each task: (Description, status, due date, priority)

    - If using a list of dictionaries, what keys will the dictionaries have? (e.g., 'description', 'status', 'due_date', 'priority').

    - How will the application handle an empty task list ('tell user that we want to delete it and proceed if they confirm/ask user to update')

    - I don't need to store the date or time the task was added, just the due_date
    
3. Error Handling and Edge Cases:

    - What happens if the user enters invalid input? : Throw a TypeError.

    - What happens if the user tries to mark a task as complete that doesn't exist: Throw a message 
        saying that the task doesn't exist
    - What happens if the user tries to delete a task that doesn't exist "Throw a message saying:
        the task doesn't exist)
    - What happens if the user inputs nothing for the task description: The task should keep coming
        again and again

4. Code Organization and Modularity:

    - How will the code be organized into functions : (One function per action).

    - How will data be passed between functions: passed as arguments:
        Eg: def add_task(tasks, new_task): # tasks list passed as an argument
            def view_tasks(tasks): # tasks list passed as an argument

    - How can the code be made reusable and maintainable (throgh the use of small chunk of function 
        with meaningfull name)
    
    - main modules or components of the application:

        - Input/Output Module: This would handle getting user input (e.g., task descriptions, menu choices)
            and displaying output (e.g., the list of tasks, confirmation messages). In a 
            command-line application, this module is basically the main loop, and all the print and input 
            functions

        - Data Storage/Manipulation Module: This would handle storing the tasks (the list of dictionaries we 
            discussed earlier) and performing operations on them (adding, completing, deleting). 
            These are your core functions that manipulate the list

        - (Later, in Phase 2) File I/O Module: This would handle saving and loading the tasks to/from a file
        
        - (Later, in Phase 3) GUI Module: If we add a GUI, this would handle the GUI elements and their interactions

"""
from tabulate import tabulate
# PROJECT CODE

#STEP 1: Initializing the Task List

tasks = []

# Step 2: Create the add_task() Function

def add_task(tasks):
    """
    Responsible for adding task to tasks list
    """
    print('Hi Dear We are here in Todo App to help you managing well your time.')
    print('')
    print('Give the following descriptions for your task')

    taskDescription = input('Task description: ')
    taskDueDate     = input('Task due date: ')
    taskPriority    = input('Task priority: ')
    taskstatus ='pending'

    task = {}

    task['description'] = taskDescription
    task['due date'] = taskDueDate
    task['priority']   = taskPriority
    task['status'] = taskstatus

    tasks.append(task)

    print('Your Task was well added to your Todos')
    return tasks



# Step 3: Create the view_tasks() Function



def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    headers = ["#", "Description", "Status", "Priority"]
    table_data = []

    for i, task in enumerate(tasks):
        table_data.append([i + 1, task['description'], task['status'], task['priority']])
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    
tasks = [{'description':'Go to church ', 'status':'pending', 'priority':'M'},
         {'description':'Go to school', 'status':'pending', 'priority':'M'},
         {'description':'Go to job', 'status':'done', 'priority':'M'}
]




def completTask(task):

    print('Hi Dear, here you can mark task as completed to remove them')

    for task in tasks:
        if task['status'] != 'completed':
            print('Would you like to mark below task as completed. Answer by y(yes) or n(no)')
            print(task['description'])
            userInput = input('answer here')



def menuLoop():
    """
    Showing the main menu
    """
    keepGoing = True

    while keepGoing:

        print("Welcome to your Todo App")
        print("")
        print('Menu'.center(20, "-"))
        print("1. Add task,")
        print("2. View tasks")
        print("3. Exit.")

        userInput = int(input('Choose an option: '))

    
        if userInput == 1:
            add_task(tasks)
        elif userInput == 2:
            view_tasks(tasks)
        elif userInput ==3:
            keepGoing = False
        else:
            print('Invalid choice')

menuLoop()
"""

Run this code: Try running this basic version of your application.
Experiment: Add the complete task functionality.
Test: Test your code thoroughly to make sure it works as expected.
Expand: add the delete task functionality.
"""

