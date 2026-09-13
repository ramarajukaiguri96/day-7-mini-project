# Requirements

## Functional Requirements

These are the features the application must provide to satisfy the assignment.

| ID  | Requirement                                                                 |
|-----|-----------------------------------------------------------------------------|
| F01 | User can add a task with a title, priority, due date, and description       |
| F02 | User can list all tasks in a formatted table                                |
| F03 | User can view the full detail of a single task by ID                        |
| F04 | User can mark a task as complete                                            |
| F05 | User can delete a task by ID                                                |
| F06 | User can filter tasks by status (pending/completed) or priority             |
| F07 | User can view a summary: total, completed, pending, and overdue task counts |
| F08 | All tasks are saved to data/tasks.json immediately after any change         |
| F09 | Application starts fresh (empty list) if data file is missing               |
| F10 | Application warns and starts fresh if data file is corrupted                |

---

## Non-Functional Requirements

| ID   | Category        | Requirement                                                              |
|------|-----------------|--------------------------------------------------------------------------|
| NF01 | Reliability     | Application must not crash on any ordinary user input                    |
| NF02 | Usability       | Menu must be clear; prompts must explain what is expected                 |
| NF03 | Usability       | Error messages must be helpful, not technical tracebacks                 |
| NF04 | Maintainability | Code must follow PEP 8 and use clear naming                              |
| NF05 | Maintainability | Functions must be small and focused on a single responsibility           |
| NF06 | Performance     | No performance requirements beyond "responds instantly" on a local machine|
| NF07 | Persistence     | Data must survive application restarts                                   |
| NF08 | Security        | No secrets, credentials, or personal data stored or hard-coded           |
| NF09 | Portability     | Must run on Python 3.13+ with no third-party packages                    |
| NF10 | Understandability| Every important line of code must be explainable by the student          |

---

## Input Requirements

| Input       | Valid Values                        | Invalid Values                          |
|-------------|-------------------------------------|-----------------------------------------|
| Menu choice | "1" through "8"                     | Any other string, empty, numbers > 8   |
| Title       | Any non-empty string                | Empty string, whitespace only           |
| Priority    | "high", "medium", "low"             | Any other string, empty, numbers        |
| Due date    | "YYYY-MM-DD" format, or blank       | Wrong separators, wrong order, letters  |
| Task ID     | Positive integer matching a task    | Non-integer, negative, non-existent ID |
| Description | Any string including empty          | N/A — description is always optional   |

---

## Output Requirements

- List view: aligned columns with ID, Status, Priority, Due Date, Title
- Detail view: all fields displayed clearly with labels
- Summary: labelled counts with clear formatting
- Success messages: prefix with ✅
- Error messages: prefix with ❌, include what was wrong and how to fix it
- Overdue tasks: marked with [OVERDUE] in the list view

---

## Assignment Requirement Mapping

| Assignment Requirement        | Implementation                          | Test Coverage         |
|-------------------------------|-----------------------------------------|-----------------------|
| Solves a real problem         | Personal task tracking                  | Manual demo           |
| At least 3 non-trivial functions | 6 functions across storage.py and task_manager.py | test_storage.py, test_task_manager.py |
| At least 1 class              | Task class in task.py                   | test_task.py          |
| File I/O (JSON)               | load_tasks() and save_tasks()           | test_storage.py       |
| Error handling (try/except)   | All input paths and file operations     | All test files        |
| Clear user interface          | Numbered menu with prompts              | Manual demo           |
| README.md                     | README.md at project root               | Manual review         |
| 5+ meaningful commits         | 7 commits planned                       | git log               |
| PEP 8                         | Followed throughout                     | Manual review         |
