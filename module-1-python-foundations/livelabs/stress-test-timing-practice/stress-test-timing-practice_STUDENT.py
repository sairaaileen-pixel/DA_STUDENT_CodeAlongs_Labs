#!/usr/bin/env python3
"""Lab: Stress-Test Your Code: Timing & Efficiency
GitBook Quest 1.9: Lookups Matter

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 stress-test-timing-practice_STUDENT.py
    Or make it executable once:
        chmod +x stress-test-timing-practice_STUDENT.py
    and from then on run it directly:
        ./stress-test-timing-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it stress-test-timing-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Generate Batches of Your Class at Three Sizes (10, 1,000, and 100,000) =====
# Any class works: your own from Day 15's lab, a new one, or the sample
# LibraryTool on today's slides.

import random  # Python's built-in module for random values

# TODO: paste your class here (or the sample LibraryTool from the slides)


def make_batch(size):
    # TODO: make an empty list called batch
    # TODO: loop `size` times with: for i in range(size):
    # TODO: inside the loop, create one object and append it to batch
    # TODO: give each object a unique name, e.g. f"Tool{i}"
    # TODO: use random.randint(0, 5) for any number attribute
    # TODO: after the loop, return batch
    pass


# TODO: small_batch = make_batch(10)
# TODO: make medium_batch (1,000) and large_batch (100,000) the same way
# TODO: print len() of all three batches to check their sizes

# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

def find_by_name_linear(batch, name):
    # TODO: loop over batch, one object at a time
    # TODO: if the object's name equals name, return the object
    # TODO: after the loop, return None (nothing matched)
    pass


def build_lookup(batch):
    # TODO: return a dict: {obj.name: obj for obj in batch}
    # TODO: (use your class's real name attribute, e.g. tool_name)
    pass


# TODO: lookup = build_lookup(large_batch)
# TODO: pick a name you know is in large_batch, like "Tool99999"
# TODO: print what find_by_name_linear returns for that name
# TODO: print what lookup.get() returns for the same name
# TODO: check both printed lines show the same object

# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

import time  # Python's built-in module; time.perf_counter() is new

# TODO: predict first: which time grows with size? Write it here:
# Prediction:

# TODO: make a list of (size, batch) pairs for your three batches
# TODO: loop over that list: for size, batch in pairs:
# TODO:   lookup = build_lookup(batch)
# TODO:   start = time.perf_counter()
# TODO:   run find_by_name_linear(batch, "NotThere")
# TODO:   linear_time = time.perf_counter() - start
# TODO:   time lookup.get("NotThere") the same way, as dict_time
# TODO:   print(size, linear_time, dict_time)
# TODO: search for "NotThere" on purpose: a missing name is the worst case
# TODO: 1.5e-06 in your output means 0.0000015 seconds

# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer:
#
#

# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Bring your numbers, not a summary of them. Specifically:
# - Your timings at each batch size, for both searches. Everyone tested a
#   different class on a different laptop, so the raw numbers won't match -
#   put yours up anyway.
# - Which column changed as the batch grew, and which one didn't. - The
#   batch size where the difference stopped being something you had to
#   squint at.
# - Whether anything surprised you. A linear scan that looked suspiciously
#   flat is worth raising - say what you found out was going on.
# - If you tried the AI stretch: what it claimed, and whether your own
#   timings actually backed it up. "It was wrong" is a good answer if you
#   can show the number that proves it.
#
# Be ready for "why does that happen?" - the timings are evidence, and the
# explanation is what's being assessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
