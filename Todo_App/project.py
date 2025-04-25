# A simple app to help people organizing their future task by priority and deadlines
"""       
- (Later, in Phase 3) GUI Module: If we add a GUI, this would handle the GUI elements and their interactions

"""
from coreFunctions import CoreFunctions

#STEP 1: Initializing the Task List

"""tasks = [{'description':'Go to church ', 'status':'pending', 'priority':'M','key':'2025-04-22 17:15:07.331035'},
         {'description':'Go to school', 'status':'pending', 'priority':'M','key':'2025-04-22 17:15:54.325101'},
         {'description':'Go to job', 'status':'complete', 'priority':'M', 'key':'2025-04-22 17:19:27.595020'}
#"""


def menuLoop():
    """
    Showing the main menu
    """
    keepGoing = True
    appFunctions = CoreFunctions("tasks.json")
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

"""
NEXT STEPS: 
Test: Testing the code thoroughly to make sure it works as expected.
Ranging Todo things by due date (there is not need now to do that)

"""


menuLoop()

