"""
storage.py — JSON persistence layer

This module handles all reading from and writing to the data file
(data/tasks.json). The rest of the application never touches the file
directly — it always goes through these two functions.

Keeping file I/O in one place makes it easy to:
  - Change the file path without touching the rest of the code.
  - Handle all file-related errors in one place.
  - Test the load/save logic independently.
"""

import json
import os

from task import Task

# The path to the JSON data file.
# Using a constant here means if we ever need to change the location,
# we only need to update it in one place.
DATA_FILE = os.path.join("data", "tasks.json")


def load_tasks(filepath: str = DATA_FILE) -> list:
    """
    Load all tasks from the JSON file and return them as a list of Task objects.

    This function is called once when the application starts. It reads the
    JSON file, converts each dictionary entry back into a Task object, and
    returns the full list.

    Three failure cases are handled gracefully (without crashing):
      - FileNotFoundError: the file doesn't exist yet (first run). Return [].
      - json.JSONDecodeError: the file is corrupted or empty. Warn and return [].
      - KeyError: a task dict is missing expected fields. Skip that task.

    Parameters:
        filepath (str): Path to the JSON file. Defaults to DATA_FILE.

    Returns:
        list[Task]: A list of Task objects. Empty list if file is missing
                    or unreadable.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # The JSON file stores tasks under the key "tasks".
        # We use .get() with a default of [] so a file missing the key
        # doesn't crash — it just returns an empty list.
        raw_tasks = data.get("tasks", [])

        # Convert each plain dictionary back into a Task object.
        tasks = []
        for item in raw_tasks:
            try:
                tasks.append(Task.from_dict(item))
            except KeyError as e:
                # If a single task entry is malformed, skip it and warn.
                # We do not want one bad entry to prevent loading the rest.
                print(f"⚠️  Warning: skipping malformed task entry (missing field: {e})")

        return tasks

    except FileNotFoundError:
        # No data file yet — this is normal on the very first run.
        # Return an empty list; the file will be created on the first save.
        return []

    except json.JSONDecodeError:
        # The file exists but its contents are not valid JSON.
        # This can happen if the file was manually edited incorrectly,
        # or if a previous save was interrupted. Warn the user and start fresh.
        print("⚠️  Warning: data/tasks.json is corrupted. Starting with an empty task list.")
        return []


def save_tasks(tasks: list, filepath: str = DATA_FILE) -> None:
    """
    Save the current list of Task objects to the JSON file.

    This function is called every time a task is added, completed, or deleted.
    It converts all Task objects to plain dictionaries and writes the full list
    to disk. Any existing file contents are overwritten.

    The data/ directory is created automatically if it does not exist.
    This means the application works even if someone deleted the data/ folder.

    Parameters:
        tasks (list[Task]): The full list of tasks to save.
        filepath (str): Path to the JSON file. Defaults to DATA_FILE.

    Errors handled:
        - OSError: filesystem-level error (e.g. disk full, bad path).
        - PermissionError: no write access to the file or directory.
    """
    # Ensure the data/ directory exists before trying to write to it.
    # exist_ok=True means this does nothing if the directory already exists.
    directory = os.path.dirname(filepath)
    if directory:
        os.makedirs(directory, exist_ok=True)

    try:
        # Convert each Task object to a plain dict before writing.
        # json.dump() cannot serialise custom objects directly.
        data = {"tasks": [task.to_dict() for task in tasks]}

        # indent=2 makes the JSON file human-readable when opened in a text editor.
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    except PermissionError:
        # The OS refused to write — e.g. read-only filesystem or wrong permissions.
        print(f"❌ Error: Permission denied when saving to {filepath}.")
        print("   Check that you have write access to the data/ directory.")

    except OSError as e:
        # Catch other filesystem errors (disk full, bad path, etc.).
        print(f"❌ Error: Could not save tasks — {e}")
