#!/usr/bin/env python3
"""Error Handling
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson10_error-handling_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson10_error-handling_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson10_error-handling_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Watch This Crash =====
# This code tries to turn the text "abc" into a number. Run it and read the
# error message Python prints.
# Watch-only demo: the code is already here. Run it and read the output.
# This is supposed to raise ValueError: run it, read the traceback, then
# comment out the raising line so the rest of the file runs.
print('----- 1. Watch This Crash -----')
quantity = "abc"
count = int(quantity)
print("Converted:", count)

# PREDICT before you run: This crash is a ValueError. Which error would "5" + 3
#                         raise? ValueError, TypeError or NameError?
# Your answer:
#
#
#
# PREDICT before you run: A function reads a variable that was defined only
#                         inside another function. Which error does Python
#                         raise?
# Your answer:
#
#


# ===== 2. Catching the Crash =====
# Use try and except so a bad number prints a friendly message instead of
# crashing.
print('----- 2. Catching the Crash -----')
# TODO: set quantity = "abc"
# TODO: inside a try block, convert it to int and print "Converted:"
# plus the result
# TODO: in an except ValueError block, print "That's not a valid
# number."

# DISCUSS: In the door-handle analogy, which part of this code is reacting once
#          you find the door locked?
# Your answer:
#
#
#
# PREDICT before you run: Change quantity to "5". What prints now?
# Your answer:
#
#


# ===== 3. Putting It Together: Two except Clauses =====
# Write validate_batch so it catches two kinds of bad lines, each with its own
# message, and keeps going.
print('----- 3. Putting It Together: Two except Clauses -----')
# TODO: define validate_batch(lines)
# TODO: for each line, inside a try block: split on ",", print
# "OK:" with fields[1] and int(fields[2])
# TODO: add an except IndexError clause printing "Bad format:" + line
# TODO: add an except ValueError clause printing "Bad quantity:" + line

# TODO: create a list called lines with these 3 strings:
# "ADD,Chess,4", "REMOVE,Uno", "ADD,Dice,two"
# TODO: call validate_batch(lines)

# PREDICT before you run: For "REMOVE,Uno", which step raises the error?
#                         line.split(","), fields[2], or int(...)?
# Your answer:
#
#
#
# DISCUSS: What if you replaced both except clauses with one bare except:? What
#          is the real risk?
# Your answer:
#
#
