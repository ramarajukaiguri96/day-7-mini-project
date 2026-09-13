# Architecture

## Overview

This is a single-user, local CLI application. There is no server, no database,
no network connection, and no external dependencies. Everything runs on the
user's own machine.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│                     User                        │
│         (types commands in the terminal)        │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│                   main.py                       │
│         CLI menu loop and user prompts          │
│   Reads input → calls logic → prints output     │
└──────┬──────────────────────────────────────────┘
       │                         │
       ▼                         ▼
┌─────────────┐         ┌────────────────────┐
│   task.py   │         │  task_manager.py   │
│ Task class  │◄────────│  Business logic    │
│ (data model)│         │  filter, validate, │
└─────────────┘         │  format, get_id    │
                        └────────┬───────────┘
                                 │
                                 ▼
                        ┌────────────────────┐
                        │    storage.py      │
                        │  load_tasks()      │
                        │  save_tasks()      │
                        └────────┬───────────┘
                                 │
                                 ▼
                        ┌────────────────────┐
                        │  data/tasks.json   │
                        │  Local JSON file   │
                        │  (auto-created)    │
                        └────────────────────┘
```

---

## Components

| Component        | Type         | Description                                      |
|------------------|--------------|--------------------------------------------------|
| main.py          | Entry point  | Menu loop, user prompts, display results         |
| task.py          | Data model   | Task class — represents one task                 |
| task_manager.py  | Logic layer  | Functions that operate on lists of tasks         |
| storage.py       | I/O layer    | Read/write tasks.json                            |
| data/tasks.json  | Storage      | Plain JSON file on the local filesystem          |

---

## What Is Not Used (and Why)

| Technology     | Status       | Reason                                               |
|----------------|--------------|------------------------------------------------------|
| PostgreSQL     | NOT USED     | JSON file is sufficient; no database needed          |
| AWS            | NOT USED     | Local execution; no cloud required                   |
| Flask/FastAPI  | NOT USED     | CLI tool; no web server needed                       |
| React/HTML/CSS | NOT USED     | Terminal UI only                                     |
| Third-party packages | NOT USED | Python stdlib covers all requirements            |
| .env file      | NOT USED     | No secrets or environment-specific config            |
| Docker         | NOT USED     | Not required by the assignment                       |
