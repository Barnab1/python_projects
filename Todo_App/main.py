#main.py 
# Main part of the App
from task_manager import TaskManager

def main():
    keepGoing = True
    appFunctions = TaskManager("tasks.json") # Tasks are loaded on initialization

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
            continue # Go back to the menu

        if userInput == 1:
            appFunctions.add_task()
        elif userInput == 2:
            appFunctions.view_tasks()
        elif userInput == 3:
            appFunctions.markTaskCompleted()
        elif userInput == 4:
            appFunctions.deleteTask()
        elif userInput == 5:
            print('GoodBye dear friend')
            keepGoing = False
        else:
            print('Invalid choice')
main()
