#coreFunctions.py
from tabulate import tabulate
from datetime import datetime
from input_output_module import InputOutputModule


class CoreFunctions:
    def __init__(self, filePath):
        self.filePath = filePath
        
        self.file = InputOutputModule(self.filePath,'Task')

    def add_task(self):
        """
        Responsible for adding task to tasks list
        """
        print('Hi Dear We are here in Todo App to help you managing well your time.')
        print('')
        print('Give the following descriptions for your task')

        tasks = file.load(self.filePath)

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

        file.save(tasks,filePath)

# Step 3: Create the view_tasks() Function

    def view_tasks(self):
        """
            That function is responsible for showing all user tasks
        """

        tasks = InputOutputModule.load(self.filePath)

        if not tasks:
            print("No tasks found.")
            return
        else:
            print('Tasks'.center(30,'-'))
            headers = ["#", "Description", "Status", "Priority"]
            table_data = []

            for i, task in enumerate(tasks):
                table_data.append([i + 1, task['description'], task['status'], task['priority']])
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
# Step 4: Create the markAsCompleted function

    def markTaskCompleted(self):

        print('Hi Dear, here you can mark task as completed')

        tasks = InputOutputModule.load(self.filePath)
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
                    InputOutputModule.save(tasks,self.filePath)
                    print('Your task is marked as completed')


                print("Here are your task with their status")
                self.view_tasks(tasks)
            else:
                print('Your task is already marked as completed')

        

    # Step 5: Making the deleteTask function

    def deleteTask(self):
        """
        That function will be responsible for deleting a task inside Todos
        """
        print('Hi, that functionality helps to delete tasks')
        print('Answer only by y(yes) or n(No)')
        
        print('')

        tasks = InputOutputModule.load(self.filePath)
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

        InputOutputModule.save(tasks, self.filePath)        
        print('')
        self.view_tasks(tasks)
