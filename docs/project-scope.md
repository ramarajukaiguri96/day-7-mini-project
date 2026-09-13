# Project Scope

## In Scope

The following features will be implemented:

- Add a task (title, priority, due date, optional description)
- List all tasks in a formatted table
- View full detail of a single task by ID
- Mark a task as complete by ID
- Delete a task by ID
- Filter tasks by status (pending/completed) or by priority
- Summary view: total, completed, pending, overdue counts
- Persistent storage in data/tasks.json (auto-created)
- Input validation for all user-facing fields
- Graceful error handling — no crashes on bad input
- Unit tests covering the Task class, storage layer, and business logic
- README.md at the project root
- Documentation files in docs/
- run.sh script for easy setup and launch
- At least 7 meaningful Git commits

---

## Out of Scope

The following will NOT be implemented. Any request to add these requires
explicit user approval before any work begins.

- Edit/update an existing task's fields
- Sort tasks by due date or priority in list view
- Web interface of any kind (Flask, FastAPI, Django, HTML, CSS, JavaScript)
- REST API
- React, TypeScript, or Node.js
- PostgreSQL, SQLite, or any database engine
- AWS or any cloud service
- Docker or containerisation
- Authentication or user accounts
- Multi-user support
- Recurring tasks
- Subtasks or task dependencies
- Email or push notifications
- External API calls
- Export to CSV or PDF
- Colour output (colorama library)
- argparse / --help CLI flags
- Any paid service or paid tool
