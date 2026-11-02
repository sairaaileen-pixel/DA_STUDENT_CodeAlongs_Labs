#!/usr/bin/env python3
"""Writing Your First Validation Function, From Scratch
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson9_writing-your-first-validation-function-from-scratch_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson9_writing-your-first-validation-function-from-scratch_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson9_writing-your-first-validation-function-from-scratch_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Step 1: Just Look at the Data =====
# Make a list of five shipment lines and print each one, so you see the data
# before you check it.
print('----- 1. Step 1: Just Look at the Data -----')
# TODO: create a list called lines with these 5 strings:
# "ADD,Chess,4", "ADD,Checkers,two", "ADD,Uno", "" (empty), "ADD,Clue,6"


# TODO: loop over lines and print each one


# ===== 2. Step 2: Check Each Line's Shape =====
# Check each line and report whether it has exactly three fields.
print("----- 2. Step 2: Check Each Line's Shape -----")
# TODO: loop over lines
# TODO: split each line on "," into a variable called fields
# TODO: if fields has exactly 3 items, print "Looks valid:" and the line
# TODO: otherwise, print "Wrong number of fields:" and the line

# PREDICT before you run: Which message prints for "ADD,Uno"?
# Your answer:
#
#


# ===== 3. Step 3: Wrap It in a Real Function =====
# Move your line check into a function called validate_batch, so it works on
# any list of lines.
print('----- 3. Step 3: Wrap It in a Real Function -----')
# TODO: define validate_batch(lines) — move Step 2's loop and
# conditional inside it


# TODO: call validate_batch(lines)


# ===== 4. Step 4: Add enumerate() =====
# Use enumerate() so each message names its line number, starting at 1.
print('----- 4. Step 4: Add enumerate() -----')
# TODO: change the loop to "for line_number, line in
# enumerate(lines, start=1):"
# TODO: update both print statements to use f"Line {line_number}: ..."
# instead of printing the line's text

# PREDICT before you run: Delete start=1, so the loop reads enumerate(lines).
#                         What line number does "ADD,Uno" get?
# Your answer:
#
#


# ===== 5. Putting It Together: Both Checks at Once =====
# Write validate_batch so it reports bad format, bad players, or OK for each
# numbered line.
print('----- 5. Putting It Together: Both Checks at Once -----')
# TODO: define validate_batch(lines) using enumerate(lines, 1)
# TODO: if len(fields) != 3, report "bad format"
# TODO: elif fields[2] isn't all digits (.isdigit()), report
# "bad players"
# TODO: else, unpack fields into action, title, players and report
# "OK, {title}"

# PREDICT before you run: Which check flags "ADD,Checkers,two"? The len(fields)
#                         check, the unpacking line, or the isdigit() check?
# Your answer:
#
#
