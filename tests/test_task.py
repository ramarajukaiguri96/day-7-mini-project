"""
tests/test_task.py — Unit tests for the Task class

Tests cover:
  - Creating Task objects with various inputs
  - to_dict() serialisation
  - from_dict() deserialisation and round-trip
  - is_overdue() behaviour under different date/status combinations
  - mark_complete() state transition
  - __str__() output
"""

import unittest
from datetime import date, timedelta
from task import Task


class TestTaskCreation(unittest.TestCase):
    """Tests for creating Task objects and verifying their attributes."""

    def test_create_task_all_fields(self):
        """A Task created with all fields stores them correctly."""
        t = Task(
            task_id=1,
            title="Write tests",
            description="Cover all edge cases",
            priority="high",
            due_date="2026-09-14",
            status="pending",
            created_at="2026-09-13",
        )
        self.assertEqual(t.task_id, 1)
        self.assertEqual(t.title, "Write tests")
        self.assertEqual(t.description, "Cover all edge cases")
        self.assertEqual(t.priority, "high")
        self.assertEqual(t.due_date, "2026-09-14")
        self.assertEqual(t.status, "pending")
        self.assertEqual(t.created_at, "2026-09-13")

    def test_create_task_minimal(self):
        """A Task created with only required fields uses correct defaults."""
        t = Task(task_id=2, title="Minimal task")
        self.assertEqual(t.task_id, 2)
        self.assertEqual(t.title, "Minimal task")
        self.assertEqual(t.description, "")
        self.assertEqual(t.priority, "medium")
        self.assertEqual(t.due_date, "")
        self.assertEqual(t.status, "pending")
        # created_at should be auto-set to today's date
        self.assertEqual(t.created_at, date.today().isoformat())

    def test_created_at_auto_set_when_empty(self):
        """created_at is automatically set to today if not provided."""
        t = Task(task_id=3, title="Auto date task", created_at="")
        self.assertEqual(t.created_at, date.today().isoformat())

    def test_created_at_preserved_when_provided(self):
        """created_at is kept as supplied when explicitly provided."""
        t = Task(task_id=4, title="Old task", created_at="2025-01-01")
        self.assertEqual(t.created_at, "2025-01-01")

    def test_title_stored_as_given(self):
        """Title is stored exactly as provided — no automatic trimming in __init__."""
        t = Task(task_id=5, title="  My Task  ")
        self.assertEqual(t.title, "  My Task  ")

    def test_priority_high(self):
        """High priority is stored correctly."""
        t = Task(task_id=6, title="Urgent", priority="high")
        self.assertEqual(t.priority, "high")

    def test_priority_medium(self):
        """Medium priority is the default."""
        t = Task(task_id=7, title="Normal")
        self.assertEqual(t.priority, "medium")

    def test_priority_low(self):
        """Low priority is stored correctly."""
        t = Task(task_id=8, title="Whenever", priority="low")
        self.assertEqual(t.priority, "low")

    def test_empty_due_date(self):
        """Empty due date string is stored without error."""
        t = Task(task_id=9, title="No deadline", due_date="")
        self.assertEqual(t.due_date, "")

    def test_status_defaults_to_pending(self):
        """New tasks start with status 'pending'."""
        t = Task(task_id=10, title="Fresh task")
        self.assertEqual(t.status, Task.STATUS_PENDING)


class TestTaskSerialization(unittest.TestCase):
    """Tests for to_dict() and from_dict() — converting between Task and dict."""

    def setUp(self):
        """Create a standard task used by several tests."""
        self.task = Task(
            task_id=1,
            title="Serialisation test",
            description="Check round-trip",
            priority="medium",
            due_date="2026-10-01",
            status="pending",
            created_at="2026-09-13",
        )

    def test_to_dict_returns_dict(self):
        """to_dict() returns a Python dictionary."""
        result = self.task.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_contains_all_keys(self):
        """to_dict() dictionary contains all expected keys."""
        result = self.task.to_dict()
        expected_keys = {"task_id", "title", "description", "priority",
                         "due_date", "status", "created_at"}
        self.assertEqual(set(result.keys()), expected_keys)

    def test_to_dict_values_correct(self):
        """to_dict() dictionary values match the Task's attributes."""
        result = self.task.to_dict()
        self.assertEqual(result["task_id"], 1)
        self.assertEqual(result["title"], "Serialisation test")
        self.assertEqual(result["description"], "Check round-trip")
        self.assertEqual(result["priority"], "medium")
        self.assertEqual(result["due_date"], "2026-10-01")
        self.assertEqual(result["status"], "pending")
        self.assertEqual(result["created_at"], "2026-09-13")

    def test_from_dict_creates_task(self):
        """from_dict() creates a Task instance from a dictionary."""
        data = {
            "task_id": 2,
            "title": "From dict",
            "description": "Created from a dict",
            "priority": "low",
            "due_date": "2026-11-01",
            "status": "completed",
            "created_at": "2026-09-01",
        }
        t = Task.from_dict(data)
        self.assertIsInstance(t, Task)
        self.assertEqual(t.task_id, 2)
        self.assertEqual(t.title, "From dict")
        self.assertEqual(t.status, "completed")

    def test_round_trip_to_dict_from_dict(self):
        """Converting to dict and back produces an identical Task."""
        original = self.task
        restored = Task.from_dict(original.to_dict())
        self.assertEqual(restored.task_id, original.task_id)
        self.assertEqual(restored.title, original.title)
        self.assertEqual(restored.description, original.description)
        self.assertEqual(restored.priority, original.priority)
        self.assertEqual(restored.due_date, original.due_date)
        self.assertEqual(restored.status, original.status)
        self.assertEqual(restored.created_at, original.created_at)

    def test_from_dict_missing_optional_fields_use_defaults(self):
        """from_dict() uses defaults when optional keys are missing."""
        data = {"task_id": 3, "title": "Sparse task"}
        t = Task.from_dict(data)
        self.assertEqual(t.description, "")
        self.assertEqual(t.priority, "medium")
        self.assertEqual(t.due_date, "")
        self.assertEqual(t.status, "pending")


class TestTaskIsOverdue(unittest.TestCase):
    """Tests for is_overdue() — checking whether a task is past its due date."""

    def _past_date(self):
        """Return a date string guaranteed to be in the past."""
        return (date.today() - timedelta(days=1)).isoformat()

    def _future_date(self):
        """Return a date string guaranteed to be in the future."""
        return (date.today() + timedelta(days=1)).isoformat()

    def test_overdue_past_date_pending(self):
        """A pending task with a past due date is overdue."""
        t = Task(1, "Overdue", due_date=self._past_date(), status="pending")
        self.assertTrue(t.is_overdue())

    def test_not_overdue_future_date_pending(self):
        """A pending task with a future due date is not overdue."""
        t = Task(2, "Future", due_date=self._future_date(), status="pending")
        self.assertFalse(t.is_overdue())

    def test_not_overdue_past_date_completed(self):
        """A completed task is never overdue, even with a past due date."""
        t = Task(3, "Done", due_date=self._past_date(), status="completed")
        self.assertFalse(t.is_overdue())

    def test_not_overdue_no_due_date(self):
        """A task with no due date is never overdue."""
        t = Task(4, "No deadline", due_date="")
        self.assertFalse(t.is_overdue())

    def test_not_overdue_future_date_completed(self):
        """A completed task with a future due date is not overdue."""
        t = Task(5, "Early finisher", due_date=self._future_date(), status="completed")
        self.assertFalse(t.is_overdue())

    def test_overdue_today_is_not_overdue(self):
        """A task due today (not in the past) is not yet overdue."""
        # Due today means due date == today, which is NOT < today.
        today = date.today().isoformat()
        t = Task(6, "Due today", due_date=today, status="pending")
        self.assertFalse(t.is_overdue())

    def test_invalid_date_string_not_overdue(self):
        """A task with an unparseable due_date string is treated as not overdue."""
        t = Task(7, "Bad date", due_date="not-a-date", status="pending")
        self.assertFalse(t.is_overdue())


class TestTaskMarkComplete(unittest.TestCase):
    """Tests for mark_complete() — changing a task's status."""

    def test_mark_complete_changes_status(self):
        """mark_complete() changes status from pending to completed."""
        t = Task(1, "Do something")
        self.assertEqual(t.status, "pending")
        t.mark_complete()
        self.assertEqual(t.status, "completed")

    def test_mark_complete_already_complete_no_error(self):
        """mark_complete() on an already-completed task does not raise an error."""
        t = Task(2, "Already done", status="completed")
        try:
            t.mark_complete()
        except Exception as e:
            self.fail(f"mark_complete() raised an exception on a completed task: {e}")
        self.assertEqual(t.status, "completed")

    def test_mark_complete_not_overdue_after(self):
        """After marking complete, is_overdue() returns False even for past dates."""
        past = (date.today() - timedelta(days=5)).isoformat()
        t = Task(3, "Late but done", due_date=past)
        self.assertTrue(t.is_overdue())  # overdue before completing
        t.mark_complete()
        self.assertFalse(t.is_overdue())  # not overdue after completing


class TestTaskStr(unittest.TestCase):
    """Tests for __str__() — the short summary string."""

    def test_str_contains_title(self):
        """__str__() output contains the task title."""
        t = Task(1, "My important task", priority="high")
        self.assertIn("My important task", str(t))

    def test_str_contains_id(self):
        """__str__() output contains the task ID."""
        t = Task(42, "Another task")
        self.assertIn("42", str(t))

    def test_str_contains_overdue_tag(self):
        """__str__() includes [OVERDUE] for overdue tasks."""
        past = (date.today() - timedelta(days=1)).isoformat()
        t = Task(1, "Late task", due_date=past)
        self.assertIn("[OVERDUE]", str(t))

    def test_str_no_overdue_tag_for_future(self):
        """__str__() does not include [OVERDUE] for non-overdue tasks."""
        future = (date.today() + timedelta(days=5)).isoformat()
        t = Task(1, "On time task", due_date=future)
        self.assertNotIn("[OVERDUE]", str(t))

    def test_str_is_string(self):
        """__str__() always returns a string."""
        t = Task(1, "Test")
        self.assertIsInstance(str(t), str)


if __name__ == "__main__":
    unittest.main()
