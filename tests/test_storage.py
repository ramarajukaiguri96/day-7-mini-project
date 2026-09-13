"""
tests/test_storage.py — Unit tests for the storage layer

Tests cover:
  - load_tasks() when the file does not exist
  - load_tasks() when the file contains corrupted JSON
  - load_tasks() when the file is empty
  - load_tasks() with a valid file
  - save_tasks() writing correct content
  - save_tasks() creating the data directory if needed
  - save_tasks() with an empty task list
  - Round-trip: save then load returns identical tasks
"""

import json
import os
import tempfile
import unittest

from storage import load_tasks, save_tasks
from task import Task


class TestLoadTasks(unittest.TestCase):
    """Tests for load_tasks() — reading the JSON data file."""

    def test_load_returns_empty_list_when_file_missing(self):
        """load_tasks() returns [] when the file does not exist."""
        # Use a path that is guaranteed not to exist.
        result = load_tasks("/tmp/this_file_does_not_exist_xyz123.json")
        self.assertEqual(result, [])

    def test_load_returns_empty_list_for_corrupted_json(self):
        """load_tasks() returns [] and does not crash on corrupted JSON."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            f.write("this is not valid json {{{{")
            tmp_path = f.name

        try:
            result = load_tasks(tmp_path)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp_path)

    def test_load_returns_empty_list_for_empty_file(self):
        """load_tasks() returns [] for a completely empty file."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            f.write("")
            tmp_path = f.name

        try:
            result = load_tasks(tmp_path)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp_path)

    def test_load_returns_empty_list_for_missing_tasks_key(self):
        """load_tasks() handles JSON with no 'tasks' key — returns []."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump({"other_key": "value"}, f)
            tmp_path = f.name

        try:
            result = load_tasks(tmp_path)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp_path)

    def test_load_returns_task_objects(self):
        """load_tasks() returns a list of Task instances, not dicts."""
        data = {
            "tasks": [
                {
                    "task_id": 1,
                    "title": "Test task",
                    "description": "",
                    "priority": "high",
                    "due_date": "2026-09-14",
                    "status": "pending",
                    "created_at": "2026-09-13",
                }
            ]
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(data, f)
            tmp_path = f.name

        try:
            result = load_tasks(tmp_path)
            self.assertEqual(len(result), 1)
            self.assertIsInstance(result[0], Task)
        finally:
            os.unlink(tmp_path)

    def test_load_correct_field_values(self):
        """load_tasks() restores all field values correctly."""
        data = {
            "tasks": [
                {
                    "task_id": 5,
                    "title": "Buy milk",
                    "description": "Skimmed",
                    "priority": "low",
                    "due_date": "2026-10-01",
                    "status": "completed",
                    "created_at": "2026-09-01",
                }
            ]
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(data, f)
            tmp_path = f.name

        try:
            tasks = load_tasks(tmp_path)
            t = tasks[0]
            self.assertEqual(t.task_id, 5)
            self.assertEqual(t.title, "Buy milk")
            self.assertEqual(t.description, "Skimmed")
            self.assertEqual(t.priority, "low")
            self.assertEqual(t.due_date, "2026-10-01")
            self.assertEqual(t.status, "completed")
            self.assertEqual(t.created_at, "2026-09-01")
        finally:
            os.unlink(tmp_path)

    def test_load_multiple_tasks(self):
        """load_tasks() loads all tasks from a file with multiple entries."""
        data = {
            "tasks": [
                {"task_id": 1, "title": "First", "description": "",
                 "priority": "high", "due_date": "", "status": "pending",
                 "created_at": "2026-09-13"},
                {"task_id": 2, "title": "Second", "description": "",
                 "priority": "low", "due_date": "", "status": "completed",
                 "created_at": "2026-09-13"},
                {"task_id": 3, "title": "Third", "description": "",
                 "priority": "medium", "due_date": "", "status": "pending",
                 "created_at": "2026-09-13"},
            ]
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(data, f)
            tmp_path = f.name

        try:
            tasks = load_tasks(tmp_path)
            self.assertEqual(len(tasks), 3)
            self.assertEqual(tasks[0].title, "First")
            self.assertEqual(tasks[2].title, "Third")
        finally:
            os.unlink(tmp_path)

    def test_load_empty_tasks_array(self):
        """load_tasks() returns [] for a file with an empty tasks array."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump({"tasks": []}, f)
            tmp_path = f.name

        try:
            result = load_tasks(tmp_path)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp_path)


class TestSaveTasks(unittest.TestCase):
    """Tests for save_tasks() — writing the JSON data file."""

    def test_save_creates_file(self):
        """save_tasks() creates the file if it does not exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            self.assertFalse(os.path.exists(filepath))
            save_tasks([], filepath)
            self.assertTrue(os.path.exists(filepath))

    def test_save_empty_list_writes_valid_json(self):
        """save_tasks([]) writes a valid JSON file with an empty tasks array."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            save_tasks([], filepath)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIn("tasks", data)
            self.assertEqual(data["tasks"], [])

    def test_save_writes_correct_task_data(self):
        """save_tasks() writes the correct field values for each task."""
        tasks = [
            Task(1, "Test task", "A description", "high", "2026-09-14",
                 "pending", "2026-09-13")
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            save_tasks(tasks, filepath)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            saved = data["tasks"][0]
            self.assertEqual(saved["task_id"], 1)
            self.assertEqual(saved["title"], "Test task")
            self.assertEqual(saved["priority"], "high")

    def test_save_creates_directory_if_missing(self):
        """save_tasks() creates the directory automatically if it does not exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Use a nested directory that does not yet exist.
            filepath = os.path.join(tmp_dir, "subdir", "tasks.json")
            self.assertFalse(os.path.exists(os.path.dirname(filepath)))
            save_tasks([], filepath)
            self.assertTrue(os.path.exists(filepath))

    def test_save_multiple_tasks(self):
        """save_tasks() correctly writes multiple tasks."""
        tasks = [
            Task(1, "First", priority="high"),
            Task(2, "Second", priority="low"),
            Task(3, "Third", priority="medium"),
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            save_tasks(tasks, filepath)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(len(data["tasks"]), 3)
            self.assertEqual(data["tasks"][1]["title"], "Second")


class TestRoundTrip(unittest.TestCase):
    """Round-trip tests: save a list of tasks then load it back."""

    def test_round_trip_preserves_all_fields(self):
        """Saving and reloading a task list produces identical Task objects."""
        original_tasks = [
            Task(1, "Task one", "Desc one", "high", "2026-09-14", "pending", "2026-09-13"),
            Task(2, "Task two", "", "low", "", "completed", "2026-09-12"),
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            save_tasks(original_tasks, filepath)
            loaded_tasks = load_tasks(filepath)

        self.assertEqual(len(loaded_tasks), 2)

        for original, loaded in zip(original_tasks, loaded_tasks):
            self.assertEqual(original.task_id, loaded.task_id)
            self.assertEqual(original.title, loaded.title)
            self.assertEqual(original.description, loaded.description)
            self.assertEqual(original.priority, loaded.priority)
            self.assertEqual(original.due_date, loaded.due_date)
            self.assertEqual(original.status, loaded.status)
            self.assertEqual(original.created_at, loaded.created_at)

    def test_round_trip_empty_list(self):
        """Saving and reloading an empty list returns an empty list."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")
            save_tasks([], filepath)
            result = load_tasks(filepath)
        self.assertEqual(result, [])

    def test_save_overwrites_previous_content(self):
        """A second save_tasks() call replaces the previous file contents."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "tasks.json")

            # First save: 2 tasks
            tasks_v1 = [Task(1, "Old task one"), Task(2, "Old task two")]
            save_tasks(tasks_v1, filepath)

            # Second save: 1 different task
            tasks_v2 = [Task(1, "New task")]
            save_tasks(tasks_v2, filepath)

            loaded = load_tasks(filepath)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0].title, "New task")


if __name__ == "__main__":
    unittest.main()
