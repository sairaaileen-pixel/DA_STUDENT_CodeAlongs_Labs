#!/usr/bin/env python3
"""Magic Methods — What __init__/__str__/__repr__ Actually Mean
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson14_magic-methods-what-init-str-repr-actually-mean_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson14_magic-methods-what-init-str-repr-actually-mean_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson14_magic-methods-what-init-str-repr-actually-mean_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Watch This: The Default Is Ugly =====
# This builds one game and prints it before the class knows how to describe
# itself, so Python shows its own default text.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 1. Watch This: The Default Is Ugly -----')
class BoardGame:
    def __init__(self, title, players_available,
                 category):
        self.title = title
        self.players_available = players_available
        self.category = category

connect4 = BoardGame("Connect Four", 4, "Strategy")
print(connect4)


# ===== 2. Step 1: Add __str__ =====
# Teach BoardGame to describe itself in plain words, so printing a game shows
# its title and how many are left.
print('----- 2. Step 1: Add __str__ -----')
# TODO: keep __init__ from before
# TODO: add __str__(self) that returns
# f"{self.title}, {self.players_available} left"


# TODO: create connect4 again, then print(connect4)

# DISCUSS: The Step 1 code never calls __str__ by name. So why did
#          print(connect4) change? Talk it over with your partner.
# Your answer:
#
#


# ===== 3. Step 2: Add __repr__ Too =====
# Add a second, more exact way for BoardGame to describe itself, one that helps
# a coder track down bugs.
print('----- 3. Step 2: Add __repr__ Too -----')
# TODO: keep __init__ and __str__ from Step 1
# TODO: add __repr__(self) that returns f"BoardGame('{self.title}')"


# ===== 4. Now Test repr() =====
# This asks Python for the exact version of one game instead of the friendly
# version, then prints the result.
# Watch-only demo: the code is already here. Run it and read the output.
#
# PREDICT before you run: What will print(repr(connect4)) show? Write your
#                         guess before you run it.
# Your answer:
#
#
print('----- 4. Now Test repr() -----')
connect4 = BoardGame("Connect Four", 4, "Strategy")
print(repr(connect4))

# DISCUSS: Why did the Now Test repr() code print BoardGame('Connect Four') and
#          not Connect Four, 4 left? Talk it over with your partner.
# Your answer:
#
#


# ===== 5. The Real Gotcha: A List of Objects =====
# Print one game by itself, then print a list of two games, and compare which
# description each line uses.
#
# PREDICT before you run: Inside print([connect4, uno]), which method runs for
#                         each object: __str__ or __repr__? Predict both
#                         printed lines with your partner before you run.
# Your answer:
#
#
print('----- 5. The Real Gotcha: A List of Objects -----')
# TODO: create connect4 and uno again
# TODO: print(connect4) alone
# TODO: print a list containing both: [connect4, uno]
