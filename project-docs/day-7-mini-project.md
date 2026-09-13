CanvasListFolder
infinitra-build-sep2026
@Yogananda Karra created this channel on 7 September. This is the very beginning of the infinitra-build-sep2026 channel.
  10:24 PM
joined infinitra-build-sep2026. Also, and 7 others joined via invitation.
  10:41 PM
Welcome to Infinitra Build - Sep 2026 Cohort!
10:42
TODAY — Day 1: Development Environment Setup
Duration: ~6 hours · Goal: All tools installed and verified
****************************************************************************************************************************************
By end of today you'll have:
 - VS Code installed + configured for Python
 - Comfort with basic terminal commands
 - Git installed + configured with your identity
 - GitHub account with SSH key connected
 - Kiro IDE installed and signed in
 - Python 3.13 installed and verified
 - Your first Git commit pushed to GitHub
********************************************************************
Steps:
   │ 1. Terminal basics — practice pwd, ls, cd, mkdir, touch, cat, echo, clear. Create ~/projects/infinitra-build.
****************************************************************************************************************************************
   │ 2. Install VS Code
   │ • Native Ubuntu / download: code.visualstudio.com/download

   │ • Mac: brew install --cask visual-studio-code
   │ • Extensions (all): Python, Pylance, GitLens
   │ • Verify: code --version
****************************************************************************************************************************************
   │ 3. Install Python 3.13
   │ • Ubuntu/WSL2 (not in default repos — use deadsnakes):
   │   > sudo apt update
   > sudo apt install software-properties-common -y
   > sudo add-apt-repository ppa:deadsnakes/ppa -y
   > sudo apt update
   > sudo apt install python3.13 python3.13-venv python3.13-dev -y
   >   │ • Mac: brew install python@3.13
   │ • Verify: python3.13 --version · Test: python3 -c "print('Hello, Infinitra!')"
****************************************************************************************************************************************
   │ 4. Install & configure Git
   │ • Ubuntu: sudo apt install git -y
   │ • Mac: brew install git
   │ • Then set your identity:
   │   > git config --global user.name "Your Full Name"
   > git config --global user.email "your.email@example.com"
   > git config --global init.defaultBranch main
   > git config --global core.editor "code --wait"
   >   │ • Verify: git --version
****************************************************************************************************************************************
   │ 5. GitHub + SSH
   │ • Create account at github.com/signup

   │ • ssh-keygen -t ed25519 -C "your.email@example.com"
   │ • Copy key: cat ~/.ssh/id_ed25519.pub → add at github.com/settings/keys

   │ • Test: ssh -T git@github.com
   │ • Install GitHub CLI — Ubuntu: sudo apt install gh -y · Mac: brew install gh
   │ • Then: gh auth login (GitHub.com → SSH → login via browser)
****************************************************************************************************************************************
   │ 6. Install Kiro CLI (same on both OS)
   │ curl -fsSL kiro.dev/install.sh
| bash
   │ If needed: echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
   │ Sign in: kiro (free tier) · Test: kiro "What is 2 + 2?"
****************************************************************************************************************************************
   │ 7. Install Cursor Agent CLI (same on both OS)
   │ curl cursor.com/install
-fsS | bash
   │ Add to PATH if needed (same line as above). Sign in: agent · Test: agent "What is 2 + 2?"
****************************************************************************************************************************************
   │ 8. Your first commit
   │   > git init
   > echo 'print("Hello from Day 1!")' > hello.py
   > python3 hello.py
   > git add hello.py
   > git commit -m "Add hello.py - my first commit"
   > gh repo create day-1-hello --public --source=. --push
   >
****************************************************************************************************************************************
   │ :white_tick: Exit check — all must return a version number:
   │ code --version · python3 --version · git --version · gh --version · kiro --version · agent --version
   │ Plus: SSH key connected · first commit pushed · confident with cd/ls/mkdir/pwd.
****************************************************************************************************************************************
   │ Resources: code.visualstudio.com/docs · git-scm.com (first-time setup) · GitHub SSH docs · kiro.dev/docs ·  docs.cursor.com/en/cli · python.org/downloads (edited) 
  10:49 PM
:snake: Day 2 — Python Fundamentals
Duration: ~6 hours · Deliverable: 10 practice problems solved and committed to GitHub
****************************************************************************************************************************************
   │ By end of today you'll be able to:
   │ - Create variables and use Python's core data types
   │ - Get user input and convert types
   │ - Write conditional logic (if/elif/else)
   │ - Use for and while loops
   │ - Define and call functions with parameters and return values
****************************************************************************************************************************************
   │ Topics to work through: print() · variables & f-strings · data types (int, float, str, bool, None) · input() + type
   conversion · operators (arithmetic, comparison, logical) · conditionals · for/while loops, break/continue · functions
   (parameters, return, defaults, docstrings)
****************************************************************************************************************************************
   │ :memo: Practice Problems (solve all 10, commit after each):
   │ 1. Hello World — print "Hello, World!" then your name
   │ 2. Personal Info — name/age/height variables printed with an f-string
   │ 3. Simple Calculator — read two numbers, print sum/difference/product/quotient
   │ 4. Even or Odd — read a number, say if it's even or odd (use %)
   │ 5. Grade Classifier — read score 0–100, print letter grade A–F
   │ 6. Countdown — countdown from user's number to 1, then "Liftoff!" (while loop)
   │ 7. Sum of Numbers — sum 1 to 100 with a for loop (answer: 5050)
   │ 8. FizzBuzz — 1 to 30, Fizz/Buzz/FizzBuzz rules
   │ 9. Temperature Converter — two functions, C:left_right_arrow:F, test 0°C/100°C/32°F/212°F
   │ 10. Word Frequency Counter — count_words(sentence) returns a dict of word→count
****************************************************************************************************************************************
   │ :white_tick: Exit check:
   │ - All 10 problems running correctly
   │ - Committed: git add . && git commit -m "Solve Day 2 problems"
   │ - Can explain: difference between = and ==; what range(1, 6) produces; what a function returns
****************************************************************************************************************************************
   │ Resources: docs.python.org/3.13/tutorial · Control Flow chapter · PEP 8 · pythontutor.com (visualizer) ·
   realpython.com
  2:44 PM
Practice ProblemsCreate a file for each problem (or one file with all solutions). Commit after each problem.Problem 1: Hello World (5 min)Print "Hello, World!" to the screen. Then print your name on a separate line.
Expected output:

Hello, World!
Alice

Problem 2: Personal Info (5 min)Create variables for your name (str), age (int), and height in meters (float). Print them using an f-string.
Expected output:

My name is Alice, I am 25 years old, and 1.65 meters tall.

Problem 3: Simple Calculator (7 min)Ask the user for two numbers. Print their sum, difference, product, and quotient.
Expected output (if user enters 10 and 3):

Sum: 13.0
Difference: 7.0
Product: 30.0
Quotient: 3.3333333333333335

Problem 4: Even or Odd (7 min)Ask the user for a number. Print whether it is even or odd.
Hint: Use the modulo operator %. A number is even if number % 2 == 0.
Expected output (if user enters 7):

7 is odd

Problem 5: Grade Classifier (10 min)Ask the user for a test score (0–100). Print the letter grade:

    90–100: A
    80–89: B
    70–79: C
    60–69: D
    Below 60: F

Expected output (if user enters 85):

Your grade is: B

Problem 6: Countdown (10 min)Ask the user for a starting number. Print a countdown from that number to 1, then print "Liftoff!" Use a while loop.
Expected output (if user enters 5):

5
4
3
2
1
Liftoff!

Problem 7: Sum of Numbers (10 min)Use a for loop to calculate and print the sum of all numbers from 1 to 100.
Expected output:

The sum of 1 to 100 is: 5050

Problem 8: FizzBuzz (15 min)Print numbers from 1 to 30. But:

    For multiples of 3, print "Fizz" instead
    For multiples of 5, print "Buzz" instead
    For multiples of both 3 and 5, print "FizzBuzz"

Expected output (first 15 lines):

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

Hint: Check "both" first (multiples of 15), then 3, then 5, then the number itself.Problem 9: Temperature Converter (15 min)Write two functions:

    celsius_to_fahrenheit(celsius)— returns the Fahrenheit value
    fahrenheit_to_celsius(fahrenheit)— returns the Celsius value

Formula: F = C × 9/5 + 32
Test with: 0°C, 100°C, 32°F, 212°F
Expected output:

0°C = 32.0°F
100°C = 212.0°F
32°F = 0.0°C
212°F = 100.0°C

Problem 10: Word Frequency Counter (20 min)Write a function count_words(sentence) that takes a string and returns a dictionary with each word as a key and its count as the value. Convert to lowercase first.
Test with: "The cat sat on the mat and the cat sat"
Expected output:

{'the': 3, 'cat': 2, 'sat': 2, 'on': 1, 'mat': 1, 'and': 1}

Hint: Use .lower() and .split() on the string. Loop through words and build a dictionary.
  6:02 PM
PDF 
PythonProject.pdf
PDF
  8:53 AM
day-3-data-structures.md 
day-3-data-structures.md
Markdown
Day 3: Data Structures, File I/O & JSON

    Week 1 · Duration: 6 hours
    Deliverable: CLI expense tracker (working, committed to GitHub)

Instructor Notes
Structure
Block 	Duration 	Activity
Lecture + live coding 	2 hrs 	Lists, dicts, tuples/sets, file I/O, JSON, error handling
Guided exercise 	1 hr 	Build expense tracker together (core structure)
Independent practice 	2.5 hrs 	Complete expense tracker features
Wrap-up 	30 min 	Demo solutions, common issues
Lecture Outline

    Lists (30 min) — creation, indexing, slicing, methods, comprehensions
    Dictionaries (30 min) — creation, access, methods, iteration, comprehensions
    Tuples & Sets (15 min) — when to use each
    File I/O (20 min) — open(), with statement, read/write, encoding
    JSON (15 min) — json.load/dump, why it matters
    Error Handling (30 min) — try/except/else/finally, common exceptions

Teaching Tips

    Show lists and dicts side by side: “lists are ordered by position, dicts are accessed by name”
    Demo file I/O with a real file — create it, write to it, read it back
    For error handling, deliberately cause errors first (FileNotFoundError, ValueError) then show how to catch them
    The expense tracker project ties everything together — start it as a guided exercise, then let students finish independently

Student Material
Today’s Objectives

By the end of today, you will:

    [ ] Use lists (create, index, slice, methods, comprehensions)
    [ ] Use dictionaries (create, access, iterate, comprehensions)
    [ ] Read and write files using with open()
    [ ] Load and save JSON data
    [ ] Handle errors gracefully with try/except
    [ ] Build a working CLI expense tracker

Lists

Lists are ordered, mutable collections. Use them when you have a sequence of items.

# Create
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
empty = []

# Index (0-based, negative from end)
fruits[0]    # "apple"
fruits[-1]   # "cherry"

# Slice [start:stop:step] — stop is exclusive
numbers[1:4]    # [2, 3, 4]
numbers[:3]     # [1, 2, 3]
numbers[::2]    # [1, 3, 5]
numbers[::-1]   # [5, 4, 3, 2, 1] — reversed

Key Methods

fruits = ["apple", "banana"]

fruits.append("cherry")        # Add to end → ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")  # Insert at index
fruits.remove("banana")        # Remove first occurrence
last = fruits.pop()            # Remove & return last item
fruits.sort()                  # Sort in place (returns None)
fruits.reverse()               # Reverse in place

len(fruits)                    # Length
"apple" in fruits              # Membership test → True
fruits.index("apple")          # Find index → 0
fruits.count("apple")          # Count occurrences → 1

List Comprehensions

# [expression for item in iterable if condition]
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

names = ["alice", "bob", "charlie"]
upper = [name.upper() for name in names]
# ["ALICE", "BOB", "CHARLIE"]

Useful Patterns

# enumerate — get index + value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip — iterate two lists in parallel
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Check if empty
if not my_list:
    print("List is empty")

Dictionaries

Dictionaries store key-value pairs. Use them when you need to look up values by name.

# Create
person = {"name": "Alice", "age": 30, "city": "Kurnool"}

# Access
person["name"]              # "Alice" — KeyError if missing
person.get("name")          # "Alice" — None if missing
person.get("phone", "N/A") # "N/A" — custom default

# Add / Update
person["email"] = "alice@example.com"
person["age"] = 31

# Delete
del person["city"]
phone = person.pop("phone", None)  # Remove & return (no error if missing)

Key Methods

person.keys()    # dict_keys(["name", "age", ...])
person.values()  # dict_values(["Alice", 30, ...])
person.items()   # dict_items([("name", "Alice"), ("age", 30), ...])
person.update({"age": 32, "country": "India"})  # Merge

Iterating

# Over keys (default)
for key in person:
    print(key)

# Over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

Dict Comprehensions

squares = {x: x ** 2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

Nested Dicts

students = {
    "alice": {"grade": "A", "gpa": 3.9},
    "bob": {"grade": "B", "gpa": 3.2},
}
students["alice"]["gpa"]  # 3.9

Tuples & Sets (Brief)

Tuples — immutable ordered sequences:

point = (3, 4)
x, y = point  # Unpacking

# Use for: fixed data, function return values, dict keys
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 4, 1, 5])  # lo=1, hi=5

Sets — unordered, unique elements:

colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("red")

# Remove duplicates from a list
unique = list(set([1, 2, 2, 3, 3, 3]))  # [1, 2, 3]

# Fast membership test (O(1) vs O(n) for lists)
"red" in colors  # True

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
a | b  # Union: {1, 2, 3, 4}
a & b  # Intersection: {2, 3}
a - b  # Difference: {1}

File I/O
Reading Files

# Always use 'with' — guarantees the file is closed
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()  # Entire file as one string

# Read line by line (memory efficient)
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # strip() removes trailing newline

Writing Files

# Write (creates or overwrites)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Append (adds to end)
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Line 3\n")

File Modes
Mode 	Description
"r" 	Read (default). File must exist.
"w" 	Write. Creates or overwrites.
"a" 	Append. Creates if doesn’t exist.
"x" 	Create. Fails if file already exists.

⚠️ Always specify encoding="utf-8" — the default is platform-dependent.

    Source: https://docs.python.org/3.13/tutorial/inputoutput.html#reading-and-writing-files

JSON

JSON (JavaScript Object Notation) is the standard format for data exchange. APIs return JSON. Config files use JSON. It maps directly to Python dicts and lists.

import json

# Python → JSON string
data = {"name": "Alice", "scores": [95, 87, 92]}
json_string = json.dumps(data, indent=2)
print(json_string)

# JSON string → Python
parsed = json.loads('{"name": "Bob", "age": 25}')
print(parsed["name"])  # "Bob"

Reading/Writing JSON Files

import json

# Save to file
expenses = [{"category": "food", "amount": 25.50}]
with open("expenses.json", "w", encoding="utf-8") as f:
    json.dump(expenses, f, indent=2)

# Load from file
with open("expenses.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

Type Mapping
Python 	JSON
dict 	object {}
list 	array []
str 	string
int/float 	number
True/False 	true/false
None 	null

    Source: https://docs.python.org/3.13/library/json.html

Error Handling

Programs crash when unexpected things happen. Error handling lets you respond gracefully instead of showing a traceback.

try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Runs only if NO exception occurred
    print(f"Result: {result}")
finally:
    # ALWAYS runs (cleanup)
    print("Done.")

Common Exceptions
Exception 	When
ValueError 	Wrong value: int("abc")
TypeError 	Wrong type: "a" + 1
KeyError 	Dict key missing: d["nope"]
IndexError 	List index out of range
FileNotFoundError 	File doesn’t exist
ZeroDivisionError 	Division by zero
json.JSONDecodeError 	Invalid JSON
Practical Pattern

import json

def load_data(filepath):
    """Load JSON data from file. Return empty list if file missing or corrupt."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Data file corrupted. Starting fresh.")
        return []

    Source: https://docs.python.org/3.13/tutorial/errors.html

Project: CLI Expense Tracker

Build a command-line expense tracker that stores data in a JSON file.
Features

    Add expense — category, amount, description
    List all expenses — formatted table
    Filter by category — show only matching
    Summary — total + breakdown by category
    Persistent storage — saves to expenses.json

Acceptance Criteria

    [ ] Running with no existing JSON file creates one automatically
    [ ] Adding an expense saves it immediately
    [ ] Invalid amount (non-numeric, negative) shows error without crashing
    [ ] Empty list shows “No expenses recorded”
    [ ] Summary shows total and per-category totals
    [ ] All amounts display with 2 decimal places

Data Structure (expenses.json)

{
  "expenses": [
    {
      "id": 1,
      "category": "food",
      "amount": 25.50,
      "description": "Lunch at cafe",
      "date": "2026-05-22"
    }
  ]
}

Starter Code

"""CLI Expense Tracker — Day 3 Project"""
import json
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from JSON file. Return empty list if file doesn't exist."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("expenses", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Data file corrupted. Starting fresh.")
        return []


def save_expenses(expenses):
    """Save expenses list to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"expenses": expenses}, f, indent=2)


def get_next_id(expenses):
    """Return the next available ID."""
    if not expenses:
        return 1
    return max(exp["id"] for exp in expenses) + 1


def add_expense(expenses):
    """Prompt user for expense details and add to list."""
    category = input("Category: ").strip().lower()
    if not category:
        print("Error: Category cannot be empty.")
        return

    amount_str = input("Amount: ").strip()
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be positive")
    except ValueError as e:
        print(f"Error: Invalid amount — {e}")
        return

    description = input("Description: ").strip()

    expense = {
        "id": get_next_id(expenses),
        "category": category,
        "amount": round(amount, 2),
        "description": description,
        "date": str(date.today()),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Expense added (ID: {expense['id']})")


def list_expenses(expenses):
    """Display all expenses in a formatted table."""
    if not expenses:
        print("No expenses recorded.")
        return

    print(f"\n{'ID':<4} {'Date':<12} {'Category':<12} {'Amount':>8} {'Description'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp['id']:<4} {exp['date']:<12} {exp['category']:<12} "
              f"${exp['amount']:>7.2f} {exp['description']}")


def filter_by_category(expenses):
    """Show expenses for a specific category."""
    category = input("Filter category: ").strip().lower()
    filtered = [e for e in expenses if e["category"] == category]
    if not filtered:
        print(f"No expenses found for category: {category}")
        return
    list_expenses(filtered)


def show_summary(expenses):
    """Show total and per-category breakdown."""
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(exp["amount"] for exp in expenses)
    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]

    print(f"\nTotal: ${total:.2f}")
    print("\nBy category:")
    for cat, amount in sorted(categories.items()):
        print(f"  {cat:<15} ${amount:.2f}")


def main():
    """Main program loop."""
    expenses = load_expenses()

    menu = """
--- Expense Tracker ---
1. Add expense
2. List all expenses
3. Filter by category
4. Summary
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose (1-5): ").strip()

        match choice:
            case "1":
                add_expense(expenses)
            case "2":
                list_expenses(expenses)
            case "3":
                filter_by_category(expenses)
            case "4":
                show_summary(expenses)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Enter 1-5.")


if __name__ == "__main__":
    main()

How to Run

python3 expense_tracker.py

Commit Your Work

git add expense_tracker.py
git commit -m "Add CLI expense tracker with JSON persistence"

Exit Check

    [ ] Expense tracker runs without errors
    [ ] Can add, list, filter, and summarize expenses
    [ ] Data persists between runs (saved in JSON file)
    [ ] Invalid input doesn’t crash the program
    [ ] Code committed to GitHub

Resources
Resource 	URL
Data Structures Tutorial 	https://docs.python.org/3.13/tutorial/datastructures.html
File I/O 	https://docs.python.org/3.13/tutorial/inputoutput.html#reading-and-writing-files
json module 	https://docs.python.org/3.13/library/json.html
Errors and Exceptions 	https://docs.python.org/3.13/tutorial/errors.html
Built-in Exceptions 	https://docs.python.org/3.13/library/exceptions.html

Infinitra Build · Week 1 · Day 3
  8:27 AM
day-4-lecture.md 
day-4-lecture.md
Markdown
Day 4 Lecture: Git Workflow & AI Coding Tools

    Duration: 2.5 hours (1.5h Git + 1h AI Tools)
    Context: Week 1, Day 4 - Collaboration and AI-assisted development
    Audience: Students with basic Git knowledge from Day 1
    Format: Live demos with collaborative exercises

Pre-Lecture Setup (5 minutes)
Instructor Preparation

    Have VS Code open with a demo repository
    Terminal open beside VS Code
    Create instructor GitHub organization beforehand
    Set up shared repository: bootcamp-day4-collab
    Students should have completed their expense tracker from Day 3

Opening Statement

    “Yesterday you built software that works. Today you learn how software teams work together. Git isn’t just for backup - it’s how developers coordinate without stepping on each other’s code. And AI tools aren’t magic - they’re powerful assistants that amplify your skills when used correctly.”

Part 1: Git Deep Dive (1.5 hours)
Section 1: Mental Model - The Three Areas (15 minutes)
The Problem Git Solves (3 minutes)

Without Version Control:

my_project/
├── app.py
├── app_backup.py
├── app_working.py
├── app_final.py
├── app_final_final.py
└── app_actually_final.py

The Chaos:

    Which version is actually the latest?
    What changed between versions?
    How do you merge two people’s changes?
    How do you go back when things break?

Git’s Three Areas (8 minutes)

Live Demo Setup:

# Create a demo repository
mkdir git-demo
cd git-demo
git init

The Visual Model:

┌─────────────────┐     git add     ┌───────────────┐    git commit    ┌────────────┐
│ Working         │ ──────────────► │ Staging Area  │ ──────────────► │ Repository │
│ Directory       │                 │ (Index)       │                 │ (.git)     │
│                 │                 │               │                 │            │
│ Your files as   │                 │ What you've   │                 │ Permanent  │
│ they exist now  │                 │ chosen for    │                 │ history of │
│                 │                 │ next commit   │                 │ snapshots  │
└─────────────────┘                 └───────────────┘                 └────────────┘

Live Demo:

# Working Directory - create a file
echo "Hello World" > hello.txt
git status  # Untracked file

# Staging Area - prepare for commit
git add hello.txt
git status  # Changes to be committed

# Repository - save permanently
git commit -m "Add hello.txt"
git status  # Working tree clean

Key Teaching Points:

    Working Directory: What you see in your file explorer
    Staging Area: Your “shopping cart” for the next commit
    Repository: The permanent, versioned history
    git status is your best friend - run it constantly

File States Deep Dive (4 minutes)

# Demo the four file states
echo "Modified content" >> hello.txt
git status  # Modified (red)

git add hello.txt
git status  # Staged (green)

git commit -m "Update hello.txt"
git status  # Committed (clean)

# Untracked
echo "New content" > new.txt
git status  # Untracked (red)

Interactive Moment: “Before I run git status, what do you think it will show?”
Section 2: Branching - Parallel Development (20 minutes)
Why Branches Matter (5 minutes)

The Problem:

# Without branches - working directly on main
git log --oneline
# a1b2c3d Fix critical bug
# d4e5f6g Add new feature (BROKEN!)
# g7h8i9j Working code

What if the new feature breaks everything?

    Main branch is broken
    Can’t deploy the bug fix
    Have to revert or fix forward
    Team is blocked

The Solution - Branches:

main ──────●──────●──────●──────●────── (always stable)
            \              \
feature      ●────●────●───/ 

Branching Commands (8 minutes)

# See current branch and all branches
git branch
# * main  (asterisk shows current)

# Create and switch to new branch (modern syntax)
git switch -c feature/greeting

# Verify we're on the new branch
git branch
# main
# * feature/greeting

# Do some work
echo 'def greet(name): return f"Hello, {name}!"' > greeting.py
git add greeting.py
git commit -m "Add greeting function"

# Switch back to main
git switch main
ls  # greeting.py doesn't exist here!

# Switch back to feature branch
git switch feature/greeting
ls  # greeting.py exists here!

Key Teaching Points:

    Branches are lightweight - just pointers to commits
    Each branch has its own working directory state
    git switch -c creates and switches in one command
    Old syntax: git checkout -b (still works, but switch is clearer)

Branch Naming Conventions (2 minutes)

# Good branch names
git switch -c feature/user-authentication
git switch -c fix/calculator-division-bug  
git switch -c docs/update-installation-guide
git switch -c refactor/extract-database-layer

# Bad branch names
git switch -c my-work
git switch -c temp
git switch -c asdf
git switch -c john-branch

Pattern: type/brief-description

    feature/ - new functionality
    fix/ - bug fixes
    docs/ - documentation changes
    refactor/ - code cleanup
    test/ - adding tests

The Feature Branch Workflow (5 minutes)

Live Demo - Complete Workflow:

# 1. Always start from updated main
git switch main
git pull origin main  # Get latest changes

# 2. Create feature branch
git switch -c feature/add-calculator

# 3. Do your work
cat > calculator.py << EOF
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
EOF

# 4. Stage and commit
git add calculator.py
git commit -m "Add basic calculator functions"

# 5. Push to GitHub (creates remote branch)
git push -u origin feature/add-calculator

# 6. Create Pull Request (next section)
# 7. After merge, cleanup (next section)

Section 3: Merging & Conflicts (15 minutes)
Simple Merge (5 minutes)

# Merge feature branch into main
git switch main
git merge feature/add-calculator

# Check the result
git log --oneline
ls  # calculator.py now exists on main

# Clean up
git branch -d feature/add-calculator  # Delete local branch

Key Teaching Points:

    Fast-forward merge: When main hasn’t changed since branch creation
    Merge commit: When both branches have new commits
    Always merge into main, not the other way around

Merge Conflicts Demo (10 minutes)

Setup Conflict Scenario:

# Create two conflicting branches
git switch main
echo "Original content" > conflict.txt
git add conflict.txt
git commit -m "Add original content"

# Branch A
git switch -c branch-a
echo "Content from Branch A" > conflict.txt
git add conflict.txt
git commit -m "Update from branch A"

# Branch B  
git switch main
git switch -c branch-b
echo "Content from Branch B" > conflict.txt
git add conflict.txt
git commit -m "Update from branch B"

# Try to merge - CONFLICT!
git switch main
git merge branch-a  # This works fine
git merge branch-b  # CONFLICT!

Show the Conflict:

git status
# both modified: conflict.txt

cat conflict.txt
# <<<<<<< HEAD
# Content from Branch A
# =======
# Content from Branch B
# >>>>>>> branch-b

Resolve the Conflict:

# Edit the file to resolve
echo "Content from both branches combined" > conflict.txt

# Mark as resolved
git add conflict.txt

# Complete the merge
git commit -m "Merge branch-b, resolve conflict"

# Verify
git log --oneline --graph

Key Teaching Points:

    Conflicts happen when same lines are modified
    Git can’t decide which version to keep
    Conflict markers: <<<<<<<, =======, >>>>>>>
    Resolution steps: Edit → Add → Commit
    Use VS Code’s conflict resolution UI (show briefly)

Section 4: Pull Requests (20 minutes)
What Are Pull Requests? (5 minutes)

Conceptual Explanation:

    “A Pull Request (PR) is a request to merge your branch into main. It’s called a ‘request’ because someone else reviews your code first. This catches bugs, shares knowledge, and maintains code quality.”

Benefits:

    Code Review: Fresh eyes catch mistakes
    Knowledge Sharing: Team learns from each other
    Documentation: Discussion about why changes were made
    Quality Gates: Automated tests run before merge
    History: Clear record of what changed and why

Creating PRs with GitHub CLI (8 minutes)

Setup Demo Repository:

# Create a new feature
git switch -c feature/add-subtract-function
echo 'def subtract(a, b): return a - b' >> calculator.py
git add calculator.py
git commit -m "Add subtract function"
git push -u origin feature/add-subtract-function

Create PR via CLI:

# Interactive creation (recommended for beginners)
gh pr create
# ? Title: Add subtract function to calculator
# ? Body: Adds subtraction capability to calculator module
# ? What's next? Submit

# Or one-liner
gh pr create --title "Add subtract function" --body "Adds subtraction capability to calculator module"

Show PR on GitHub Web:

    Navigate to the PR URL
    Show Files Changed tab
    Show Conversation tab
    Demonstrate line comments

PR Review Process (7 minutes)

Reviewer Commands:

# List open PRs
gh pr list

# View PR details
gh pr view 1

# Check out PR locally for testing
gh pr checkout 1

# Test the changes
python calculator.py

# Leave review via CLI or web
gh pr review 1 --approve --body "LGTM! Code works as expected."

Web Review Demo:

    Go to PR → Files changed
    Click line numbers to add comments
    Click “Review changes” → Approve/Request changes
    Submit review

Key Teaching Points:

    Test changes locally before approving
    Focus on functionality, not style (for now)
    Be constructive: “Consider using…” not “This is wrong”
    LGTM = “Looks Good To Me” (common approval phrase)

Section 5: Best Practices (10 minutes)
Commit Message Quality (4 minutes)

Bad Commit Messages:

git log --oneline
# 1a2b3c4 update
# 5d6e7f8 fix
# 9g0h1i2 changes
# 3j4k5l6 asdf
# 7m8n9o0 final version

Good Commit Messages:

git log --oneline  
# a1b2c3d Add subtract function to calculator module
# d4e5f6g Fix division by zero error in calculator
# g7h8i9j Update README with installation instructions
# j0k1l2m Refactor calculator functions into separate class
# m3n4o5p Add unit tests for calculator operations

The Formula:

[verb] [what you did] [where/context]

Examples:
Add user authentication to login page
Fix memory leak in file processing
Update Docker configuration for production
Remove deprecated API endpoints
Refactor database queries for performance

What NOT to Commit (3 minutes)

Create .gitignore Demo:

# Create files that shouldn't be committed
echo "secret_key = 'abc123'" > .env
echo "cache data" > cache.tmp
mkdir __pycache__
touch __pycache__/app.pyc

# Show what Git wants to track
git status  # All these files appear!

# Create .gitignore
cat > .gitignore << EOF
# Environment variables
.env
*.env

# Python cache
__pycache__/
*.pyc
*.pyo

# Temporary files
*.tmp
*.log

# IDE files
.vscode/settings.json
.idea/
EOF

git status  # Files disappear!

Never Commit:

    Secrets: API keys, passwords, database URLs
    Generated files: Compiled code, build artifacts
    Personal settings: IDE configurations, OS files
    Large files: Videos, datasets (use Git LFS)
    Dependencies: node_modules/, venv/ (use requirements.txt)

Small, Focused Commits (3 minutes)

Bad - Everything at Once:

git add .
git commit -m "Add login, fix bugs, update docs, refactor utils"

Good - Logical Chunks:

git add login.py
git commit -m "Add user login functionality"

git add utils.py  
git commit -m "Refactor string utilities for better performance"

git add README.md
git commit -m "Update README with new login instructions"

Benefits:

    Easier to review - focused changes
    Easier to revert - surgical rollbacks
    Better history - clear development progression
    Easier debugging - git bisect to find issues

Part 2: AI Coding Tools (1 hour)
Section 1: Introduction to AI-Assisted Development (10 minutes)
The AI Revolution in Programming (3 minutes)

2020 vs 2026:

2020: Write everything from scratch
      Google for Stack Overflow answers
      Read documentation line by line
      Debug by print statements

2026: AI generates boilerplate instantly
      AI explains complex code in plain English  
      AI suggests fixes for errors
      AI refactors and optimizes code

**But the fundamental…
  5:20 PM
aws.amazon.com/training/learn-about/cloud-practitioner
Cloud Practitioner
Find information about foundational AWS training courses and certification for cloud practitioners.Amazon Web Services, Inc.Amazon Web Services, Inc.
  12:27 PM
course-signup-site-007658781819.s3-website.ap-south-1.amazonaws.com
Full-Stack Web Development — Course & Signup
Browse the curriculum and sign up for our Full-Stack Web Development course.
course-signup-site-007658781819.s3-website.ap-south-1.amazonaws.com
  4:23 PM
day-7-mini-project.md 
day-7-mini-project.md
Markdown
Day 6: Mini-Project Day

    Week 1 · Duration: 6 hours
    Deliverable: Working CLI tool deployed to GitHub with README

Instructor Notes
Schedule
Time 	Block 	Duration
9:00–9:30 	Morning brief 	30 min
9:30–12:00 	Build time (Part 1) 	2.5 hrs
12:00–12:45 	Lunch 	45 min
12:45–14:45 	Build time (Part 2) 	2 hrs
14:45–15:30 	Presentations 	45 min
15:30–15:45 	Retro 	15 min
Morning Brief Script (30 min)

    Set the tone (5 min): “Today you’re a developer shipping a product. By end of day, you’ll have a working tool on GitHub that anyone can clone and use.”
    Walk through requirements (10 min): Show rubric on screen. Emphasize: it must work, it must not crash, it must be documented.
    Demo a finished example (10 min): Show a simple CLI tool — run it, show the repo, show the README, show commit history.
    Q&A (5 min): Remind them: pick something you’d actually use.

Key message: “Done is better than perfect. Ship something that works, then improve it.”
Facilitation Guide

Let them struggle when:

    They’re Googling error messages
    They’re reading documentation
    They’re trying different approaches
    They’ve been stuck < 15 minutes

Step in when:

    Same issue for 20+ minutes
    Stuck on environment/setup (not today’s learning goal)
    Visibly frustrated and shutting down
    Past 12:00 and haven’t started coding

Common Blockers & Hints
Blocker 	Hint (not solution)
“I don’t know where to start” 	“What’s the simplest version? Build that first. One function, one feature.”
JSON file not found 	“Print os.getcwd(). Are you running from the right directory?”
API returning errors 	“Print the full response. What status code? Check the API docs.”
Class confusion 	“What thing are you modeling? What data does it hold? What can it do?”
“My code is too messy” 	“Does it work? Ship it working first. Refactor later.”
Git issues 	“git status first. Then git log --oneline. What does it say?”
Early Finishers

    Add a feature
    Write tests
    Help a classmate (explain, don’t type for them)
    Add color output (colorama library)
    Add a --help flag with argparse

Emergency Intervention (student stuck at 12:00)

    Sit with them for 5 minutes
    Help pick the simplest possible version
    Sketch structure on paper: “3 files, 2 classes, done”
    Get them to a working “hello world” version in 15 minutes
    If stuck on idea: assign Expense Tracker or Contact Book

Student Material
Project Brief

What you’re building: A command-line tool that solves a real problem. Something you or someone you know would actually use.
Requirements

Your project must include:

    [ ] Solves a real problem (not just a toy)
    [ ] Uses functions (at least 3 non-trivial)
    [ ] Uses at least one class
    [ ] Uses file I/O (JSON/CSV/text) OR an API call
    [ ] Has error handling (try/except — doesn’t crash on bad input)
    [ ] Has a clear user interface (interactive menu or command-line arguments)
    [ ] Includes a README.md (description, setup, usage, examples)
    [ ] Pushed to GitHub with at least 5 meaningful commits
    [ ] Code follows PEP 8 (readable, good naming)

Project Ideas

Pick one, or propose your own (check with instructor):
# 	Project 	Description 	Difficulty
1 	Expense Tracker 	Track daily expenses, categorize, view summaries 	⭐
2 	Flashcard Tool 	Create decks, quiz yourself, track scores 	⭐
3 	Task Manager 	Add tasks with deadlines, priorities, mark complete 	⭐
4 	Contact Book 	Store, search, edit, export contacts 	⭐
5 	Weather Dashboard 	Fetch weather for multiple cities, save history 	⭐⭐
6 	Password Generator 	Generate, store, retrieve passwords locally 	⭐⭐
7 	Quiz Engine 	Load questions from JSON/API, timed quizzes, high scores 	⭐⭐
8 	Bookmark Manager 	Save, tag, search, open bookmarks from terminal 	⭐⭐
9 	GitHub Repo Scout 	Search GitHub repos by language/stars, save favorites 	⭐⭐
10 	Habit Tracker 	Log daily habits, view streaks, weekly summaries 	⭐⭐⭐
AI Tool Usage Policy

✅ ALLOWED:
- Using Kiro, Cursor Agent, or other AI tools
- Asking AI to explain concepts or errors
- Asking AI to generate boilerplate
- Asking AI to debug or review your code

⚠️ REQUIRED:
- You MUST understand every line of code
- You MUST be able to explain what any function does and WHY
- You MUST be able to modify the code if asked

❌ NOT ALLOWED:
- Submitting code you cannot explain
- Copying an entire project without understanding it

The “Explain This Line” Rule: During presentations, the instructor may point to any line and ask what it does. If you can’t answer, you need to go back and understand your code.
README Template

Use this template for your project:

# [Project Name]

[One-line description]

## Problem It Solves

[2-3 sentences: What problem? Who would use it?]

## Features

- [Feature 1]
- [Feature 2]
- [Feature 3]

## Setup

### Prerequisites
- Python 3.13+

### Installation
```bash
git clone https://github.com/[username]/[repo].git
cd [repo]
pip install -r requirements.txt

Usage

python main.py

Examples

# Example with expected output

Project Structure

project/
├── main.py
├── [module].py
├── data/
├── README.md
└── requirements.txt

What I Learned

    [Key learning 1]
    [Key learning 2]

Future Improvements

    [ ] [Improvement 1]
    [ ] [Improvement 2]


---

### Commit Strategy

Don't make one giant commit at the end. Commit as you build:

```bash
git add main.py
git commit -m "Add project skeleton with main menu"

git add expense.py
git commit -m "Implement Expense class with validation"

git add .
git commit -m "Add JSON persistence for expenses"

git add .
git commit -m "Add category filtering and summary"

git add README.md
git commit -m "Add README with setup and usage instructions"

Minimum 5 commits. Each should represent a logical step.
Presentation Guide (2 minutes)

Structure your demo:

    What it does (10 sec) — one sentence
    Live demo (60 sec) — show it working
    One interesting challenge (30 sec) — what was hard and how you solved it
    What you’d add next (20 sec) — if you had more time

Rubric
Criteria 	Excellent (5) 	Good (4) 	Adequate (3) 	Needs Work (2) 	Incomplete (1)
Functionality 	Works perfectly, handles edge cases 	Works for main use case 	Mostly works, minor bugs 	Partially works 	Doesn’t run
Code Quality 	Clean, organized, PEP 8, good naming 	Mostly clean, minor issues 	Readable but disorganized 	Hard to follow 	Unreadable
Error Handling 	Handles all bad input gracefully 	Handles most bad input 	Some try/except 	Minimal 	Crashes on bad input
Documentation 	Complete README, clear examples 	Good README, minor gaps 	Basic README 	Minimal 	No README
Git Usage 	5+ meaningful commits, clear messages 	4-5 commits 	3 commits 	2 commits 	1 giant commit
Presentation 	Clear demo, explains decisions 	Good demo 	Adequate 	Unclear 	No demo

Scoring: 30 points max. 25+ = Exceeds. 20-24 = Meets. 15-19 = Approaching. <15 = Needs revision.
Exit Check

    [ ] Project runs without errors
    [ ] README exists with description, setup, and usage
    [ ] At least 5 commits on GitHub
    [ ] Can explain every line of code
    [ ] Presented to the class (2 min)

Resources
Resource 	URL
Python argparse tutorial 	https://docs.python.org/3.13/howto/argparse.html
PEP 8 Style Guide 	https://peps.python.org/pep-0008/
GitHub: Creating a repo 	https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
Open-Meteo API (if using weather) 	https://open-meteo.com/en/docs
requests library 	https://requests.readthedocs.io/

Infinitra Build · Week 1 · Day 7 (Mini-Project)
  5:06 PM
https://form.typeform.com/to/CHNu8WtN
New form
Turn data collection into an experience with Typeform. Create beautiful online forms, surveys, quizzes, and so much more. Try it for FREE.form.typeform.com


Message infinitra-build-sep2026
:bell:
Slack needs your permission to enable notifications. 
loading…
Slack is trying to connect. 
Day 6: Mini-Project Day

    Week 1 · Duration: 6 hours
    Deliverable: Working CLI tool deployed to GitHub with README

Instructor Notes
Schedule
Time 	Block 	Duration
9:00–9:30 	Morning brief 	30 min
9:30–12:00 	Build time (Part 1) 	2.5 hrs
12:00–12:45 	Lunch 	45 min
12:45–14:45 	Build time (Part 2) 	2 hrs
14:45–15:30 	Presentations 	45 min
15:30–15:45 	Retro 	15 min
Morning Brief Script (30 min)

    Set the tone (5 min): “Today you’re a developer shipping a product. By end of day, you’ll have a working tool on GitHub that anyone can clone and use.”
    Walk through requirements (10 min): Show rubric on screen. Emphasize: it must work, it must not crash, it must be documented.
    Demo a finished example (10 min): Show a simple CLI tool — run it, show the repo, show the README, show commit history.
    Q&A (5 min): Remind them: pick something you’d actually use.

Key message: “Done is better than perfect. Ship something that works, then improve it.”
Facilitation Guide

Let them struggle when:

    They’re Googling error messages
    They’re reading documentation
    They’re trying different approaches
    They’ve been stuck < 15 minutes

Step in when:

    Same issue for 20+ minutes
    Stuck on environment/setup (not today’s learning goal)
    Visibly frustrated and shutting down
    Past 12:00 and haven’t started coding

Common Blockers & Hints
Blocker 	Hint (not solution)
“I don’t know where to start” 	“What’s the simplest version? Build that first. One function, one feature.”
JSON file not found 	“Print os.getcwd(). Are you running from the right directory?”
API returning errors 	“Print the full response. What status code? Check the API docs.”
Class confusion 	“What thing are you modeling? What data does it hold? What can it do?”
“My code is too messy” 	“Does it work? Ship it working first. Refactor later.”
Git issues 	“git status first. Then git log --oneline. What does it say?”
Early Finishers

    Add a feature
    Write tests
    Help a classmate (explain, don’t type for them)
    Add color output (colorama library)
    Add a --help flag with argparse

Emergency Intervention (student stuck at 12:00)

    Sit with them for 5 minutes
    Help pick the simplest possible version
    Sketch structure on paper: “3 files, 2 classes, done”
    Get them to a working “hello world” version in 15 minutes
    If stuck on idea: assign Expense Tracker or Contact Book

Student Material
Project Brief

What you’re building: A command-line tool that solves a real problem. Something you or someone you know would actually use.
Requirements

Your project must include:

    [ ] Solves a real problem (not just a toy)
    [ ] Uses functions (at least 3 non-trivial)
    [ ] Uses at least one class
    [ ] Uses file I/O (JSON/CSV/text) OR an API call
    [ ] Has error handling (try/except — doesn’t crash on bad input)
    [ ] Has a clear user interface (interactive menu or command-line arguments)
    [ ] Includes a README.md (description, setup, usage, examples)
    [ ] Pushed to GitHub with at least 5 meaningful commits
    [ ] Code follows PEP 8 (readable, good naming)

Project Ideas

Pick one, or propose your own (check with instructor):
# 	Project 	Description 	Difficulty
1 	Expense Tracker 	Track daily expenses, categorize, view summaries 	⭐
2 	Flashcard Tool 	Create decks, quiz yourself, track scores 	⭐
3 	Task Manager 	Add tasks with deadlines, priorities, mark complete 	⭐
4 	Contact Book 	Store, search, edit, export contacts 	⭐
5 	Weather Dashboard 	Fetch weather for multiple cities, save history 	⭐⭐
6 	Password Generator 	Generate, store, retrieve passwords locally 	⭐⭐
7 	Quiz Engine 	Load questions from JSON/API, timed quizzes, high scores 	⭐⭐
8 	Bookmark Manager 	Save, tag, search, open bookmarks from terminal 	⭐⭐
9 	GitHub Repo Scout 	Search GitHub repos by language/stars, save favorites 	⭐⭐
10 	Habit Tracker 	Log daily habits, view streaks, weekly summaries 	⭐⭐⭐
AI Tool Usage Policy

✅ ALLOWED:
- Using Kiro, Cursor Agent, or other AI tools
- Asking AI to explain concepts or errors
- Asking AI to generate boilerplate
- Asking AI to debug or review your code

⚠️ REQUIRED:
- You MUST understand every line of code
- You MUST be able to explain what any function does and WHY
- You MUST be able to modify the code if asked

❌ NOT ALLOWED:
- Submitting code you cannot explain
- Copying an entire project without understanding it

The “Explain This Line” Rule: During presentations, the instructor may point to any line and ask what it does. If you can’t answer, you need to go back and understand your code.
README Template

Use this template for your project:

# [Project Name]

[One-line description]

## Problem It Solves

[2-3 sentences: What problem? Who would use it?]

## Features

- [Feature 1]
- [Feature 2]
- [Feature 3]

## Setup

### Prerequisites
- Python 3.13+

### Installation
```bash
git clone https://github.com/[username]/[repo].git
cd [repo]
pip install -r requirements.txt

Usage

python main.py

Examples

# Example with expected output

Project Structure

project/
├── main.py
├── [module].py
├── data/
├── README.md
└── requirements.txt

What I Learned

    [Key learning 1]
    [Key learning 2]

Future Improvements

    [ ] [Improvement 1]
    [ ] [Improvement 2]


---

### Commit Strategy

Don't make one giant commit at the end. Commit as you build:

```bash
git add main.py
git commit -m "Add project skeleton with main menu"

git add expense.py
git commit -m "Implement Expense class with validation"

git add .
git commit -m "Add JSON persistence for expenses"

git add .
git commit -m "Add category filtering and summary"

git add README.md
git commit -m "Add README with setup and usage instructions"

Minimum 5 commits. Each should represent a logical step.
Presentation Guide (2 minutes)

Structure your demo:

    What it does (10 sec) — one sentence
    Live demo (60 sec) — show it working
    One interesting challenge (30 sec) — what was hard and how you solved it
    What you’d add next (20 sec) — if you had more time

Rubric
Criteria 	Excellent (5) 	Good (4) 	Adequate (3) 	Needs Work (2) 	Incomplete (1)
Functionality 	Works perfectly, handles edge cases 	Works for main use case 	Mostly works, minor bugs 	Partially works 	Doesn’t run
Code Quality 	Clean, organized, PEP 8, good naming 	Mostly clean, minor issues 	Readable but disorganized 	Hard to follow 	Unreadable
Error Handling 	Handles all bad input gracefully 	Handles most bad input 	Some try/except 	Minimal 	Crashes on bad input
Documentation 	Complete README, clear examples 	Good README, minor gaps 	Basic README 	Minimal 	No README
Git Usage 	5+ meaningful commits, clear messages 	4-5 commits 	3 commits 	2 commits 	1 giant commit
Presentation 	Clear demo, explains decisions 	Good demo 	Adequate 	Unclear 	No demo

Scoring: 30 points max. 25+ = Exceeds. 20-24 = Meets. 15-19 = Approaching. <15 = Needs revision.
Exit Check

    [ ] Project runs without errors
    [ ] README exists with description, setup, and usage
    [ ] At least 5 commits on GitHub
    [ ] Can explain every line of code
    [ ] Presented to the class (2 min)

Resources
Resource 	URL
Python argparse tutorial 	https://docs.python.org/3.13/howto/argparse.html
PEP 8 Style Guide 	https://peps.python.org/pep-0008/
GitHub: Creating a repo 	https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
Open-Meteo API (if using weather) 	https://open-meteo.com/en/docs
requests library 	https://requests.readthedocs.io/

Infinitra Build · Week 1 · Day 7 (Mini-Project)

