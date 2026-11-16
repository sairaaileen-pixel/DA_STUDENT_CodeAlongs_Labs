#!/usr/bin/env python3
"""Debugging Like a Pro: Finding Planted Bugs Independently
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson16_debugging-like-a-pro-finding-planted-bugs-independently_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson16_debugging-like-a-pro-finding-planted-bugs-independently_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson16_debugging-like-a-pro-finding-planted-bugs-independently_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. The Script, Part 1: The Class =====
# This code defines a BoardGame class that stores a title, the number of open
# player slots, and a category.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 1. The Script, Part 1: The Class -----')
class BoardGame:
    def __init__(self, title,
               players_available, category):
        self.title = title
        self.players_available = players_available
        self.category = category

    def is_available(self):
        return self.players_available >= 0


# ===== 2. The Script, Part 2: The Data =====
# This code builds a list of four BoardGame objects for the script to count.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 2. The Script, Part 2: The Data -----')
games = [
    BoardGame("Catan", 3, "Strategy"),
    BoardGame("Uno", 0, "Card"),
    BoardGame("Chess", 2, "strategy"),
    BoardGame("Sorry!", 4, "Strategy"),
]


# ===== 3. The Script, Part 3: Counting Strategy Games =====
# This loop is meant to count how many games are in the Strategy category, then
# print a summary.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 3. The Script, Part 3: Counting Strategy Games -----')
strategy_count = 0
for i in range(len(games) - 1):
    if games[i].category == "Strategy":
        strategy_count += 1

print("--- Summary ---")
print("Category: Strategy")
print("Count:", strategy_count)


# ===== 4. The Script, Part 4: Counting Available Games =====
# This loop is meant to count how many games have at least one open player
# slot, then print a summary.
# Watch-only demo: the code is already here. Run it and read the output.
print('----- 4. The Script, Part 4: Counting Available Games -----')
available_count = 0
for game in games:
    if game.is_available():
        available_count += 1

print("--- Summary ---")
print("Category: Available")
print("Count:", available_count)

# DISCUSS: Would you trust the script in sections 1-4 if it ran clean? Pick yes
#          or no, then answer: what made it look trustworthy, or what would you
#          verify before trusting it?
# Your answer:
#
#


# Sections 5-8 are not in your copy. Your instructor runs them on the shared
# screen after work time.
