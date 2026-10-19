#!/usr/bin/env python3
"""Nested Loops & Conditionals
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson2_nested-loops-conditionals_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson2_nested-loops-conditionals_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson2_nested-loops-conditionals_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
#
# DISCUSS: Before you run the Nested Loop code, imagine both loops used
#          range(2). Put these outputs in the order Python prints them. A: 1 0.
#          B: 0 0. C: 1 1. D: 0 1.
# Your answer:
#
#
print('----- 1. Nested Loop, Live -----')
# TODO: write a nested loop that prints every (row, col)
# pair for row in range(2) and col in range(3)

# PREDICT before you run: Change the Nested Loop code to range(3) on the
#                         outside and range(2) on the inside. How many lines
#                         print?
# Your answer:
#
#
#
# DISCUSS: With range(3) outside and range(2) inside, a classmate's version
#          prints only 3 lines instead of 6. What's the most likely cause?
# Your answer:
#
#


# ===== 2. Nested Conditional, Live =====
# Check a transaction in two steps: first the operation type, then whether the
# quantity is positive. Here it should print Invalid quantity.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first; if it's "ADD", nest a second
# check confirming quantity is greater than 0
operation = "ADD"
quantity = -5

# DISCUSS: Suppose the inner quantity check in the Nested Conditional code
#          never seems to run. What should you trace first? Try it: set
#          operation to "SEARCH" and run.
# Your answer:
#
#


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# Check each transaction line and print whether it is valid, has an invalid
# quantity, or is a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
# TODO: loop over transactions; for each line, split it into
# operation and amount, then nest the ADD/quantity check
# from the nested-conditional step inside the loop
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]

# PREDICT before you run: In the Putting It Together code, which check flags
#                         "ADD -5" as invalid: operation == "ADD", amount > 0,
#                         or operation == "REMOVE"?
# Your answer:
#
#
