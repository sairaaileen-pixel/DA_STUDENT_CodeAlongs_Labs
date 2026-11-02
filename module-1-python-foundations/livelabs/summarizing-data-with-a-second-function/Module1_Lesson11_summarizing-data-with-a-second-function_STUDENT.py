#!/usr/bin/env python3
"""Summarizing Data With a Second Function
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson11_summarizing-data-with-a-second-function_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson11_summarizing-data-with-a-second-function_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson11_summarizing-data-with-a-second-function_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Step 1: A Formatted Listing =====
# Write summarize_batch to print one line per game showing how many players are
# available.
print('----- 1. Step 1: A Formatted Listing -----')
# TODO: create a list called games of (title, players) tuples:
# ("Chess", 4), ("Checkers", 6), ("Clue", 1), ("Uno", 8)


# TODO: define summarize_batch(games) that prints one formatted
# line per game: "{title}: {players} available"


# TODO: call summarize_batch(games)

# PREDICT before you run: What is the third line this code prints?
# Your answer:
#
#


# ===== 2. Step 2: Add a Low-Availability Alert =====
# Add a second list to summarize_batch that flags every game with fewer than 3
# players.
print('----- 2. Step 2: Add a Low-Availability Alert -----')
# TODO: keep Step 1's listing loop
# TODO: print a blank line, then "Low availability:"
# TODO: loop over games again; if players < 3, print
# "  {title} ({players})"
# TODO: call summarize_batch(games)

# PREDICT before you run: In the games list, change Uno from 8 to 2. What
#                         changes in the output?
# Your answer:
#
#


# ===== 3. Step 3: Add a Total Count =====
# Finish summarize_batch with one last line that says how many games are in the
# list.
print('----- 3. Step 3: Add a Total Count -----')
# TODO: keep Step 2's listing and alert loops
# TODO: print a blank line, then f"{len(games)} games total"
# TODO: call summarize_batch(games)

# PREDICT before you run: Add one more game to the games list, like ("Dice",
#                         5). What prints last?
# Your answer:
#
#
