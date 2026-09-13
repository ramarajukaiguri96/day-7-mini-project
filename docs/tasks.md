# Implementation Tasks

## Checklist

Work through these tasks in order. Each task maps to a Git commit.

---

### Commit 1 — Project skeleton

- [x] Initialise Git repository, rename branch to main
- [x] Create directory structure: tests/, data/, docs/
- [x] Create .gitignore
- [x] Create data/.gitkeep
- [x] Create tests/__init__.py
- [x] Create README.md at project root
- [x] Create docs/requirements.md
- [x] Create docs/design.md
- [x] Create docs/architecture.md
- [x] Create docs/data-model.md
- [x] Create docs/project-scope.md
- [x] Create docs/tasks.md (this file)
- [x] Create docs/testing.md
- [x] Create docs/security.md
- [x] Create docs/error-logs.md
- [x] Create docs/change-log.md
- [x] Create docs/known-issues.md

---

### Commit 2 — Task class

- [x] Implement Task class in task.py
- [x] Add all attributes: task_id, title, description, priority, due_date, status, created_at
- [x] Implement to_dict()
- [x] Implement from_dict() classmethod
- [x] Implement is_overdue()
- [x] Implement mark_complete()
- [x] Implement __str__()
- [x] Add docstrings and comments

---

### Commit 3 — JSON storage layer

- [x] Implement load_tasks() in storage.py
- [x] Implement save_tasks() in storage.py
- [x] Handle FileNotFoundError in load_tasks
- [x] Handle json.JSONDecodeError in load_tasks
- [x] Handle OSError/PermissionError in save_tasks
- [x] Auto-create data/ directory in save_tasks
- [x] Add docstrings and comments

---

### Commit 4 — Business logic

- [x] Implement get_next_id() in task_manager.py
- [x] Implement filter_tasks() in task_manager.py
- [x] Implement format_task_table() in task_manager.py
- [x] Implement validate_date() in task_manager.py
- [x] Implement get_summary() in task_manager.py
- [x] Implement find_task_by_id() in task_manager.py
- [x] Add docstrings and comments

---

### Commit 5 — CLI menu and user interaction

- [x] Implement main menu loop in main.py
- [x] Implement add_task() prompt flow
- [x] Implement list_tasks() display
- [x] Implement view_task_detail() prompt flow
- [x] Implement mark_task_complete() prompt flow
- [x] Implement delete_task() prompt flow
- [x] Implement filter_tasks_menu() prompt flow
- [x] Implement show_summary() display
- [x] Add docstrings and comments
- [x] Verify application runs end-to-end

---

### Commit 6 — Unit tests

- [x] Write tests/test_task.py (Task class tests)
- [x] Write tests/test_storage.py (load/save tests)
- [x] Write tests/test_task_manager.py (logic function tests)
- [x] Run all tests: python3 -m unittest discover tests -v
- [x] All tests pass (92/92)

---

### Commit 7 — Documentation and run.sh

- [x] Create run.sh
- [x] Complete docs/test-cases.md (92 automated + 14 manual cases)
- [x] Complete docs/sample-output.md
- [x] Complete docs/setup-and-run.md
- [x] Update docs/error-logs.md with real status
- [x] Update docs/change-log.md with all commits
- [x] Update docs/known-issues.md (no issues found)
- [x] Final review of README.md
- [x] Run full test suite one final time
- [x] Verify run.sh works end-to-end

---

## Status

All tasks complete. Project ready for submission.
