# Test driver for the Student Grade Calculator program.
# This script runs VIBE.py and supplies sample student input automatically.
# It is meant to exercise the program with the required three sample students.

import builtins
import os
import runpy

if os.path.exists("student_grades.txt"):
    os.remove("student_grades.txt")

test_inputs = iter([
    "1",  "Alice Johnson", "S1001", "95", "88", "92",
    "1",  "Bob Smith",     "S1002", "78", "82", "75",
    "1",  "Jamie Smith",   "S1003", "65", "98", "75",
    "2",                          #Display all students
    "3", "Bob Smith",                 #Search - found
    "3", "Ashley Mollina",            #Search - not found
    "4",                              #Class statistics
    "5"                               #Save and exit
])

def driver(prompt=""):
    value = next(test_inputs)
    print(f"{prompt}{value}")
    return value

builtins.input = driver

runpy.run_path("VIBE.py", run_name="__main__")
