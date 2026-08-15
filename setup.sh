#!/bin/bash
echo "========================================================"
echo "  Launching Reframe Automated Setup (macOS / Linux)..."
echo "========================================================"
if command -v python3 &>/dev/null; then
    python3 setup.py
elif command -v python &>/dev/null; then
    python setup.py
else
    echo "Python not found. Please install Python to run automated setup."
fi
