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

# Paste your class here (or the sample LibraryTool from the slides)

class LibraryTool:
    def __init__(self, tool_name, quantity_available, requires_inspection):
        self.tool_name = tool_name
        self.quantity_available = quantity_available
        self.requires_inspection = requires_inspection

    def is_available(self):
        return self.quantity_available > 0


def make_batch(size):

    tools = []

    for i in range(size):
        tools.append(LibraryTool(f"Tool{i}", random.randint(0, 5), random.choice([True, False])))
    
    return tools


small_batch = make_batch(10)
medium_batch = make_batch(1000)
large_batch = make_batch(100000)


# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

def find_by_name_linear(tools, name):
   
    for tool in tools:
   
        if tool.tool_name == name:
            return tool
    return None 
    


def build_lookup(tools):
   
    return {tool.tool_name: tool for tool in tools}

lookup = build_lookup(large_batch)
print(find_by_name_linear(large_batch, "Tool99999").tool_name)
print(lookup.get("Tool99999").tool_name)

# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

import time  # Python's built-in module; time.perf_counter() is new

# Predict first: which time grows with size? Write it here:
# Prediction:
#  Linear search time (linear_time) will grow proportionally with the batch size (O(N)),
#  while dictionary lookup time (dict_time) 
#  will stay flat (O(1)) because hash table lookups do not depend on the number of items stored.

pairs = [
    (10, small_batch),
    (1000, medium_batch),
    (100000, large_batch)
]

for size, batch in pairs:
    lookup = build_lookup(batch)
    start = time.perf_counter()
    find_by_name_linear(batch, "NotThere")
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    lookup.get("NotThere")
    dict_time = time.perf_counter() - start

    print(size, linear_time, dict_time)

# Output:
# 10 1.5226000000034823e-05 2.6909999999435996e-06
# 1000 9.891299999997827e-05 1.0270000000422996e-06
# 100000 0.008113929999999936 3.1560000000041555e-06

# Test AI-optimized linear search

def find_by_name_linear_optimized(tools, name):
    return next((tool for tool in tools if tool.tool_name == name), None)

start = time.perf_counter()
find_by_name_linear(batch, "NotThere")
orig_time = time.perf_counter() - start



start = time.perf_counter()
find_by_name_linear_optimized(batch, "NotThere")
opt_time = time.perf_counter() - start


print(f"Size {size} | Original: {orig_time:.6f}s | Optimized: {opt_time:.6f}s")

# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer:
# No, a linear search will not be fine at 100,000 records due to O(N) scaling, but it will remain fine using a dictionary lookup because of its O(1) constant time.


# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
# An AI suggested using a generator expression with next() to speed up the linear scan. 
# However, when tested at 100,000 items, the optimized version (0.023351s) was actually slightly slower than the original for-loop (0.016703s).
# This proves that minor code tricks cannot fix O(N) growth; only switching to a dictionary lookup (O(1)) actually solves the scaling problem.

# Terminal output: 
# Size 100000 | Original: 0.016703s | Optimized: 0.023351s

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
#  Your notes for the share out:
#
# 1. Raw Timings (Linear O(N) vs. Dictionary O(1)):
#    - Size 10:      Linear = 0.000011s | Dict = 0.000002s
#    - Size 1,000:   Linear = 0.000059s | Dict = 0.0000005s
#    - Size 100,000: Linear = 0.009701s | Dict = 0.000004s
#
# 2. Trends and Tipping Point:
#    - Linear search grew noticeably as the batch scaled (jumping to ~9.7 ms).
#    - Dictionary lookup stayed completely flat (~0.000004s) at every size.
#    - Tipping point: At 100,000 items, the gap stopped being subtle—dictionary lookup was over 2,000x faster.
#
# 3. Why It Happens & Why We Tested This Way:
#    - Searched for a target not in the list ("NotThere") to force the worst-case scenario; otherwise, an early match makes linear search look falsely fast.
#    - Linear slows down because it checks items one by one O(N); dictionary stays flat because hash tables jump straight to the key O(1).
#
# 4. AI Stretch Test (next() generator expression):
#    - AI claimed using next() would speed up the linear scan.
#    - My numbers proved it wrong: Original = 0.016703s vs. AI-Optimized = 0.023351s (actually slower at 100,000 items).
#    - Takeaway: Syntax shortcuts can't fix O(N) growth; only switching to an O(1) dictionary solves the scaling bottleneck.
# 
