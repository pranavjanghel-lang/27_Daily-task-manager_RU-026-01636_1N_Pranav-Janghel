# Project Summary: Daily Task Manager (PS 27)

## Problem Statement

Build a console task manager in Python where each task has a title, a priority and a due date. The user can add tasks, view them by priority, list pending tasks and mark tasks as done. Tasks are saved to a file so they persist between runs.

## Objective

To apply Python fundamentals (lists, dictionaries, functions and file handling) to build a small, working application with proper input validation.

## Approach

1. Understood the problem and listed the required menu options.
2. Stored each task as a dictionary (ID, title, priority, due date, status) inside a list.
3. Wrote one function for each action: add, view by priority, show pending and complete.
4. Validated priority (High, Medium, Low) and date format (YYYY-MM-DD) before saving a task.
5. Loaded tasks from `tasks.txt` at start and saved them after every change.
6. Tested the program with the given test cases and fixed any errors.

## Key Features

- Unique task IDs starting from T101
- Sorting by priority (High, then Medium, then Low)
- Pending task filter
- Clear error messages for invalid input
- Persistent storage in a text file

## Testing

Four test cases were prepared (see `test_cases.txt`):

| No. | Type | Purpose |
|---|---|---|
| 1 | Normal input | Add a task and confirm the output |
| 2 | Boundary | Show pending tasks when the file is empty |
| 3 | Invalid input | Wrong priority, wrong date format, unknown task ID |
| 4 | Different valid scenario | View by priority, then complete a task |

## Outcome

The program meets all the bare minimum requirements: it runs from the console, stores tasks as dictionaries in a list with unique IDs, has one function per action, validates input, and keeps data in a file between runs.

## Learning

- Using dictionaries and lists together to model real data
- Reading and writing files safely
- Handling invalid user input without crashing
- Writing test cases before and after coding

---

**Author:** Rishi Shrivas
Rungta International Skills University, B.Tech CSE (First Semester)
