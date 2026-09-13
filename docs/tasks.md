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

- [ ] Implement Task class in task.py
- [ ] Add all attributes: task_id, title, description, priority, due_date, status, created_at
- [ ] Implement to_dict()
- [ ] Implement from_dict() classmethod
- [ ] Implement is_overdue()
- [ ] Implement mark_complete()
- [ ] Implement __str__()
- [ ] Add docstrings and comments

---

### Commit 3 — JSON storage layer

- [ ] Implement load_tasks() in storage.py
- [ ] Implement save_tasks() in storage.py
- [ ] Handle FileNotFoundError in load_tasks
- [ ] Handle json.JSONDecodeError in load_tasks
- [ ] Handle OSError/PermissionError in save_tasks
- [ ] Auto-create data/ directory in save_tasks
- [ ] Add docstrings and comments

---

### Commit 4 — Business logic

- [ ] Implement get_next_id() in task_manager.py
- [ ] Implement filter_tasks() in task_manager.py
- [ ] Implement format_task_table() in task_manager.py
- [ ] Implement validate_date() in task_manager.py
- [ ] Implement get_summary() in task_manager.py
- [ ] Implement find_task_by_id() in task_manager.py
- [ ] Add docstrings and comments

---

### Commit 5 — CLI menu and user interaction

- [ ] Implement main menu loop in main.py
- [ ] Implement add_task() prompt flow
- [ ] Implement list_tasks() display
- [ ] Implement view_task_detail() prompt flow
- [ ] Implement mark_task_complete() prompt flow
- [ ] Implement delete_task() prompt flow
- [ ] Implement filter_tasks_menu() prompt flow
- [ ] Implement show_summary() display
- [ ] Add docstrings and comments
- [ ] Verify application runs end-to-end

---

### Commit 6 — Unit tests

- [ ] Write tests/test_task.py (Task class tests)
- [ ] Write tests/test_storage.py (load/save tests)
- [ ] Write tests/test_task_manager.py (logic function tests)
- [ ] Run all tests: python3 -m unittest discover tests -v
- [ ] All tests pass

---

### Commit 7 — Documentation and run.sh

- [ ] Create run.sh
- [ ] Complete docs/test-cases.md (100–150 cases)
- [ ] Complete docs/sample-output.md
- [ ] Complete docs/setup-and-run.md
- [ ] Update docs/error-logs.md with any real errors found
- [ ] Update docs/change-log.md with all commits
- [ ] Update docs/known-issues.md (genuine issues only)
- [ ] Final review of README.md
- [ ] Run full test suite one final time
- [ ] Verify run.sh works end-to-end

---

## Status

Currently on: Commit 1 — Project skeleton
