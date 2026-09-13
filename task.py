"""
task.py — Task class definition

This module defines the Task class, which is the core data object of the
application. Every task the user creates is represented as a Task instance.

A Task holds all the information about a single to-do item: its title,
priority, due date, status, and so on. The class also provides methods
for converting to/from JSON-friendly dictionaries (for saving to disk)
and for checking whether the task is overdue.
"""

from datetime import date


class Task:
    """
    Represents a single task in the task manager.

    A Task stores all the data for one to-do item and provides methods
    to update its state (mark complete), check its state (is_overdue),
    and convert it to/from a dictionary for JSON storage.

    Attributes:
        task_id (int): Unique numeric ID assigned automatically.
        title (str): Short description of the task (required).
        description (str): Optional longer detail about the task.
        priority (str): Importance level — "high", "medium", or "low".
        due_date (str): Target completion date in "YYYY-MM-DD" format,
                        or empty string if no due date is set.
        status (str): Current state — "pending" or "completed".
        created_at (str): Date the task was created, in "YYYY-MM-DD" format.
    """

    # The two allowed status values. Using constants avoids typos elsewhere.
    STATUS_PENDING = "pending"
    STATUS_COMPLETED = "completed"

    # The three allowed priority values.
    VALID_PRIORITIES = ("high", "medium", "low")

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str = "",
        priority: str = "medium",
        due_date: str = "",
        status: str = "pending",
        created_at: str = "",
    ):
        """
        Create a new Task object.

        Parameters:
            task_id (int): Unique identifier for this task.
            title (str): What the task is. Must not be empty.
            description (str): Optional extra detail. Defaults to "".
            priority (str): "high", "medium", or "low". Defaults to "medium".
            due_date (str): "YYYY-MM-DD" or "". Defaults to "" (no due date).
            status (str): "pending" or "completed". Defaults to "pending".
            created_at (str): "YYYY-MM-DD". Defaults to today's date.
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

        # If created_at is not supplied (e.g. when creating a new task),
        # automatically set it to today's date.
        self.created_at = created_at if created_at else date.today().isoformat()

    # ------------------------------------------------------------------
    # Serialisation — converting between Task objects and dictionaries
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Convert this Task to a plain Python dictionary.

        This is needed for JSON storage: json.dump() can only write
        plain dicts and lists, not custom objects. Calling to_dict()
        on every task produces a list of dicts that json.dump() can save.

        Returns:
            dict: All task fields as key-value pairs.
        """
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """
        Create a Task object from a dictionary (e.g. loaded from JSON).

        This is the reverse of to_dict(). When we read tasks.json, we get
        a list of plain dicts. from_dict() turns each dict back into a
        proper Task object so the rest of the application can use it.

        Parameters:
            data (dict): A dictionary with the same keys as to_dict() produces.

        Returns:
            Task: A fully populated Task instance.
        """
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date", ""),
            status=data.get("status", "pending"),
            created_at=data.get("created_at", ""),
        )

    # ------------------------------------------------------------------
    # State checks
    # ------------------------------------------------------------------

    def is_overdue(self) -> bool:
        """
        Check whether this task is overdue.

        A task is overdue when ALL of these are true:
          1. A due date has been set (due_date is not empty).
          2. The due date is in the past (before today).
          3. The task has not been completed yet.

        Completed tasks are never considered overdue, even if their due
        date has passed — the work is done.

        Returns:
            bool: True if the task is overdue, False otherwise.
        """
        # If no due date is set, the task cannot be overdue.
        if not self.due_date:
            return False

        # Completed tasks are never overdue.
        if self.status == self.STATUS_COMPLETED:
            return False

        # Parse the stored date string and compare with today.
        # If due_date is not a valid date string, treat as not overdue
        # rather than crashing — storage layer validates on write.
        try:
            due = date.fromisoformat(self.due_date)
            return due < date.today()
        except ValueError:
            return False

    # ------------------------------------------------------------------
    # State changes
    # ------------------------------------------------------------------

    def mark_complete(self) -> None:
        """
        Mark this task as completed.

        Sets the status to "completed". Calling this on a task that is
        already completed is safe — it just leaves the status unchanged.
        """
        self.status = self.STATUS_COMPLETED

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Return a short, human-readable summary of the task.

        Used when printing a single task to the terminal. Shows the most
        important fields in a compact one-line format.

        Returns:
            str: A formatted summary string.
        """
        # Show [OVERDUE] tag so the user can spot urgent tasks immediately.
        overdue_tag = " [OVERDUE]" if self.is_overdue() else ""
        due = self.due_date if self.due_date else "no due date"
        return (
            f"[{self.task_id}] {self.title} "
            f"| {self.priority} | {self.status} "
            f"| due: {due}{overdue_tag}"
        )
