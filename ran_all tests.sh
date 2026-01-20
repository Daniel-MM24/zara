#!/bin/bash

VENV_PY="/home/kali/Desktop/zara/.venv/bin/python"
TEST_DIR="/home/kali/Desktop/zara/tests"

for testfile in "$TEST_DIR"/test*.py; do
    echo "=============================="
    echo "Running $testfile"
    echo "=============================="
    "$VENV_PY" "$testfile"
    echo
done
