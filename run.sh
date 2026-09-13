#!/usr/bin/env bash
# run.sh — Setup and launch script for Task Manager CLI
#
# Usage:
#   bash run.sh           → run the application
#   bash run.sh --test    → run the unit tests instead
#
# This script:
#   1. Verifies Python 3.13+ is available
#   2. Creates the data/ directory if missing
#   3. Runs the application (or tests)
#
# Works on Ubuntu. Does not delete any user data.

set -e  # Exit immediately if any command returns a non-zero exit code.

# ------------------------------------------------------------------
# Step 1: Check Python version
# ------------------------------------------------------------------

# Find a Python 3 executable.
PYTHON=""
for candidate in python3.13 python3 python; do
    if command -v "$candidate" &>/dev/null; then
        PYTHON="$candidate"
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "❌ Python 3 not found."
    echo "   Install Python 3.13: sudo apt install python3.13"
    exit 1
fi

# Check the major.minor version is at least 3.13.
VERSION=$("$PYTHON" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
MAJOR=$(echo "$VERSION" | cut -d. -f1)
MINOR=$(echo "$VERSION" | cut -d. -f2)

if [ "$MAJOR" -lt 3 ] || { [ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 13 ]; }; then
    echo "❌ Python 3.13 or later is required. Found: Python $VERSION"
    echo "   Install Python 3.13: sudo apt install python3.13"
    exit 1
fi

echo "✅ Python $VERSION found."

# ------------------------------------------------------------------
# Step 2: Ensure the data/ directory exists
# ------------------------------------------------------------------

# The application creates this at runtime, but creating it here
# avoids any startup message about missing directories.
if [ ! -d "data" ]; then
    mkdir -p data
    echo "✅ Created data/ directory."
fi

# ------------------------------------------------------------------
# Step 3: Run the application or tests
# ------------------------------------------------------------------

if [ "$1" = "--test" ]; then
    echo ""
    echo "Running unit tests..."
    echo "---------------------"
    "$PYTHON" -m unittest discover tests -v
else
    echo ""
    "$PYTHON" main.py
fi
