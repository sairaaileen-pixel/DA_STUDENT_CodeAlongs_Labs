#!/usr/bin/env python3
"""Big-O in Practice: Linear Scan vs. Dict Lookup, With a Partner
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson15_big-o-in-practice-linear-scan-vs-dict-lookup-with-a-partner_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson15_big-o-in-practice-linear-scan-vs-dict-lookup-with-a-partner_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson15_big-o-in-practice-linear-scan-vs-dict-lookup-with-a-partner_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Setup: A Class and Its Objects =====
# Create a SupplyItem class and a list of four supply items to search.
print('----- 1. Setup: A Class and Its Objects -----')
# TODO: define SupplyItem with __init__ storing name, count,
# department


# TODO: create a list called supplies with 4 SupplyItem objects
# of your own choosing


# ===== 2. Search 1: Linear Scan =====
# Write a function that checks each item one at a time until it finds the one
# with the right name.
print('----- 2. Search 1: Linear Scan -----')
# TODO: define find_by_name_linear(supplies, name) that loops over
# supplies and returns the item whose .name matches, or None if
# nothing matches


# TODO: call it looking for "Tape", then print the result's name
# and count

# PREDICT before you run: What does find_by_name_linear(supplies, "Nope")
#                         return? Agree on a guess with your partner, then add
#                         print(find_by_name_linear(supplies, "Nope")) under
#                         the Tape search in Search 1: Linear Scan and run it.
# Your answer:
#
#


# ===== 3. Search 2: Dict-Keyed Lookup =====
# Build a dict keyed by item name, then find Tape in one step with .get().
print('----- 3. Search 2: Dict-Keyed Lookup -----')
# TODO: build supplies_by_name as a dict comprehension keyed by
# each item's .name, valued as the item itself


# TODO: look up "Tape" with .get(), then print its name and count

# PREDICT before you run: What does supplies_by_name.get("Nope") return? Agree
#                         on a guess with your partner, then add
#                         print(supplies_by_name.get("Nope")) under the Tape
#                         lookup in Search 2: Dict-Keyed Lookup and run it.
# Your answer:
#
#
#
# DISCUSS: What is the Big-O of each search, and why does the dict lookup scale
#          better as the list grows? Agree on both answers with your partner.
# Your answer:
#
#
