# Daily Task Manager

**PS No. 27** | Rungta International Skills University
School of Computer Science and Engineering | B.Tech CSE, First Semester

**Author:** Rishi Shrivas

---

## About

Daily Task Manager is a console-based Python application that helps you keep track of your daily tasks. Each task has a title, a priority and a due date. Tasks are saved in a text file, so they are still there the next time you run the program.

## Features

- Add a task with a title, priority (High / Medium / Low) and due date
- View all tasks sorted by priority
- Show only pending tasks
- Mark a task as complete using its task ID
- Input validation for priority and date format
- Automatic loading from and saving to `tasks.txt`

## Concepts Used

- Lists and dictionaries
- Functions
- File handling
- Input validation and error handling

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```bash
python task_manager.py
```

## Menu

```
1. Add task
2. View by priority
3. Show pending
4. Complete task
```

## Data Format

- Each task is stored as a dictionary inside a list, with a unique ID.
- Task IDs start from `T101` (T101, T102, T103, ...).
- Priority must be `High`, `Medium` or `Low`.
- Dates must use the format `YYYY-MM-DD` (example: `2026-10-15`).
- The file is read when the program starts and saved after every change.

## Sample Run

```
Option: 1 (Add)
Title: Submit report
Priority: High
Due: 2026-10-15

Task added.
T101 | Submit report | High | 2026-10-15 | Pending
```

## Error Handling

| Situation | Message |
|---|---|
| Priority not High/Medium/Low | Invalid priority. Enter High, Medium or Low. |
| Date not in YYYY-MM-DD | Invalid date. Use YYYY-MM-DD. |
| Task ID does not exist | Task T999 not found. |
| No pending tasks | No pending tasks. You are all caught up! |

## Test Cases

Full test cases are in [`test_cases.txt`](test_cases.txt). They cover:

1. Normal input (adding a task)
2. Boundary case (no tasks in the file)
3. Invalid input (bad priority, bad date, unknown task ID)
4. A different valid scenario (view by priority, complete a task)

## Project Files

```
.
├── task_manager.py     # Main program
├── tasks.txt           # Saved tasks
├── test_cases.txt      # Test cases
├── SUMMARY.md          # Project summary
└── README.md
```

## Author

Rishi Shrivas
B.Tech Computer Science and Engineering, First Semester
Rungta International Skills University
