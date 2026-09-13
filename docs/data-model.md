# Data Model

## Storage Format

Tasks are stored in a single JSON file: `data/tasks.json`

The file contains one top-level key `"tasks"` whose value is a list of task
objects. This structure makes it easy to add other top-level keys in future
(e.g. settings) without breaking existing data.

---

## JSON Structure

```json
{
  "tasks": [
    {
      "task_id": 1,
      "title": "Finish Python assignment",
      "description": "Complete the Day 7 mini-project",
      "priority": "high",
      "due_date": "2026-09-14",
      "status": "pending",
      "created_at": "2026-09-13"
    },
    {
      "task_id": 2,
      "title": "Buy groceries",
      "description": "",
      "priority": "low",
      "due_date": "",
      "status": "completed",
      "created_at": "2026-09-12"
    }
  ]
}
```

---

## Field Reference

| Field        | Type   | Required | Allowed Values                    | Notes                          |
|--------------|--------|----------|-----------------------------------|--------------------------------|
| task_id      | int    | Yes      | Positive integers (1, 2, 3, ...)  | Auto-assigned, never reused    |
| title        | str    | Yes      | Any non-empty string              | Cannot be blank                |
| description  | str    | No       | Any string including ""           | Empty string if not provided   |
| priority     | str    | Yes      | "high", "medium", "low"           | Always lowercase               |
| due_date     | str    | No       | "YYYY-MM-DD" or ""                | Empty string means no due date |
| status       | str    | Yes      | "pending", "completed"            | Starts as "pending"            |
| created_at   | str    | Yes      | "YYYY-MM-DD"                      | Auto-set to today's date       |

---

## Validation Rules

- `task_id`: auto-generated as max(existing IDs) + 1, or 1 if list is empty
- `title`: stripped of leading/trailing whitespace; rejected if empty after strip
- `priority`: converted to lowercase; rejected if not "high", "medium", or "low"
- `due_date`: validated with datetime.strptime(date_str, "%Y-%m-%d"); accepted
  if blank (means no due date); rejected if format is wrong
- `status`: set to "pending" on creation; only changed to "completed" via
  the mark-complete action; never set to any other value
- `created_at`: set automatically to today's date (date.today().isoformat())

---

## File Behaviour

- If `data/tasks.json` does not exist: application starts with an empty list
  and creates the file automatically on the first save
- If `data/tasks.json` exists but is empty or contains invalid JSON: application
  warns the user and starts with an empty list
- If `data/` directory does not exist: `os.makedirs("data", exist_ok=True)`
  creates it before saving
- The file is written with `indent=2` for human readability
