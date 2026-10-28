#!/usr/bin/env python3
"""Day 8 code-along: Data Serialization. Run: python3 <file> or ./<file>"""

# ===== 1. Writing to a File =====
# Write two restock reminders to a file called notes.txt, one per line.
print('----- 1. Writing to a File -----')
# TODO: use a `with` block and open("notes.txt", "w")
# TODO: write "Restock staplers" and "Restock printer paper"
# TODO: end each line with "\n"


# ===== 2. Reading It Back =====
# Open notes.txt again and print everything inside it.
print('----- 2. Reading It Back -----')
# TODO: use a `with` block and open("notes.txt")
# TODO: print its full contents with f.read()

# PREDICT before you run: Rewrite notes.txt in "w" mode. Do old lines survive?
# Your answer:
#


# ===== 3. A CSV File Is Just Plain Text =====
# This code saves three supply rows as a CSV, then prints the file as text.
# TODO: run this and read the output
print('----- 3. A CSV File Is Just Plain Text -----')
csv_content = "name,count,department\nStapler,12,Office\nPaper,200,Office\n"

with open("supply.csv", "w") as f:
    f.write(csv_content)

with open("supply.csv") as f:
    print(f.read())


# ===== 4. Serializing a Record With json.dump() =====
# Save one supply record, stored as a dict, to a file called supply.json.
print('----- 4. Serializing a Record With json.dump() -----')
# TODO: import json
# TODO: create a dict called supply: name, count and department
# TODO: use "Stapler", 12 and "Office"
# TODO: open "supply.json" in write mode; save the dict with json.dump()


# ===== 5. Deserializing It Back With json.load() =====
# Load supply.json back into Python and check that it is a real dict again.
print('----- 5. Deserializing It Back With json.load() -----')
# TODO: import json
# TODO: open "supply.json"; read it into supply with json.load()
# TODO: print supply["name"], then print type(supply)

# PREDICT before you run: Dump a tuple to JSON and load it back. What type?
# Your answer:
#
