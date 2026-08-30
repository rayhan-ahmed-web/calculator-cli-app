# Python Developer Internship — Task 2

## To-Do List Application

A console-based To-Do List manager built with Python. This project follows the Task 2 requirements from the internship brief: use a list to store tasks, implement add/remove/view functionality, and persist tasks in a text file using `open()`.

## Features

- Add tasks
- View all tasks with numbered output
- Remove tasks by number
- Persistent storage in `tasks.txt`
- Loads saved tasks when the application starts
- Handles an empty task list
- Handles invalid menu choices and task numbers
- Handles missing `tasks.txt` automatically
- Uses `with open(...)` for safe file handling

## Requirements

- Python 3.x
- VS Code or any terminal

## How to Run

Open a terminal in the repository folder and run:

```bash
python todo.py
```

Or:

```bash
python3 todo.py
```

The first time you add a task, the program creates `tasks.txt` automatically. Tasks remain available the next time the program is started.

## Example

```text
====================================
       TO-DO LIST APPLICATION
====================================

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 1
Enter a task: Complete internship Task 2
Task added successfully.

1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 2

Your Tasks:
1. Complete internship Task 2
```

## Concepts Demonstrated

- Lists and list methods (`append`, `pop`)
- Functions
- Loops and conditionals
- String manipulation with `.strip()`
- File handling with `open()`
- File modes (`r` and `w`)
- Context managers with `with`
- Exception handling with `try/except`
- Persistent CLI applications

## Internship Task Reference

**Task 2: Create a To-Do List Application (Console-based)**

The internship brief specifies Python, VS Code/terminal, a Python file named `todo.py`, lists for storing tasks, add/remove/view functionality, and storing tasks in a text file using `open()`.
