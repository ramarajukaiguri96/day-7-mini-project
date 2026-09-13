# Sample Output

Realistic examples of the application running. All output shown below
was produced by the actual running application.

---

## Starting the Application

```
$ python3 main.py

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
Choose option (1-8):
```

---

## Adding a Task (Valid Input)

```
Choose option (1-8): 1

--- Add New Task ---
Title: Finish Python assignment
Priority (high/medium/low): high
Due date (YYYY-MM-DD or leave blank): 2026-09-14
Description (optional): Complete the Day 7 mini-project
✅ Task added (ID: 1)
```

---

## Adding a Task (Invalid Input — Recovery)

```
Choose option (1-8): 1

--- Add New Task ---
Title:
❌ Title cannot be empty. Please enter a title.
Title: Buy groceries
Priority (high/medium/low): urgent
❌ Invalid priority. Please enter one of: high, medium, low.
Priority (high/medium/low): low
Due date (YYYY-MM-DD or leave blank): 13/09/2026
❌ Invalid date format. Please use YYYY-MM-DD (e.g. 2026-09-14), or press Enter to skip.
Due date (YYYY-MM-DD or leave blank):
Description (optional):
✅ Task added (ID: 2)
```

---

## Listing All Tasks

```
Choose option (1-8): 2

--- All Tasks ---
ID    Status      Priority  Due Date      Title
----------------------------------------------------------------------
1     pending     high      2026-09-14    Finish Python assignment
2     pending     low       none          Buy groceries
3     pending     medium    2026-09-10    Call the dentist [OVERDUE]
```

---

## Viewing Task Detail

```
Choose option (1-8): 3

--- View Task Detail ---
Enter task ID to view: 1

  ID          : 1
  Title       : Finish Python assignment
  Description : Complete the Day 7 mini-project
  Priority    : high
  Due Date    : 2026-09-14
  Status      : pending
  Created     : 2026-09-13
```

---

## Marking a Task Complete

```
Choose option (1-8): 4

--- Mark Task Complete ---
Enter task ID to mark complete: 1
✅ Task 1 marked as completed.
```

---

## Marking an Already-Complete Task

```
Choose option (1-8): 4

--- Mark Task Complete ---
Enter task ID to mark complete: 1
ℹ️  Task 1 is already marked as completed.
```

---

## Deleting a Task

```
Choose option (1-8): 5

--- Delete Task ---
Enter task ID to delete: 2
Delete 'Buy groceries'? (yes/no): yes
✅ Task 2 deleted.
```

```
Enter task ID to delete: 2
Delete 'Buy groceries'? (yes/no): no
Deletion cancelled.
```

---

## Filtering Tasks

```
Choose option (1-8): 6

--- Filter Tasks ---
  1. Filter by status   (pending / completed)
  2. Filter by priority (high / medium / low)
Filter by (1/2): 2
Priority (high/medium/low): high

--- Tasks with priority 'high' ---
ID    Status      Priority  Due Date      Title
----------------------------------------------------------------------
1     completed   high      2026-09-14    Finish Python assignment
```

---

## Summary

```
Choose option (1-8): 7

📋 Task Summary
---------------
Total tasks   : 3
Completed     : 1
Pending       : 2
Overdue       : 1
```

---

## Invalid Menu Input

```
Choose option (1-8): 9
❌ '9' is not a valid option. Please enter a number from 1 to 8.

Choose option (1-8): abc
❌ 'abc' is not a valid option. Please enter a number from 1 to 8.
```

---

## Non-Existent Task ID

```
Enter task ID to mark complete: 999
❌ No task found with ID 999.
```

---

## Exiting

```
Choose option (1-8): 8

Goodbye! Your tasks are saved.
```

---

## First Run (No Data File)

```
$ python3 main.py

╔══════════════════════════════╗
║       TASK MANAGER CLI       ║
...
```

(No warning shown — application starts silently with an empty task list
and creates data/tasks.json automatically on the first save.)
