# A simple app to help people organizing their future task by priority and deadlines
 
"""
Priorities are ('Must do':'M','should do':'S','could do':'C', 'Will not do':'W')

        
- (Later, in Phase 3) GUI Module: If we add a GUI, this would handle the GUI elements and their interactions

"""
from tabulate import tabulate
from datetime import datetime
import json
# PROJECT CODE

#STEP 1: Initializing the Task List

tasks = [{'description':'Go to church ', 'status':'pending', 'priority':'M','key':'2025-04-22 17:15:07.331035'},
         {'description':'Go to school', 'status':'pending', 'priority':'M','key':'2025-04-22 17:15:54.325101'},
         {'description':'Go to job', 'status':'complete', 'priority':'M', 'key':'2025-04-22 17:19:27.595020'}
]

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
    task['key'] = datetime.now()

    tasks.append(task)

    print('Your Task was well added to your Todos')
    return tasks

# Step 3: Create the view_tasks() Function

def view_tasks(tasks):
    """
        That function is responsible for showing all user tasks
    """
    if not tasks:
        print("No tasks found.")
        return
    print('Tasks'.center(30,'-'))
    headers = ["#", "Description", "Status", "Priority"]
    table_data = []

    for i, task in enumerate(tasks):
        table_data.append([i + 1, task['description'], task['status'], task['priority']])
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
   
# Step 4: Create the markAsCompleted function

def markTaskCompleted(tasks):

    print('Hi Dear, here you can mark task as completed')

    for task in tasks:
        if task['status'] != 'completed':
            print('Would you like to mark below task as completed. Answer by y(yes) or n(no)')
            print('')
            print(task['description'])
            print('')
            userInput = input('answer here: ')
            userInput = str(userInput).strip().lower()
            if userInput == "y":
                task['status'] = "complete"
                print('Your task is marked as completed')
            elif userInput == "n":
                print('Ok we understant you don\'t want to mark that one as completed')
        
        print("Here are your task with their status")

    view_tasks(tasks)

# Step 5: Making the deleteTask function

def deleteTask(tasks):
    """
    That function will be responsible for deleting a task inside Todos
    """
    print('Hi, that functionality helps to delete tasks')
    print('Answer only by y(yes) or n(No)')
    
    print('')

    array_of_removed = []
    for i, task in enumerate(tasks):

        print(f' Task {i+1}:  {task['description']}')

        goodAnswer = False

        while not goodAnswer:
            userInput = input('Would you like to delete that task: ')
            userInput = str(userInput).lower().strip()

            if userInput == 'y' or userInput == 'n':
                goodAnswer = True

        if userInput == 'y':
            array_of_removed.append(tasks[i]['key'])
           
            print('Your task is going to be deleted')

    if len(array_of_removed) > 0:
        for key in array_of_removed:
            tasks = [task for task in tasks if task.get('key') != key]
            
    print('')
    view_tasks(tasks)


# Step 6: Menu Loop

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
        print("3. Mark task as completed")
        print("4. Delete Task.")
        print("5. Exit")


        try:
            userInput = int(input('Choose an option: '))
        except ValueError:
            print('Please Give number only')
            return
            
        if userInput == 1:
                add_task(tasks)
        elif userInput == 2:
            view_tasks(tasks)
        elif userInput == 3:
            markTaskCompleted(tasks)
        elif userInput == 4:
            deleteTask(tasks)
        elif userInput == 5:
            print('GoodBye dear friend')
            keepGoing = False
        else:
                print('Invalid choice')

"""
NEXT STEPS: 
Test: Testing the code thoroughly to make sure it works as expected.
Ranging Todo things by due date (there is not need now to do that)

"""


#menuLoop()

# Phase 2 : File I/O Module: This would handle saving and loading the tasks to/from a file

# Step 1: Implementing the save_tasks() Function

def save_tasks(tasks, filename="task.json"):
    """
Write tasks dictionary to a file

    """
    try:
        with open(filename, 'w+') as file:
            json.dump(tasks, file)
            print(f'Tasks saved to {filename}')
    except Exception as e:
        print(f'Error saving task: {e}')

save_tasks(tasks)
