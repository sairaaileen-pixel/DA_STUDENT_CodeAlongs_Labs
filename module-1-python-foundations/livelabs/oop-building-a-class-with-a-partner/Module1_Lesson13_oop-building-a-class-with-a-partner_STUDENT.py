#!/usr/bin/env python3
"""OOP: Building a Class With a Partner
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson13_oop-building-a-class-with-a-partner_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson13_oop-building-a-class-with-a-partner_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson13_oop-building-a-class-with-a-partner_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Step 1: __init__ and Attributes =====
# Write a BoardGame class that stores a title, player count and category, then
# build Connect Four and print two of its values.
print('----- 1. Step 1: __init__ and Attributes -----')
# TODO: define class BoardGame with __init__(self, title,
# players_available, category) that stores all three as
# self.title, self.players_available, self.category


# TODO: create connect4 = BoardGame("Connect Four", 4, "Strategy")
# TODO: print connect4.title, then print connect4.players_available

# DISCUSS: Why does connect4.players_available hold 4 and not "Connect Four" in
#          the Step 1 code? Talk it over with your partner.
# Your answer:
#
#


# ===== 2. Step 2: Add a Method =====
# Give BoardGame a method that checks its own player count and reports whether
# the game is running low.
print('----- 2. Step 2: Add a Method -----')
# TODO: keep Step 1's __init__
# TODO: add a method is_low_stock(self) that returns
# self.players_available < 3


# TODO: create connect4 again, then print connect4.is_low_stock()

# PREDICT before you run: Which change makes connect4.is_low_stock() return
#                         True: the player count set to 2, the category set to
#                         "Party", or the title set to "Uno"? Agree on one with
#                         your partner, make that change in the Step 2 code,
#                         and run it.
# Your answer:
#
#


# ===== 3. Step 3: Prove Independent Storage =====
# Make two games, change only one of them, and check that the other game still
# keeps its own data.
print('----- 3. Step 3: Prove Independent Storage -----')
# TODO: create connect4 = BoardGame("Connect Four", 4, "Strategy")
# TODO: create uno = BoardGame("Uno", 8, "Party")


# TODO: set connect4.players_available = 1
# TODO: print connect4.is_low_stock(), then print uno.is_low_stock()

# DISCUSS: In the Step 3 code, connect4.is_low_stock() prints True but
#          uno.is_low_stock() still prints False. Why? Talk it over with your
#          partner.
# Your answer:
#
#
