#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `records`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return `comparisons` when row[0] == tap_id
    # TODO: after the loop, return `comparisons`
    pass


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
#
# Step 1, answer 2:
#


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    # TODO: print "rows:", `size`, "| worst-case comparisons:", `worst`
# TODO: assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
# TODO: add 1 to `pairs` in the inner loop
# TODO: print len(taps) and `pairs`
# TODO: assign `big` to len(taps) * 10
# TODO: print the scan's worst case and the pair loop's count on `big` rows

# Step 2, answer 1:
#
# Step 2, answer 2:
#


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# TODO: assign `card_ids` to an empty list (each card, first-seen order)
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
# TODO: assign `comparisons` to 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
# TODO: inside it, loop over range(len(card_ids)); add 1 to `comparisons`
# TODO: if card_ids[i] == card, add 1 to tap_counts[i], set found, break
# TODO: after the inner loop, if not found, append `card` and 1 to the lists

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
# TODO: assign `lookups` to 0
# TODO: loop over `taps`; add 1 to `lookups`
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
# TODO: assign `repeat_riders` to 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
# Step 4, answer 4:
#


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": None,
    "distinct_cards": None,
    "stations": None,
    "taps_by_card": None,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
text = json.dumps(summary, indent=2)
print(text)

# Step 5, answer 1:
#
# Step 5, answer 2:
#
# Step 5, answer 3:
#


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
# TODO: replace None with json.load() of "tap_summary.json"
reloaded = None

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
#
# Step 6, answer 2:
#
