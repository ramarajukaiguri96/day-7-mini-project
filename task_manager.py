"""
task_manager.py — Business logic functions

This module contains all the functions that operate on the list of tasks.
It sits between the CLI (main.py) and the data layer (storage.py).

None of these functions read from or write to the file — that is storage.py's
job. These functions only work with Python lists and Task objects in memory.

Having logic here (instead of in main.py) keeps the CLI code short and clean,
and makes it easy to test each piece of logic independently.
"""

from datetime import date, datetime
from task import Task


# ------------------------------------------------------------------
# ID management
# ------------------------------------------------------------------

def get_next_id(tasks: list) -> int:
    """
    Return the next available task ID.

    IDs are assigned as simple incrementing integers (1, 2, 3, ...).
    This function finds the highest existing ID and adds 1. If there
    are no tasks yet, it starts at 1.

    Why not just use len(tasks) + 1? Because if tasks have been deleted,
    len() would recycle old IDs. Using max() ensures IDs are always unique,
    even after deletions.

    Parameters:
        tasks (list[Task]): The current list of all tasks.

    Returns:
        int: The next ID to use for a new task.
    """
    if not tasks:
        return 1
    return max(task.task_id for task in tasks) + 1


# ------------------------------------------------------------------
# Lookup
# ------------------------------------------------------------------

def find_task_by_id(tasks: list, task_id: int):
    """
    Find and return a single task by its numeric ID.

    Searches the list for a task whose task_id matches the given value.
    Returns None if no match is found, rather than raising an exception —
    the caller is responsible for handling the "not found" case.

    Parameters:
        tasks (list[Task]): The full list of tasks to search.
        task_id (int): The ID to look for.

    Returns:
        Task or None: The matching Task, or None if not found.
    """
    for task in tasks:
        if task.task_id == task_id:
            return task
    return None


# ------------------------------------------------------------------
# Filtering
# ------------------------------------------------------------------

def filter_tasks(tasks: list, status: str = None, priority: str = None) -> list:
    """
    Return a filtered subset of tasks matching the given criteria.

    Both parameters are optional. If neither is provided, all tasks are
    returned. If both are provided, only tasks matching BOTH criteria
    are returned.

    This function does not modify the original list — it returns a new list.

    Parameters:
        tasks (list[Task]): The full list of tasks.
        status (str or None): Filter by "pending" or "completed". None = no filter.
        priority (str or None): Filter by "high", "medium", or "low". None = no filter.

    Returns:
        list[Task]: Tasks that match all supplied criteria.
    """
    result = tasks

    # Apply status filter if provided.
    if status is not None:
        result = [t for t in result if t.status == status]

    # Apply priority filter if provided.
    if priority is not None:
        result = [t for t in result if t.priority == priority]

    return result


# ------------------------------------------------------------------
# Validation
# ------------------------------------------------------------------

def validate_date(date_str: str) -> bool:
    """
    Check whether a string is a valid date in YYYY-MM-DD format, or empty.

    An empty string is valid because due date is optional — the user can
    press Enter to skip setting a due date.

    We use datetime.strptime() to parse the string. If it raises a
    ValueError, the format is wrong and we return False.

    Parameters:
        date_str (str): The date string to validate (e.g. "2026-09-14" or "").

    Returns:
        bool: True if the string is valid or empty, False otherwise.
    """
    # Empty string is acceptable — means "no due date".
    if date_str == "":
        return True

    # Try parsing the string as YYYY-MM-DD.
    # If strptime raises ValueError, the format is wrong.
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ------------------------------------------------------------------
# Summary calculation
# ------------------------------------------------------------------

def get_summary(tasks: list) -> dict:
    """
    Calculate summary statistics for the current task list.

    Counts how many tasks are in each category. Used by the Summary
    menu option to give the user a quick overview.

    Parameters:
        tasks (list[Task]): The full list of tasks.

    Returns:
        dict: A dictionary with keys:
              "total"     — total number of tasks
              "completed" — tasks with status "completed"
              "pending"   — tasks with status "pending"
              "overdue"   — pending tasks whose due date has passed
    """
    total = len(tasks)
    completed = sum(1 for t in tasks if t.status == Task.STATUS_COMPLETED)
    pending = sum(1 for t in tasks if t.status == Task.STATUS_PENDING)

    # Overdue = pending AND due date is in the past.
    # We use the Task's own is_overdue() method to keep the logic centralised.
    overdue = sum(1 for t in tasks if t.is_overdue())

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "overdue": overdue,
    }


# ------------------------------------------------------------------
# Display formatting
# ------------------------------------------------------------------

def format_task_table(tasks: list) -> str:
    """
    Format a list of tasks as a readable table string for terminal output.

    Produces a table with fixed-width columns for ID, Status, Priority,
    Due Date, and Title. Overdue tasks are marked with [OVERDUE] in the
    title column so the user can spot them immediately.

    If the list is empty, returns a message saying so — the function never
    crashes on an empty list.

    Parameters:
        tasks (list[Task]): The tasks to display.

    Returns:
        str: A multi-line formatted table, or a "no tasks" message.
    """
    if not tasks:
        return "No tasks found."

    # Build the header row with fixed column widths.
    # The widths are chosen to fit typical values without wrapping.
    header = (
        f"{'ID':<4}  {'Status':<10}  {'Priority':<8}  "
        f"{'Due Date':<12}  {'Title'}"
    )
    separator = "-" * 70

    rows = [header, separator]

    for task in tasks:
        # Show "none" for empty due dates so the column is not blank.
        due = task.due_date if task.due_date else "none"

        # Append [OVERDUE] to the title for past-due pending tasks.
        title = task.title
        if task.is_overdue():
            title += " [OVERDUE]"

        row = (
            f"{task.task_id:<4}  {task.status:<10}  {task.priority:<8}  "
            f"{due:<12}  {title}"
        )
        rows.append(row)

    return "\n".join(rows)
