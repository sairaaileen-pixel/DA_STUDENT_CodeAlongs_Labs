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
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `parts` to `record` split on commas
    # TODO: return False, "wrong field count" if `parts` lacks 5 fields
    # TODO: return False, "missing category" if parts[2].strip() is ""
    # TODO: in a try, call float(parts[3])
    # TODO: in except ValueError, return False, "pounds is not a number"
    # TODO: return True and ""
    pass


# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
# TODO: loop over `records`; unpack validate_donation(record) as ok, reason
# TODO: if `ok`, append `record` to `valid`
# TODO: else print "rejected", the record's ID plus ":", and `reason`
print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
#
# Step 1, answer 2:
#


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0
    # TODO: loop over `valid_records`; split each record on commas into `parts`
    # TODO: assign `category` to parts[2], `pounds` to float(parts[3])
    # TODO: if `category` is not in `by_category`, add an entry for it
    # TODO: start that entry as {"donations": 0, "pounds": 0.0}
    # TODO: add 1 to its "donations" and `pounds` to its "pounds"
    # TODO: add `pounds` to `total_pounds`
    # TODO: return a dict of "records", "total_pounds" and "by_category"
    pass


# TODO: assign `summary` to summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
#


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: in a with open(path, "w") block, json.dump `summary`, indent=2
    # TODO: return `path`
    pass


def run_pipeline(in_path, out_path, summarize):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: assign `kept` to [] and loop over read_donations(in_path)
    # TODO: append each record that validate_donation() passes to `kept`
    # TODO: return export_summary() of summarize(kept) and `out_path`
    pass


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    # TODO: return the same dict shape, with "by_day" keyed by parts[4]
    pass


# TODO: call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# TODO: replace None with json.load() of "donation_summary.json"
reloaded = None

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
#
# Step 4, answer 2:
#
