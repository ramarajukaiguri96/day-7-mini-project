"""
main.py — Entry point and CLI menu

This is the file you run to start the application:
    python3 main.py

It handles everything the user sees and types:
  - Displaying the main menu
  - Reading the user's choice
  - Calling the right action for each choice
  - Showing results back to the user

main.py is deliberately kept as simple as possible. It does not contain
business logic — that lives in task_manager.py. It does not touch the
file directly — that is storage.py's job. main.py only handles user
interaction: show menu → read input → call function → show output.
"""

from storage import load_tasks, save_tasks
from task import Task
from task_manager import (
    get_next_id,
    find_task_by_id,
    filter_tasks,
    validate_date,
    get_summary,
    format_task_table,
)


# ------------------------------------------------------------------
# Menu display
# ------------------------------------------------------------------

def show_menu() -> None:
    """
    Print the main menu to the terminal.

    Called at the start of every loop iteration so the user always
    knows what options are available.
    """
    print("\n╔══════════════════════════════╗")
    print("║       TASK MANAGER CLI       ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add task                 ║")
    print("║  2. List all tasks           ║")
    print("║  3. View task detail         ║")
    print("║  4. Mark task complete       ║")
    print("║  5. Delete task              ║")
    print("║  6. Filter tasks             ║")
    print("║  7. Summary                  ║")
    print("║  8. Exit                     ║")
    print("╚══════════════════════════════╝")


# ------------------------------------------------------------------
# Input helpers — reusable prompt functions
# ------------------------------------------------------------------

def prompt_task_id(tasks: list, action: str) -> int | None:
    """
    Prompt the user to enter a task ID and validate it.

    Used by several menu options (view, complete, delete) that need the
    user to specify which task to act on.

    Validation:
      - The input must be a valid integer (catches "abc", "1.5", etc.)
      - The ID must exist in the current task list (catches "999")

    Parameters:
        tasks (list[Task]): Current list of tasks (used to validate the ID).
        action (str): A short description used in the prompt (e.g. "complete").

    Returns:
        int or None: The validated task ID, or None if the user entered
                     something invalid.
    """
    raw = input(f"Enter task ID to {action}: ").strip()

    # Check that the input is an integer.
    try:
        task_id = int(raw)
    except ValueError:
        print(f"❌ '{raw}' is not a valid ID. Please enter a number.")
        return None

    # Check that a task with this ID actually exists.
    task = find_task_by_id(tasks, task_id)
    if task is None:
        print(f"❌ No task found with ID {task_id}.")
        return None

    return task_id


# ------------------------------------------------------------------
# Action: Add a task
# ------------------------------------------------------------------

def add_task(tasks: list) -> None:
    """
    Prompt the user for task details, create a new Task, and save it.

    Fields collected:
      - Title (required — cannot be empty)
      - Priority (required — must be high/medium/low)
      - Due date (optional — leave blank for no due date)
      - Description (optional — any text or blank)

    The new task is appended to the tasks list and saved to disk.

    Parameters:
        tasks (list[Task]): The current list; the new task is appended in-place.
    """
    print("\n--- Add New Task ---")

    # --- Title ---
    # Keep prompting until the user provides a non-empty title.
    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("❌ Title cannot be empty. Please enter a title.")

    # --- Priority ---
    # Keep prompting until the user enters one of the three valid values.
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in Task.VALID_PRIORITIES:
            break
        print(f"❌ Invalid priority. Please enter one of: high, medium, low.")

    # --- Due date ---
    # Optional field. Keep prompting until the user enters a valid date
    # or presses Enter to skip.
    while True:
        due_date = input("Due date (YYYY-MM-DD or leave blank): ").strip()
        if validate_date(due_date):
            break
        print("❌ Invalid date format. Please use YYYY-MM-DD (e.g. 2026-09-14), or press Enter to skip.")

    # --- Description ---
    # Fully optional — any input is accepted, including blank.
    description = input("Description (optional): ").strip()

    # Create the Task object. task_id is auto-assigned using the helper.
    new_task = Task(
        task_id=get_next_id(tasks),
        title=title,
        description=description,
        priority=priority,
        due_date=due_date,
    )

    # Add to the in-memory list and immediately persist to disk.
    tasks.append(new_task)
    save_tasks(tasks)

    print(f"✅ Task added (ID: {new_task.task_id})")


# ------------------------------------------------------------------
# Action: List all tasks
# ------------------------------------------------------------------

def list_tasks(tasks: list) -> None:
    """
    Display all tasks in a formatted table.

    If there are no tasks, shows a helpful message instead of an empty table.

    Parameters:
        tasks (list[Task]): The current list of tasks.
    """
    print("\n--- All Tasks ---")
    print(format_task_table(tasks))


# ------------------------------------------------------------------
# Action: View task detail
# ------------------------------------------------------------------

def view_task_detail(tasks: list) -> None:
    """
    Show all fields for a single task identified by its ID.

    The list view only shows a summary. This option lets the user see
    the full description and all fields for a specific task.

    Parameters:
        tasks (list[Task]): The current list of tasks.
    """
    if not tasks:
        print("No tasks to view.")
        return

    print("\n--- View Task Detail ---")
    task_id = prompt_task_id(tasks, "view")
    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)

    # Display all fields clearly labelled.
    overdue_note = "  ⚠️  OVERDUE" if task.is_overdue() else ""
    print(f"\n  ID          : {task.task_id}")
    print(f"  Title       : {task.title}")
    print(f"  Description : {task.description if task.description else '(none)'}")
    print(f"  Priority    : {task.priority}")
    print(f"  Due Date    : {task.due_date if task.due_date else '(none)'}{overdue_note}")
    print(f"  Status      : {task.status}")
    print(f"  Created     : {task.created_at}")


# ------------------------------------------------------------------
# Action: Mark a task as complete
# ------------------------------------------------------------------

def mark_task_complete(tasks: list) -> None:
    """
    Find a task by ID and mark it as completed.

    If the task is already completed, informs the user without making
    any change or causing an error.

    Parameters:
        tasks (list[Task]): The current list; the matched task is updated in-place.
    """
    if not tasks:
        print("No tasks to complete.")
        return

    print("\n--- Mark Task Complete ---")
    task_id = prompt_task_id(tasks, "mark complete")
    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)

    # Inform the user if the task is already done.
    if task.status == Task.STATUS_COMPLETED:
        print(f"ℹ️  Task {task_id} is already marked as completed.")
        return

    # Mark as complete and save immediately.
    task.mark_complete()
    save_tasks(tasks)
    print(f"✅ Task {task_id} marked as completed.")


# ------------------------------------------------------------------
# Action: Delete a task
# ------------------------------------------------------------------

def delete_task(tasks: list) -> None:
    """
    Remove a task permanently by its ID.

    Once deleted, the task is gone — there is no undo. The user is asked
    to confirm before the deletion happens.

    Parameters:
        tasks (list[Task]): The current list; the matched task is removed in-place.
    """
    if not tasks:
        print("No tasks to delete.")
        return

    print("\n--- Delete Task ---")
    task_id = prompt_task_id(tasks, "delete")
    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)

    # Ask for confirmation before deleting — deletion cannot be undone.
    confirm = input(f"Delete '{task.title}'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return

    # Remove the task from the list and save immediately.
    tasks.remove(task)
    save_tasks(tasks)
    print(f"✅ Task {task_id} deleted.")


# ------------------------------------------------------------------
# Action: Filter tasks
# ------------------------------------------------------------------

def filter_tasks_menu(tasks: list) -> None:
    """
    Show a sub-menu to filter tasks by status or priority.

    Lets the user narrow down the task list to just what they care about:
    e.g. "show me only high-priority tasks" or "show me pending tasks".

    Parameters:
        tasks (list[Task]): The current list of tasks.
    """
    if not tasks:
        print("No tasks to filter.")
        return

    print("\n--- Filter Tasks ---")
    print("  1. Filter by status   (pending / completed)")
    print("  2. Filter by priority (high / medium / low)")

    choice = input("Filter by (1/2): ").strip()

    if choice == "1":
        # --- Filter by status ---
        status = input("Status (pending/completed): ").strip().lower()
        if status not in ("pending", "completed"):
            print("❌ Invalid status. Use 'pending' or 'completed'.")
            return
        result = filter_tasks(tasks, status=status)
        label = f"Tasks with status '{status}'"

    elif choice == "2":
        # --- Filter by priority ---
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority not in Task.VALID_PRIORITIES:
            print(f"❌ Invalid priority. Use one of: high, medium, low.")
            return
        result = filter_tasks(tasks, priority=priority)
        label = f"Tasks with priority '{priority}'"

    else:
        print("❌ Invalid choice. Please enter 1 or 2.")
        return

    # Display the filtered results.
    print(f"\n--- {label} ---")
    print(format_task_table(result))


# ------------------------------------------------------------------
# Action: Summary
# ------------------------------------------------------------------

def show_summary(tasks: list) -> None:
    """
    Display a count summary of all tasks grouped by state.

    Shows total, completed, pending, and overdue counts. Useful for a
    quick overview without scrolling through the full task list.

    Parameters:
        tasks (list[Task]): The current list of tasks.
    """
    print("\n📋 Task Summary")
    print("---------------")

    if not tasks:
        print("No tasks recorded yet.")
        return

    summary = get_summary(tasks)
    print(f"Total tasks   : {summary['total']}")
    print(f"Completed     : {summary['completed']}")
    print(f"Pending       : {summary['pending']}")
    print(f"Overdue       : {summary['overdue']}")


# ------------------------------------------------------------------
# Main loop
# ------------------------------------------------------------------

def main() -> None:
    """
    The main entry point for the Task Manager CLI.

    Loads tasks from disk, then runs a loop that:
      1. Shows the menu.
      2. Reads the user's choice.
      3. Calls the appropriate action function.
      4. Repeats until the user chooses Exit.

    The loop never crashes on bad input — invalid choices just show
    an error message and display the menu again.
    """
    # Load existing tasks from data/tasks.json.
    # If the file doesn't exist, this returns an empty list.
    tasks = load_tasks()

    # Keep running until the user explicitly chooses to exit.
    while True:
        show_menu()
        choice = input("Choose option (1-8): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            view_task_detail(tasks)
        elif choice == "4":
            mark_task_complete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            filter_tasks_menu(tasks)
        elif choice == "7":
            show_summary(tasks)
        elif choice == "8":
            # Clean exit — tell the user the application is closing.
            print("\nGoodbye! Your tasks are saved.")
            break
        else:
            # Any input that is not 1–8 lands here.
            # Show a helpful message and loop back to the menu.
            print(f"❌ '{choice}' is not a valid option. Please enter a number from 1 to 8.")


# Standard Python entry-point guard.
# This ensures main() only runs when the file is executed directly
# (python3 main.py), not when it is imported by tests or other modules.
if __name__ == "__main__":
    main()
