# Design

## Overview

The Task Manager CLI is a four-module Python application. Each module has a
single, clear responsibility. This separation makes the code easy to understand,
test, and modify.

---

## Module Responsibilities

| Module          | Responsibility                                                   |
|-----------------|------------------------------------------------------------------|
| main.py         | Entry point. Starts the app, loads data, runs the menu loop.     |
| task.py         | Defines the Task class — the core data object of the application.|
| storage.py      | Handles reading from and writing to data/tasks.json.             |
| task_manager.py | Contains the business logic: creating, filtering, formatting tasks.|

---

## CLI Flow

```
python3 main.py
       │
       ▼
Load tasks from data/tasks.json
  ├── File exists      → load tasks into a Python list
  ├── File missing     → start with empty list (file created on first save)
  └── File corrupted   → warn user, start with empty list

       │
       ▼
Display main menu (loop until user chooses Exit)
  │
  ├── 1. Add task         → prompt for title, priority, due date, description
  │                          validate each field → create Task → save
  ├── 2. List all tasks   → format all tasks as a table → print
  ├── 3. View task detail → prompt for ID → find task → print all fields
  ├── 4. Mark complete    → prompt for ID → find task → mark done → save
  ├── 5. Delete task      → prompt for ID → find task → remove → save
  ├── 6. Filter tasks     → prompt for filter type → filter → print table
  ├── 7. Summary          → count total/completed/pending/overdue → print
  └── 8. Exit             → print goodbye → break loop
```

---

## Classes

### Task (task.py)

Represents a single task. Chosen as a class because a task has multiple related
fields and methods that naturally belong together.

**Attributes:**
- task_id (int): unique identifier, auto-assigned
- title (str): what the task is, required
- description (str): optional detail
- priority (str): "high", "medium", or "low"
- due_date (str): "YYYY-MM-DD" or empty string
- status (str): "pending" or "completed"
- created_at (str): date the task was created, auto-set

**Methods:**
- to_dict(): converts Task to a plain dictionary for JSON storage
- from_dict(data): classmethod — creates a Task object from a dictionary
- is_overdue(): returns True if due date is in the past and task is not done
- mark_complete(): changes status from "pending" to "completed"
- __str__(): returns a short one-line string summary of the task

---

## Functions

### storage.py

**load_tasks(filepath)**
Reads data/tasks.json and returns a list of Task objects.
Handles: file not found, empty file, invalid JSON.

**save_tasks(tasks, filepath)**
Converts all Task objects to dicts and writes to data/tasks.json.
Handles: directory creation, OS/permission errors.

### task_manager.py

**get_next_id(tasks)**
Returns the next available integer ID.
Ensures no ID collisions even after deletions.

**filter_tasks(tasks, status, priority)**
Returns a filtered subset of tasks matching optional criteria.

**format_task_table(tasks)**
Builds a formatted string table with aligned columns for display.

**validate_date(date_str)**
Checks that a string is a valid YYYY-MM-DD date or empty.
Returns True/False.

---

## Data Flow

```
User input
    │
    ▼
Input validation (task_manager.py / main.py)
    │
    ▼
Task object created or modified (task.py)
    │
    ▼
In-memory list of Task objects updated
    │
    ▼
save_tasks() called (storage.py)
    │
    ▼
data/tasks.json updated on disk
```

---

## Storage Approach

- Single JSON file: data/tasks.json
- Loaded once at startup into a Python list
- Saved immediately after every add / complete / delete
- No caching, no buffering — always up to date on disk

---

## Error Handling Approach

- All user input is validated before use
- File errors are caught with specific except clauses
- Every error shows a helpful message — no raw tracebacks
- Application always returns to the menu after an error
- No bare `except:` blocks
