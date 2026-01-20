#!/bin/bash

VENV_PY="/home/dan/miniconda3/envs/learn_env/bin/python"
TEST_DIR="/home/dan/learn/projects/zara/tests"

for testfile in "$TEST_DIR"/test*.py; do
    echo "=============================="
    echo "Running $testfile"
    echo "=============================="
    "$VENV_PY" "$testfile"
    echo
done
