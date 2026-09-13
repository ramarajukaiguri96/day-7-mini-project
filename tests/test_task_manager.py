"""
tests/test_task_manager.py — Unit tests for the business logic functions

Tests cover:
  - get_next_id()
  - find_task_by_id()
  - filter_tasks()
  - validate_date()
  - get_summary()
  - format_task_table()
"""

import unittest
from datetime import date, timedelta
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
# Shared test fixture
# ------------------------------------------------------------------

def make_tasks():
    """
    Create a standard list of tasks used across multiple test classes.

    Returns a list with:
      - Task 1: high priority, pending, future due date
      - Task 2: medium priority, pending, past due date (overdue)
      - Task 3: low priority, completed, no due date
    """
    past = (date.today() - timedelta(days=3)).isoformat()
    future = (date.today() + timedelta(days=7)).isoformat()
    return [
        Task(1, "High priority task", priority="high",
             due_date=future, status="pending"),
        Task(2, "Overdue task", priority="medium",
             due_date=past, status="pending"),
        Task(3, "Completed task", priority="low",
             due_date="", status="completed"),
    ]


# ------------------------------------------------------------------
# get_next_id()
# ------------------------------------------------------------------

class TestGetNextId(unittest.TestCase):
    """Tests for get_next_id() — auto-assigning task IDs."""

    def test_empty_list_returns_one(self):
        """get_next_id() returns 1 when there are no tasks."""
        self.assertEqual(get_next_id([]), 1)

    def test_single_task_returns_two(self):
        """get_next_id() returns 2 when there is one task with ID 1."""
        tasks = [Task(1, "Only task")]
        self.assertEqual(get_next_id(tasks), 2)

    def test_sequential_ids(self):
        """get_next_id() returns max_id + 1 for sequential IDs."""
        tasks = [Task(1, "A"), Task(2, "B"), Task(3, "C")]
        self.assertEqual(get_next_id(tasks), 4)

    def test_gap_after_deletion(self):
        """get_next_id() skips no IDs — uses max + 1, not len + 1."""
        # Simulates tasks 1 and 3 existing after task 2 was deleted.
        tasks = [Task(1, "First"), Task(3, "Third")]
        self.assertEqual(get_next_id(tasks), 4)

    def test_large_id(self):
        """get_next_id() handles a large existing ID correctly."""
        tasks = [Task(100, "Big ID task")]
        self.assertEqual(get_next_id(tasks), 101)


# ------------------------------------------------------------------
# find_task_by_id()
# ------------------------------------------------------------------

class TestFindTaskById(unittest.TestCase):
    """Tests for find_task_by_id() — looking up tasks by ID."""

    def setUp(self):
        self.tasks = make_tasks()

    def test_find_existing_id(self):
        """find_task_by_id() returns the correct task for a valid ID."""
        result = find_task_by_id(self.tasks, 1)
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "High priority task")

    def test_find_last_task(self):
        """find_task_by_id() finds the last task in the list."""
        result = find_task_by_id(self.tasks, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Completed task")

    def test_find_non_existent_id_returns_none(self):
        """find_task_by_id() returns None for an ID that does not exist."""
        result = find_task_by_id(self.tasks, 999)
        self.assertIsNone(result)

    def test_find_in_empty_list_returns_none(self):
        """find_task_by_id() returns None when the task list is empty."""
        result = find_task_by_id([], 1)
        self.assertIsNone(result)

    def test_find_returns_task_instance(self):
        """find_task_by_id() returns a Task object, not a dict."""
        result = find_task_by_id(self.tasks, 2)
        self.assertIsInstance(result, Task)


# ------------------------------------------------------------------
# filter_tasks()
# ------------------------------------------------------------------

class TestFilterTasks(unittest.TestCase):
    """Tests for filter_tasks() — filtering by status and/or priority."""

    def setUp(self):
        self.tasks = make_tasks()

    def test_filter_by_pending_status(self):
        """filter_tasks(status='pending') returns only pending tasks."""
        result = filter_tasks(self.tasks, status="pending")
        self.assertEqual(len(result), 2)
        for t in result:
            self.assertEqual(t.status, "pending")

    def test_filter_by_completed_status(self):
        """filter_tasks(status='completed') returns only completed tasks."""
        result = filter_tasks(self.tasks, status="completed")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].status, "completed")

    def test_filter_by_high_priority(self):
        """filter_tasks(priority='high') returns only high-priority tasks."""
        result = filter_tasks(self.tasks, priority="high")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].priority, "high")

    def test_filter_by_medium_priority(self):
        """filter_tasks(priority='medium') returns only medium-priority tasks."""
        result = filter_tasks(self.tasks, priority="medium")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].priority, "medium")

    def test_filter_by_low_priority(self):
        """filter_tasks(priority='low') returns only low-priority tasks."""
        result = filter_tasks(self.tasks, priority="low")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].priority, "low")

    def test_filter_no_criteria_returns_all(self):
        """filter_tasks() with no arguments returns all tasks unchanged."""
        result = filter_tasks(self.tasks)
        self.assertEqual(len(result), 3)

    def test_filter_no_matching_results(self):
        """filter_tasks() returns an empty list when nothing matches."""
        # There are no completed + high-priority tasks in the fixture.
        result = filter_tasks(self.tasks, status="completed", priority="high")
        self.assertEqual(result, [])

    def test_filter_does_not_modify_original(self):
        """filter_tasks() returns a new list and does not change the original."""
        original_length = len(self.tasks)
        filter_tasks(self.tasks, status="pending")
        self.assertEqual(len(self.tasks), original_length)

    def test_filter_empty_list_returns_empty(self):
        """filter_tasks() on an empty list returns an empty list."""
        result = filter_tasks([], status="pending")
        self.assertEqual(result, [])


# ------------------------------------------------------------------
# validate_date()
# ------------------------------------------------------------------

class TestValidateDate(unittest.TestCase):
    """Tests for validate_date() — checking YYYY-MM-DD format."""

    def test_valid_date_returns_true(self):
        """A correctly formatted date returns True."""
        self.assertTrue(validate_date("2026-09-14"))

    def test_empty_string_returns_true(self):
        """Empty string is valid — means no due date."""
        self.assertTrue(validate_date(""))

    def test_future_date_returns_true(self):
        """A date far in the future is still valid."""
        self.assertTrue(validate_date("2030-12-31"))

    def test_past_date_returns_true(self):
        """A past date is a valid date string."""
        self.assertTrue(validate_date("2020-01-01"))

    def test_wrong_separator_returns_false(self):
        """Date with slashes instead of dashes returns False."""
        self.assertFalse(validate_date("2026/09/14"))

    def test_wrong_order_returns_false(self):
        """Date in DD-MM-YYYY order returns False."""
        self.assertFalse(validate_date("14-09-2026"))

    def test_non_date_string_returns_false(self):
        """A plain text string returns False."""
        self.assertFalse(validate_date("tomorrow"))

    def test_invalid_month_returns_false(self):
        """Month 13 is invalid."""
        self.assertFalse(validate_date("2026-13-01"))

    def test_invalid_day_returns_false(self):
        """Day 32 is invalid."""
        self.assertFalse(validate_date("2026-01-32"))

    def test_partial_date_returns_false(self):
        """An incomplete date string returns False."""
        self.assertFalse(validate_date("2026-09"))


# ------------------------------------------------------------------
# get_summary()
# ------------------------------------------------------------------

class TestGetSummary(unittest.TestCase):
    """Tests for get_summary() — computing task counts."""

    def test_summary_empty_list(self):
        """get_summary([]) returns all-zero counts."""
        s = get_summary([])
        self.assertEqual(s["total"], 0)
        self.assertEqual(s["completed"], 0)
        self.assertEqual(s["pending"], 0)
        self.assertEqual(s["overdue"], 0)

    def test_summary_all_pending(self):
        """Summary with all pending tasks."""
        tasks = [
            Task(1, "A", status="pending"),
            Task(2, "B", status="pending"),
        ]
        s = get_summary(tasks)
        self.assertEqual(s["total"], 2)
        self.assertEqual(s["pending"], 2)
        self.assertEqual(s["completed"], 0)

    def test_summary_all_completed(self):
        """Summary with all completed tasks."""
        tasks = [
            Task(1, "A", status="completed"),
            Task(2, "B", status="completed"),
        ]
        s = get_summary(tasks)
        self.assertEqual(s["total"], 2)
        self.assertEqual(s["completed"], 2)
        self.assertEqual(s["pending"], 0)
        self.assertEqual(s["overdue"], 0)

    def test_summary_overdue_count(self):
        """Overdue count matches the number of past-due pending tasks."""
        past = (date.today() - timedelta(days=1)).isoformat()
        future = (date.today() + timedelta(days=1)).isoformat()
        tasks = [
            Task(1, "Overdue", due_date=past, status="pending"),
            Task(2, "Future", due_date=future, status="pending"),
            Task(3, "Done", due_date=past, status="completed"),
        ]
        s = get_summary(tasks)
        self.assertEqual(s["overdue"], 1)
        self.assertEqual(s["total"], 3)
        self.assertEqual(s["pending"], 2)
        self.assertEqual(s["completed"], 1)

    def test_summary_returns_dict(self):
        """get_summary() returns a dictionary."""
        s = get_summary([])
        self.assertIsInstance(s, dict)

    def test_summary_keys_present(self):
        """get_summary() result contains all expected keys."""
        s = get_summary([])
        self.assertIn("total", s)
        self.assertIn("completed", s)
        self.assertIn("pending", s)
        self.assertIn("overdue", s)


# ------------------------------------------------------------------
# format_task_table()
# ------------------------------------------------------------------

class TestFormatTaskTable(unittest.TestCase):
    """Tests for format_task_table() — producing display strings."""

    def test_empty_list_returns_no_tasks_message(self):
        """format_task_table([]) returns a 'no tasks' message."""
        result = format_task_table([])
        self.assertEqual(result, "No tasks found.")

    def test_table_contains_task_title(self):
        """The formatted table contains the task title."""
        tasks = [Task(1, "Important task")]
        result = format_task_table(tasks)
        self.assertIn("Important task", result)

    def test_table_contains_task_id(self):
        """The formatted table contains the task ID."""
        tasks = [Task(42, "Task with big ID")]
        result = format_task_table(tasks)
        self.assertIn("42", result)

    def test_table_contains_priority(self):
        """The formatted table contains the priority value."""
        tasks = [Task(1, "Urgent", priority="high")]
        result = format_task_table(tasks)
        self.assertIn("high", result)

    def test_table_contains_status(self):
        """The formatted table contains the status."""
        tasks = [Task(1, "Done", status="completed")]
        result = format_task_table(tasks)
        self.assertIn("completed", result)

    def test_table_marks_overdue(self):
        """Overdue tasks are labelled [OVERDUE] in the table."""
        past = (date.today() - timedelta(days=2)).isoformat()
        tasks = [Task(1, "Late task", due_date=past, status="pending")]
        result = format_task_table(tasks)
        self.assertIn("[OVERDUE]", result)

    def test_table_no_overdue_for_future_task(self):
        """Non-overdue tasks do not get the [OVERDUE] label."""
        future = (date.today() + timedelta(days=10)).isoformat()
        tasks = [Task(1, "On time", due_date=future, status="pending")]
        result = format_task_table(tasks)
        self.assertNotIn("[OVERDUE]", result)

    def test_table_shows_none_for_empty_due_date(self):
        """Tasks with no due date show 'none' in the due date column."""
        tasks = [Task(1, "No deadline", due_date="")]
        result = format_task_table(tasks)
        self.assertIn("none", result)

    def test_table_multiple_tasks(self):
        """The table includes a row for each task in the list."""
        tasks = [
            Task(1, "Alpha"),
            Task(2, "Beta"),
            Task(3, "Gamma"),
        ]
        result = format_task_table(tasks)
        self.assertIn("Alpha", result)
        self.assertIn("Beta", result)
        self.assertIn("Gamma", result)

    def test_table_returns_string(self):
        """format_task_table() always returns a string."""
        result = format_task_table([])
        self.assertIsInstance(result, str)
        result2 = format_task_table([Task(1, "Any task")])
        self.assertIsInstance(result2, str)


if __name__ == "__main__":
    unittest.main()
