# Test Cases

Total test cases: 92 (automated) + manual verification cases below.

All 92 automated cases are implemented in tests/ and verified passing.
Manual cases cover end-to-end CLI flows that cannot be meaningfully
automated without simulating interactive input.

---

## Automated Test Cases

### Category 1 — Task Creation (tests/test_task.py :: TestTaskCreation)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC001 | All fields stored correctly | Task(1,"T","D","high","2026-09-14","pending","2026-09-13") | Each attribute matches |
| TC002 | Minimal task uses defaults | Task(2,"Minimal") | priority="medium", status="pending", description="" |
| TC003 | created_at auto-set when empty | Task(3,"T",created_at="") | created_at == today's date |
| TC004 | created_at preserved when given | Task(4,"T",created_at="2025-01-01") | created_at == "2025-01-01" |
| TC005 | Title stored as-is | Task(5,"  Spaced  ") | title == "  Spaced  " |
| TC006 | priority="high" stored | Task(6,"T",priority="high") | priority == "high" |
| TC007 | priority="medium" is default | Task(7,"T") | priority == "medium" |
| TC008 | priority="low" stored | Task(8,"T",priority="low") | priority == "low" |
| TC009 | Empty due_date stored | Task(9,"T",due_date="") | due_date == "" |
| TC010 | Default status is pending | Task(10,"T") | status == "pending" |

### Category 2 — Serialisation (tests/test_task.py :: TestTaskSerialization)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC011 | to_dict returns a dict | task.to_dict() | type is dict |
| TC012 | to_dict contains all keys | task.to_dict() | all 7 keys present |
| TC013 | to_dict values match attributes | task.to_dict() | each value correct |
| TC014 | from_dict creates Task | dict with all fields | Task instance |
| TC015 | Round-trip to/from dict | to_dict() → from_dict() | identical Task |
| TC016 | from_dict missing optional keys | {"task_id":3,"title":"X"} | defaults applied |

### Category 3 — is_overdue() (tests/test_task.py :: TestTaskIsOverdue)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC017 | Past date + pending = overdue | due=yesterday, status=pending | True |
| TC018 | Future date + pending = not overdue | due=tomorrow, status=pending | False |
| TC019 | Past date + completed = not overdue | due=yesterday, status=completed | False |
| TC020 | No due date = not overdue | due="" | False |
| TC021 | Future date + completed = not overdue | due=tomorrow, status=completed | False |
| TC022 | Due today = not overdue | due=today | False |
| TC023 | Invalid date string = not overdue | due="not-a-date" | False |

### Category 4 — mark_complete() (tests/test_task.py :: TestTaskMarkComplete)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC024 | Status changes to completed | pending task → mark_complete() | status == "completed" |
| TC025 | Already-complete task no error | completed task → mark_complete() | no exception |
| TC026 | Overdue clears after complete | past due + pending → mark_complete() | is_overdue() == False |

### Category 5 — __str__() (tests/test_task.py :: TestTaskStr)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC027 | Title in output | Task(1,"Important task") | "Important task" in str |
| TC028 | ID in output | Task(42,"X") | "42" in str |
| TC029 | [OVERDUE] in output for overdue | past due + pending | "[OVERDUE]" in str |
| TC030 | No [OVERDUE] for future task | future due | "[OVERDUE]" not in str |
| TC031 | Returns string type | any Task | isinstance(str(t), str) |

### Category 6 — load_tasks() (tests/test_storage.py :: TestLoadTasks)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC032 | Missing file returns [] | non-existent path | [] |
| TC033 | Corrupted JSON returns [] | "not valid json" | [] |
| TC034 | Empty file returns [] | "" | [] |
| TC035 | Missing 'tasks' key returns [] | {"other":"v"} | [] |
| TC036 | Returns Task objects | valid JSON | list of Task instances |
| TC037 | All field values restored | full task JSON | correct attribute values |
| TC038 | Multiple tasks loaded | 3-task JSON | list of length 3 |
| TC039 | Empty tasks array returns [] | {"tasks":[]} | [] |

### Category 7 — save_tasks() (tests/test_storage.py :: TestSaveTasks)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC040 | Creates file if missing | save to new path | file exists after |
| TC041 | Empty list writes valid JSON | save([]) | {"tasks":[]} on disk |
| TC042 | Correct values written | Task with all fields | matching JSON |
| TC043 | Creates directory if missing | path with new subdir | dir created |
| TC044 | Saves multiple tasks | 3 tasks | 3 entries in JSON |

### Category 8 — Round-trip (tests/test_storage.py :: TestRoundTrip)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC045 | All fields preserved | save then load | identical tasks |
| TC046 | Empty list round-trip | save([]) then load | [] |
| TC047 | Second save overwrites | save v1 then save v2 | only v2 on disk |

### Category 9 — get_next_id() (tests/test_task_manager.py :: TestGetNextId)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC048 | Empty list → 1 | [] | 1 |
| TC049 | Single task (ID 1) → 2 | [Task(1,...)] | 2 |
| TC050 | Sequential IDs (1,2,3) → 4 | [Task(1),Task(2),Task(3)] | 4 |
| TC051 | Gap after deletion (1,3) → 4 | [Task(1),Task(3)] | 4 |
| TC052 | Large ID (100) → 101 | [Task(100,...)] | 101 |

### Category 10 — find_task_by_id() (tests/test_task_manager.py :: TestFindTaskById)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC053 | Finds existing task | tasks, id=1 | Task with id 1 |
| TC054 | Finds last task | tasks, id=3 | Task with id 3 |
| TC055 | Non-existent ID → None | tasks, id=999 | None |
| TC056 | Empty list → None | [], id=1 | None |
| TC057 | Returns Task instance | tasks, id=2 | isinstance(result, Task) |

### Category 11 — filter_tasks() (tests/test_task_manager.py :: TestFilterTasks)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC058 | Filter pending | status="pending" | 2 pending tasks |
| TC059 | Filter completed | status="completed" | 1 completed task |
| TC060 | Filter high priority | priority="high" | 1 task |
| TC061 | Filter medium priority | priority="medium" | 1 task |
| TC062 | Filter low priority | priority="low" | 1 task |
| TC063 | No criteria → all tasks | no args | all 3 tasks |
| TC064 | No matching results → [] | status="completed", priority="high" | [] |
| TC065 | Does not modify original | filter call | original list unchanged |
| TC066 | Empty list → [] | [] | [] |

### Category 12 — validate_date() (tests/test_task_manager.py :: TestValidateDate)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC067 | Valid date → True | "2026-09-14" | True |
| TC068 | Empty string → True | "" | True |
| TC069 | Future date → True | "2030-12-31" | True |
| TC070 | Past date → True | "2020-01-01" | True |
| TC071 | Slash separator → False | "2026/09/14" | False |
| TC072 | Wrong order → False | "14-09-2026" | False |
| TC073 | Plain text → False | "tomorrow" | False |
| TC074 | Month 13 → False | "2026-13-01" | False |
| TC075 | Day 32 → False | "2026-01-32" | False |
| TC076 | Partial date → False | "2026-09" | False |

### Category 13 — get_summary() (tests/test_task_manager.py :: TestGetSummary)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC077 | Empty list → zeros | [] | all counts 0 |
| TC078 | All pending | 2 pending | pending=2, completed=0 |
| TC079 | All completed | 2 completed | completed=2, overdue=0 |
| TC080 | Overdue count | 1 overdue pending, 1 future pending, 1 done | overdue=1 |
| TC081 | Returns dict | [] | isinstance(result, dict) |
| TC082 | All keys present | [] | total, completed, pending, overdue |

### Category 14 — format_task_table() (tests/test_task_manager.py :: TestFormatTaskTable)

| ID  | Purpose | Input | Expected |
|-----|---------|-------|----------|
| TC083 | Empty list → message | [] | "No tasks found." |
| TC084 | Title in table | Task with title | title in output |
| TC085 | ID in table | Task(42,...) | "42" in output |
| TC086 | Priority in table | priority="high" | "high" in output |
| TC087 | Status in table | status="completed" | "completed" in output |
| TC088 | Overdue marked | past due + pending | "[OVERDUE]" in output |
| TC089 | Non-overdue not marked | future due | "[OVERDUE]" not in output |
| TC090 | No due date shows 'none' | due="" | "none" in output |
| TC091 | Multiple tasks all shown | 3 tasks | all 3 titles in output |
| TC092 | Returns string | any input | isinstance(result, str) |

---

## Manual Verification Cases

These cover full end-to-end CLI flows tested by running `python3 main.py`.

| ID   | Scenario | Steps | Expected |
|------|----------|-------|----------|
| MV01 | Add task and verify persistence | Add task, exit, relaunch | Task still present |
| MV02 | Invalid menu input | Enter "9", "abc", "" | Error message, menu re-shown |
| MV03 | Add task with empty title | Enter blank at title prompt | Error shown, re-prompted |
| MV04 | Add task with invalid priority | Enter "urgent" | Error shown, re-prompted |
| MV05 | Add task with invalid date | Enter "13/09/2026" | Error shown, re-prompted |
| MV06 | Mark non-existent ID complete | Enter ID 999 | "No task found" message |
| MV07 | Delete with confirmation | Enter "yes" | Task removed |
| MV08 | Delete without confirmation | Enter "no" | Task kept |
| MV09 | Filter by pending | Select status filter → pending | Only pending tasks shown |
| MV10 | Summary with mixed tasks | Add 2 pending (1 overdue) + 1 complete | Correct counts |
| MV11 | View task detail | Enter valid ID | All fields displayed |
| MV12 | Mark already-complete task | Complete a completed task | Info message, no error |
| MV13 | List with no tasks | Fresh install, list tasks | "No tasks found." |
| MV14 | Exit cleanly | Choose option 8 | "Goodbye!" printed |
