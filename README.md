# Task Manager CLI

A command-line task manager built in Python. Add tasks with priorities and due
dates, track their status, filter by category, and view a summary — all saved
locally to a JSON file.

---

## Problem It Solves

Keeping track of daily tasks using memory or scattered notes is unreliable.
This tool gives you a simple, fast, terminal-based way to record, organise, and
track personal tasks without needing an internet connection, an account, or any
paid service.

---

## Features

- Add a task with title, priority (high/medium/low), due date, and description
- List all tasks in a formatted table
- View full detail of a single task
- Mark a task as complete
- Delete a task
- Filter tasks by status (pending/completed) or priority
- Summary view: total, completed, pending, and overdue counts
- All data saved automatically to a local JSON file
- Graceful error handling — never crashes on bad input

---

## Requirements

- Python 3.13 or later
- No third-party packages — uses Python standard library only

---

## Installation

```bash
git clone https://github.com/<your-username>/day-7-mini-project.git
cd day-7-mini-project
```

No `pip install` step required — there are no external dependencies.

---

## Setup

### Option A — Using the run script (recommended)

```bash
bash run.sh
```

The script checks your Python version, creates the `data/` directory if needed,
and launches the application.

### Option B — Direct

```bash
python3 main.py
```

---

## Usage

Run the application and follow the numbered menu:

```
╔══════════════════════════════╗
║       TASK MANAGER CLI       ║
╠══════════════════════════════╣
║  1. Add task                 ║
║  2. List all tasks           ║
║  3. View task detail         ║
║  4. Mark task complete       ║
║  5. Delete task              ║
║  6. Filter tasks             ║
║  7. Summary                  ║
║  8. Exit                     ║
╚══════════════════════════════╝
```

---

## Examples

**Adding a task:**
```
Choose option (1-8): 1
Title: Finish Python assignment
Priority (high/medium/low): high
Due date (YYYY-MM-DD or leave blank):  2026-09-14
Description (optional): Complete Day 7 mini-project
✅ Task added (ID: 1)
```

**Listing tasks:**
```
ID   Status     Priority   Due Date     Title
---- ---------- ---------- ------------ ---------------------
1    pending    high       2026-09-14   Finish Python assignment
```

**Summary:**
```
📋 Task Summary
---------------
Total tasks   : 3
Completed     : 1
Pending       : 2
Overdue       : 1
```

---

## Testing

Run all unit tests:

```bash
python3 -m unittest discover tests -v
```

---

## Project Structure

```
day-7-mini-project/
├── main.py            # Entry point — CLI menu loop
├── task.py            # Task class
├── storage.py         # JSON load/save functions
├── task_manager.py    # Business logic functions
├── tests/
│   ├── test_task.py
│   ├── test_storage.py
│   └── test_task_manager.py
├── data/
│   └── tasks.json     # Auto-created at runtime (gitignored)
├── docs/              # Full project documentation
├── project-docs/      # Original assignment files (untouched)
├── README.md
├── .gitignore
└── run.sh
```

---

## Data Storage

Tasks are stored in `data/tasks.json` as a JSON array. The file is created
automatically on first run. Each task looks like this:

```json
{
  "task_id": 1,
  "title": "Finish Python assignment",
  "description": "Complete Day 7 mini-project",
  "priority": "high",
  "due_date": "2026-09-14",
  "status": "pending",
  "created_at": "2026-09-13"
}
```

---

## Error Handling

- Missing data file → starts fresh with an empty task list
- Corrupted JSON → warns the user and starts fresh
- Invalid menu input → shows a helpful message and re-displays the menu
- Invalid date format → shows the expected format and asks again
- Invalid priority → shows valid options and asks again
- Non-existent task ID → shows "Task not found" without crashing
- File write failure → shows an error message without crashing

---

## Troubleshooting

**"python3: command not found"**
Install Python 3.13: `sudo apt install python3.13`

**"Permission denied" on data/tasks.json**
Check file permissions: `ls -l data/` and run `chmod 644 data/tasks.json`

**Tasks not saving**
Ensure the `data/` directory exists: `mkdir -p data`

---

## What I Learned

- How to design and use a Python class to represent a real-world entity
- How to read and write JSON files for data persistence
- How to handle errors gracefully so programs never crash on bad input
- How to structure a multi-file Python project
- How to write unit tests with Python's built-in `unittest` module
- How to use Git with meaningful, logical commits

---

## Future Improvements

- [ ] Edit an existing task's title, priority, or due date
- [ ] Sort tasks by due date or priority in list view
- [ ] Add colour output using the `colorama` library
- [ ] Add `--help` flag using `argparse`
- [ ] Export tasks to CSV

---

## Limitations

- Single user only — no multi-user support
- No recurring tasks
- No subtasks or task dependencies
- No notifications or reminders
- Data stored locally only — no sync or backup

---

## Git Commit History

```
1. Initialize project structure and documentation
2. Add Task class with validation and serialization
3. Add JSON storage layer
4. Add business logic functions
5. Add CLI menu and user interaction
6. Add unit tests
7. Complete documentation and run.sh
```

---

## License

This project was created as part of the Infinitra Build bootcamp (Week 1, Day 7).
Free to use for educational purposes.
