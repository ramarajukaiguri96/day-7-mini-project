# Setup and Run

## Prerequisites

- Python 3.13 or later
- Git (for cloning)
- No third-party packages required

---

## Option A — Using run.sh (Recommended)

### VS Code Terminal or Ubuntu Terminal

```bash
# Clone the repository
git clone https://github.com/ramarajukaiguri96/day-7-mini-project.git
cd day-7-mini-project

# Run the application
bash run.sh

# Run the tests
bash run.sh --test
```

The script checks your Python version, creates the data/ directory if needed,
and launches the application.

---

## Option B — Direct Python

### Ubuntu Terminal

```bash
# Clone the repository
git clone https://github.com/ramarajukaiguri96/day-7-mini-project.git
cd day-7-mini-project

# Run the application
python3 main.py

# Run the tests
python3 -m unittest discover tests -v
```

### VS Code Terminal

Open the project folder in VS Code, then open the integrated terminal
(Ctrl + ` or View → Terminal) and run:

```bash
python3 main.py
```

---

## Verify Python Version

```bash
python3 --version
```

Expected output: `Python 3.13.x` (or later)

If Python 3.13 is not installed on Ubuntu:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.13 -y
```

---

## Running Tests

```bash
python3 -m unittest discover tests -v
```

Expected output ends with:
```
Ran 92 tests in X.XXXs

OK
```

---

## Project Structure After Setup

```
day-7-mini-project/
├── main.py
├── task.py
├── storage.py
├── task_manager.py
├── tests/
│   ├── test_task.py
│   ├── test_storage.py
│   └── test_task_manager.py
├── data/
│   └── tasks.json     ← created automatically on first run
├── docs/
├── project-docs/
├── README.md
├── .gitignore
└── run.sh
```

---

## Troubleshooting

**"python3: command not found"**
```bash
sudo apt install python3.13
```

**"Permission denied" on data/tasks.json**
```bash
ls -l data/
chmod 644 data/tasks.json
```

**"No module named task"**
Make sure you are running the command from the project root directory:
```bash
cd /path/to/day-7-mini-project
python3 main.py
```
