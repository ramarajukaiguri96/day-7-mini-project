# Change Log

Records meaningful changes made to the project, one entry per Git commit.

---

## [Commit 1] — 2026-09-13
**Initialize project structure and documentation**

- Initialised Git repository with `main` branch
- Created directory structure: tests/, data/, docs/
- Created .gitignore (excludes venv, __pycache__, data/tasks.json)
- Created data/.gitkeep to track empty data directory
- Created tests/__init__.py
- Created README.md at project root
- Created all documentation stub files in docs/

---

## [Commit 2] — 2026-09-13
**Add Task class with validation and serialization**

- Implemented Task class in task.py
- Added all 7 attributes with correct defaults
- Implemented to_dict(), from_dict(), is_overdue(), mark_complete(), __str__()
- Full docstrings and comments on all methods

---

## [Commit 3] — 2026-09-13
**Add JSON storage layer**

- Implemented load_tasks() in storage.py
- Implemented save_tasks() in storage.py
- Handles FileNotFoundError, json.JSONDecodeError, OSError, PermissionError
- Auto-creates data/ directory if missing

---

## [Commit 4] — 2026-09-13
**Add business logic functions**

- Implemented get_next_id(), find_task_by_id(), filter_tasks()
- Implemented validate_date(), get_summary(), format_task_table()
- Full docstrings and comments on all functions

---

## [Commit 5] — 2026-09-13
**Add CLI menu and user interaction**

- Implemented full main menu loop in main.py
- Implemented add_task(), list_tasks(), view_task_detail()
- Implemented mark_task_complete(), delete_task(), filter_tasks_menu(), show_summary()
- All input paths validated; confirmation required for delete

---

## [Commit 6] — 2026-09-13
**Add unit tests**

- Created tests/test_task.py — 49 test cases for Task class
- Created tests/test_storage.py — 19 test cases for storage layer
- Created tests/test_task_manager.py — 24 test cases for business logic
- 92 total tests, all passing

---

## [Commit 7] — 2026-09-13
**Complete documentation and run.sh**

- Created run.sh with Python version check and --test flag
- Completed docs/test-cases.md (92 automated + 14 manual cases)
- Completed docs/sample-output.md with realistic CLI examples
- Completed docs/setup-and-run.md with Ubuntu and VS Code instructions
- Updated docs/error-logs.md, docs/change-log.md, docs/known-issues.md, docs/tasks.md
