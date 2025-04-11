#Simple To-Do List Application:

#Goal: Create a command-line or basic GUI (using Tkinter) application to manage tasks.
#Skills: Variables, lists, loops, conditional statements, basic file I/O (to save/load tasks).
#Progression: Add features like task prioritization, due dates, and task completion tracking.

"""
Functionality and user interaction

    - actions performed by user: add, view, complete as done

    - way user interact with application: Commmand line input

    - type of input : text prompts

    - type of output:  formatted list

    - Tasks should be ordered by description priority ?

        -Priority hare are ('Must do':m,'should do':s,'could do':c, 'Will not do': w)

    - How will the user identify which task to mark as complete or delete? (By number ?, description ?)

    - What feedback should the user receive after each action? (Confirmation messages when everythin is fine, error message
        when there is a mistake)

Data structures and Storage

    - How will the tasks be stored in memory while the application is running? (List of dictionaries)
    - information to store for each task: (Description, status, due date, priority)
    - If using a list of dictionaries, what keys will the dictionaries have? (e.g., 'description', 'status', 'due_date', 'priority').
    - How will the application handle an empty task list ('tell user that we want to delete it and proceed if they confirm/ask user to update')
    - I don't need to store the date or time the task was added, just the due_date
3. Error Handling and Edge Cases:

    - What happens if the user enters invalid input? : Throw a TypeError.
    - What happens if the user tries to mark a task as complete that doesn't exist: Throw a message saying that the task doesn't exist
    - What happens if the user tries to delete a task that doesn't exist "Throw a message saying the task doesn't exist)
    - What happens if the user inputs nothing for the task description: The task should keep coming again and again

4. Code Organization and Modularity:

    - How will the code be organized into functions : (One function per action).


    - What are the main modules or components of the application?
    - How will data be passed between functions: passing as arguments:
        Eg: def add_task(tasks, new_task): # tasks list passed as an argument
            def view_tasks(tasks): # tasks list passed as an argument

    - How can the code be made reusable and maintainable (use of small chunk of function with meaningfull name)
"""