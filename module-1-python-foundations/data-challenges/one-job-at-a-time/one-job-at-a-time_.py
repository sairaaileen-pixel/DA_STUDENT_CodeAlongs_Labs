#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    # Add a one-sentence docstring naming its one job
    """Given one record, this function decides whether it is usable and returns a verification verdict and a reason."""
    # Assign `parts` to `record` split on commas
    parts = record.split(",")
    # Return False, "wrong field count" if `parts` lacks 5 fields
    if len(parts) != 5:
       return (False, "wrong field count") 
    # Return False, "missing category" if parts[2].strip() is ""
    if parts[2].strip() == "":
      return (False, "missing category")
    # In a try, call float(parts[3])
    try: 
        float(parts[3])
    # In except ValueError, return False, "pounds is not a number"
    except ValueError:
        return (False,  "pounds is not a number")
    # Return True and ""
    return (True, "")
    


# Assign `records` to read_donations(DATA_FILE), `valid` to []
records = read_donations(DATA_FILE)
valid = []
# Loop over `records`; unpack validate_donation(record) as ok, reason
for record in records:
    ok, reason = validate_donation(record)
# If `ok`, append `record` to `valid`
    if ok:
        valid.append(record)
# Else print "rejected", the record's ID plus ":", and `reason`
    else:
        print("rejected", record.split(",")[0] + ":", reason)
        # print("rejected", record.split(",")[0] + ":", reason)
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
# Each record represents a pantry donation with ID, item, category, pounds, and date.
# Records like D009 have a missing category, and others like D013 have non-numeric pounds.
# And "D017" has only 4 fields instead of 5 because the pounds field is missing.

# Step 1, answer 2:
# Our validation function guarantees three things for kept records: exactly 5 fields,
# a non-empty category string, and a pounds value that can be successfully converted to a float.


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    # Add a one-sentence docstring naming its one job
     """Add up total pounds and donation counts per category and is not responsible for validating records.""" 
    # Assign `by_category` to {} and `total_pounds` to 0.0
     by_category = {}
     total_pounds = 0.0
    # Loop over `valid_records`; split each record on commas into `parts`
     for record in valid_records:
        parts = record.split(",")
    # Assign `category` to parts[2], `pounds` to float(parts[3])
        category = parts[2].strip()
        pounds = float(parts[3])
    # If `category` is not in `by_category`, add an entry for it
        if category not in by_category:   
    # Start that entry as {"donations": 0, "pounds": 0.0}
           by_category[category] =  {"donations": 0, "pounds": 0.0}
    # Add 1 to its "donations" and `pounds` to its "pounds"
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
    # Add `pounds` to `total_pounds`
        total_pounds += pounds
    # Return a dict of "records", "total_pounds" and "by_category"
     return {
        "records": len(valid_records), 
        "total_pounds": total_pounds,
        "by_category": by_category
    }


# Assign `summary` to summarize_donations(valid)
summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
# Category chosen: canned.
# Hand-count :
# D002 (18) + D007 (22) + D011 (16) + D015 (24) = 80.0 lbs across 4 valid donations.
# Note: D017 ("D017,corn,canned,2026-09-09") is rejected due to wrong field count, so its row is excluded.
# Comparison: My hand count of 80.0 lbs across 4 donations matches the printed line ("canned 4 donations, 80.0 lbs") exactly.


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    # Add a one-sentence docstring naming its one job
    """Export the summary dictionary to a JSON file."""
    # In a with open(path, "w") block, json.dump `summary`, indent=2
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    # Return `path`
    return path
    


def run_pipeline(in_path, out_path, summarize):
    # Add a one-sentence docstring naming its one job
    """Run the complete donation pipeline from raw file input to exported JSON summary."""
    # Assign `kept` to [] and loop over read_donations(in_path)
    kept = []
    for record in read_donations(in_path):
        ok, _ = validate_donation(record)
    # Append each record that validate_donation() passes to `kept`
        if ok:
            kept.append(record)
    # Return export_summary() of summarize(kept) and `out_path`
    summary_dict = summarize(kept)
    return export_summary(summary_dict, out_path)
    


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
# `print(len)` prints the function reference object (<built-in function len>), whereas
# `print(len("abc"))` calls the function with parentheses and returns the integer 3.

# Step 3, answer 2:
# None of the docstrings use "and" twice. Each docstring focuses on a single job with at most one "and".


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    # Add a one-sentence docstring naming its one job
    """Calculate total records, total pounds, and daily breakdown for valid donations."""
    # Return the same dict shape, with "by_day" keyed by parts[4]
    by_day = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        day = parts[4].strip()
        pounds = float(parts[3])
        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}
        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds
    return {
        "records": len(valid_records),
        "total_pounds": total_pounds,
        "by_day": by_day
    }

# Call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# Replace None with json.load() of "donation_summary.json"
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
# Zero other functions were edited for the swap. Because `run_pipeline` accepts `summarize`
# as a flexible parameter, swapping the summarizer required no changes to reading, validation, or export logic.
# Step 4, answer 2:
# Dates with 1 donation, match the dates of rejected rows D017, D009, and D013.
# A coordinator might misinterpret this dip as low donor turnout rather than realizing records were filtered out due to data errors.


# --Exeeds-- summarizer pounds per item.

def summarize_pounds_per_items(valid_records):
    """This function calculates the total pounds and donation counts per item, this function does not validate records"""
    pounds_per_item = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(",")
        item = parts[1].strip()
        pounds = float(parts[3])
        if item not in pounds_per_item:
            pounds_per_item[item] = {"donations": 0, "pounds": 0.0}
        pounds_per_item[item]["donations"] += 1
        pounds_per_item[item]["pounds"] += pounds
        total_pounds += pounds
    return { "records": len(valid_records),
                "total_pounds": total_pounds,
                "pounds_per_item": pounds_per_item
            }
run_pipeline(DATA_FILE, "donation_summary.json", summarize_pounds_per_items)
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for item, stats in sorted(reloaded["pounds_per_item"].items()):
    print(item, stats["donations"], "donations,", stats["pounds"], "lbs")
