# Testing Strategy

## Framework

Python's built-in `unittest` module. No third-party testing packages required.

Run all tests:
```bash
python3 -m unittest discover tests -v
```

---

## Test Files

| File                       | What it tests                              |
|----------------------------|--------------------------------------------|
| tests/test_task.py         | Task class — creation, methods, validation |
| tests/test_storage.py      | load_tasks() and save_tasks()              |
| tests/test_task_manager.py | All business logic functions               |

---

## Test Categories

### 1. Task class tests (test_task.py)
- Creating a Task with valid inputs
- Task attribute values are set correctly
- to_dict() produces the correct dictionary
- from_dict() recreates the correct Task object
- Round-trip: to_dict() → from_dict() produces identical task
- is_overdue() returns True for past due date + pending status
- is_overdue() returns False for future due date
- is_overdue() returns False for past due date + completed status
- is_overdue() returns False for empty due date
- mark_complete() changes status to "completed"
- mark_complete() on already-complete task does not error
- __str__() returns a non-empty string

### 2. Storage tests (test_storage.py)
- load_tasks() returns empty list when file does not exist
- load_tasks() returns empty list for empty file
- load_tasks() returns empty list for corrupted JSON
- load_tasks() correctly loads a valid tasks.json
- save_tasks() writes correct JSON to file
- save_tasks() creates data/ directory if missing
- save_tasks() with empty list writes valid empty structure
- Round-trip: save then load returns identical tasks

### 3. Business logic tests (test_task_manager.py)
- get_next_id() returns 1 for empty list
- get_next_id() returns max_id + 1
- get_next_id() works correctly after deletion gaps
- filter_tasks() by status=pending
- filter_tasks() by status=completed
- filter_tasks() by priority=high
- filter_tasks() by priority=medium
- filter_tasks() by priority=low
- filter_tasks() with no matches returns empty list
- filter_tasks() with no filter returns all tasks
- validate_date() accepts valid YYYY-MM-DD dates
- validate_date() accepts empty string
- validate_date() rejects wrong format
- validate_date() rejects non-date strings
- format_task_table() with empty list shows "No tasks"
- format_task_table() with tasks returns formatted string
- format_task_table() marks overdue tasks
- get_summary() counts correctly
- find_task_by_id() returns correct task
- find_task_by_id() returns None for missing ID

---

## Test Isolation

- File I/O tests use tempfile.NamedTemporaryFile so no real data is touched
- Each test is independent — no test depends on another test's side effects
- setUp() and tearDown() used where shared state is needed

---

## Test Result Format

At the end of implementation, results will be recorded as:

```
Total tests  : X
Passed       : X
Failed       : 0
Skipped      : 0
Errors       : 0
```

If any tests fail, they will be fixed before the project is considered complete.
