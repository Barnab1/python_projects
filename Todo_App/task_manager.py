#task_manager.py

from tabulate import tabulate
from datetime import datetime
from data_storage import JsonStorage


class TaskManager :
    """
    Responsible for managing the core To-do list functionality
    (CRUD operations)

    This class will use the DataStorage class to handle persistence.

    Will contain most of new feature logic.
    """

    def __init__(self, filePath):
        self.storage = JsonStorage(filePath, "task")  # Use JsonStorage
        self.tasks = self.storage.load()

    def load_tasks(self): # Optional, but good practice to have a separate load method
        self.tasks = self.file.load()
        return self.tasks

    def save_tasks(self): # Add a save_tasks method to update the file
        self.file.save(self.tasks)



    def add_task(self):
        """
        Allow user to add task to their Todo list
        """
        print('Hi Dear We are here in Todo App to help you managing well your time.')
        print('')
        print('Give the following for your task')

        taskDescription = input('Task description: ')
        taskDueDate     = input('Task due date: ')
        taskPriority    = input('Task priority: ')
        taskstatus ='pending'

        task = {}
        
        task['description'] = taskDescription
        task['due date'] = taskDueDate
        task['priority']   = taskPriority
        task['status'] = taskstatus
        task['key'] = str(datetime.now())

        self.tasks.append(task)
        print('Your Task was well added to your Todos')
        self.storage.save(self.tasks)  # Use storage.save()

    def view_tasks(self):
        """
        Allow user to see their stored tasks
        """
        if not self.tasks: # Use the instance's tasks list
            print("No tasks found.")
            return
        else:
            print('Tasks'.center(30,'-'))
            headers = ["#", "Description","Due Date", "Status", "Priority"]
            table_data = []

            for i, task in enumerate(self.tasks):
                table_data.append([i + 1, task['description'], task['due date'],task['status'], task['priority']])
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def markTaskCompleted(self):
        """
        Allow user to mark their task as completed
        """
        print('Hi Dear, here you can mark task as completed')
        
        tasks_to_mark = [task for task in self.tasks if task['status'] != 'completed']

        if not tasks_to_mark:
            print("No pending tasks to mark as completed.")
            return

        for i, task in enumerate(tasks_to_mark):
            print(f"{i + 1}. {task['description']}")
            userInput = input('Would you like to mark this task as completed? (y/n): ').strip().lower()
            if userInput == "y":
                task['status'] = "complete"
                print(f"Task '{task['description']}' marked as completed.")

        self.storage.save(self.tasks)

        print("\nHere are your tasks with their updated status:")
        self.view_tasks()

    
    def deleteTask(self):
            """
            Allows the user to delete a task from the To-Do list by its number.
            """
            if not self.tasks:
                print("No tasks to delete.")
                return

            print('Hi, that functionality helps to delete tasks')
            print('Here are your current tasks:')
            print('')
            for i, task in enumerate(self.tasks):
                print(f'{i + 1}. {task["description"]}')
            print('')

            while True:
                try:
                    task_number_to_delete = int(input("Enter the number of the task you want to delete (or 0 to cancel): "))
                    if task_number_to_delete == 0:
                        print("Deletion cancelled.")
                        return
                    elif 1 <= task_number_to_delete <= len(self.tasks):
                        index_to_delete = task_number_to_delete - 1
                        deleted_task = self.tasks.pop(index_to_delete)
                        self.storage.save(self.tasks)
                        print(f"Task '{deleted_task['description']}' has been deleted.")
                        self.view_tasks()  # Show the updated list
                        break  # Exit the loop after successful deletion
                    else:
                        print("Invalid task number. Please enter a number from the list or 0 to cancel.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

