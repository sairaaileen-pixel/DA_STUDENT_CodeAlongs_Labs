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
    # Assign `comparisons` to 0
     comparisons = 0
    # Loop over `records`; add 1 to `comparisons` for every row
     for record in records:
         comparisons += 1
         if record[0] == tap_id:
           return comparisons
    # Inside the loop, return `comparisons` when row[0] == tap_id

    # After the loop, return `comparisons`
     return comparisons
    

print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Output: 
# comparisons to find T001: 1
# comparisons to find T040: 40
# comparisons to find T999: 40

# Step 1, answer 1: 
# Prediction: 
# T001:1
# T040: 40
# T999: 40
   
# Step 1, answer 2:
# We should plan around T999 because it represents the worst-case scenario. 
# It requires a full linear scan of every record and still fails to find the item. 
# As the dataset size grows, the cost of the scan scales linearly.


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    # Print "rows:", `size`, "| worst-case comparisons:", `worst`
    print("rows:", size, "| worst-case comparisons:", worst )
# Assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
pairs = 0
for  tap in taps:
    for pair in taps: 
# Add 1 to `pairs` in the inner loop
        pairs += 1
# Print len(taps) and `pairs`
print("rows:", len(taps),"| pair loop comparisons:", pairs)
     
# Assign `big` to len(taps) * 10
big = len(taps) * 10
# Print the scan's worst case and the pair loop's count on `big` rows
print("rows:", big, "| scan worst-case comparisons:", big)
print("rows:", big, "| pair loop comparisons:", big * big)

# --- EXCEEDING EXPECTATIONS: Doubled Data Test ---

# Prediction: 
#1: scan_for "T999", doubled: 80 (because of linear scan)
#2: scan_for "T001", doubled: 1 (stil 1 because is the first item)

doubled = taps + taps

print("rows:", len(doubled), "| worst-case scan (T999):", scan_for("T999", doubled))
print("rows:", len(doubled), "| best-case scan (T001):", scan_for("T001", doubled))

# Output:
# rows: 80 | worst-case scan (T999): 80
# rows: 80 | best-case scan (T001): 1



# Step 2, answer 1:
# Arithmetic: Scan at 5=5, 10=10, 20=20, 40=40.
# Pair loop on 40 rows = 40 * 40 = 1600. 
# Scan on 400 rows = 400. Pair loop on 400 rows = 400 * 400 = 160,000.

# Step 2, answer 2:
# The linear scan grows in direct proportion to the input size (linear growth).
# The pair loop grows quadratically.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# Assign `card_ids` to an empty list (each card, first-seen order)
card_ids = []
# Assign `tap_counts` to an empty list (the count for card_ids[i])
tap_counts = []
# Assign `comparisons` to 0
comparisons = 0
# Loop over `taps`; assign `card` to row[1] and `found` to False
for row in taps:
    card = row[1]
    found = False

# Inside it, loop over range(len(card_ids)); add 1 to `comparisons`
    for i in range(len(card_ids)):
        comparisons += 1
# If card_ids[i] == card, add 1 to tap_counts[i], set found, break
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
# After the inner loop, if not found, append `card` and 1 to the lists
    if not found:
            card_ids.append(card)
            tap_counts.append(1)

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# I expect comparisons higher than 40.
# Step 3, answer 2:
# The real count is 115 comparisions.
# It is higher than the number of rows because as more distint cards are discovered (12), later rows require checking multiple existing list items. 




# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# Assign `taps_by_card` to an empty dict (card ID: tap count)
taps_by_card = {}
# Assign `lookups` to 0
lookups = 0
#Loop over `taps`; add 1 to `lookups`
for row in taps:
    lookups += 1
# Add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
    card = row[1]
    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1
# Assign `stations` to set(); loop over `taps` and .add() row[2]
        stations = set()
for row in taps:
        stations.add(row[2])
# Assign `repeat_riders` to 0
repeat_riders = 0
# Loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1
for card in taps_by_card:
    if taps_by_card[card] > 1:
        repeat_riders +=1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# Lookups equal 40 (one per row in the dataset) because of O(1) access.

# Step 4, answer 2:
# Parallel lists slow down as data grows because they have to scan through items, while dictionaries stay fast with constant-time lookups (O(1)).

# Step 4, answer 3:
# - Dictionary job: Maps card IDs to their total tap counts, finding what it needs instantly via hash keys (O(1)).
# - Set job: Collects unique station names and automatically discards duplicates.
# - List cost for stations: Using a standard list would have cost us an O(n) membership check (`in`) for every single row to manually search and prevent duplicate stations, making it much slower.

# Step 4, answer 4:
# Card C001 (which has 6 taps) explains the gap between total distinct cards and repeat riders, because riders with more than one tap count toward repeat riders.


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# Replace each None with your Day 2 value; keep `stations` a set

summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": sorted(stations),
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")
# run the file and answer below before you change anything
# then put # in front of the next two lines so Step 6 can run
for key in summary: print(key, type(summary[key]))
# text = json.dumps(summary, indent=2)
# print(text)

# Step 5, answer 1:
# TypeError: Object of type set is not JSON serializable

# Step 5, answer 2:
# The key that is causing the error is the "stations" key, because a JSON file does not have a native data type for Python sets.

# Step 5, answer 3:
# Yes, "about to serialize" printed first. That tells us code runs from top to bottom.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# Assign summary["stations"] to a type JSON can hold; keep the key

#  json.dump() `summary` into a with open("tap_summary.json", "w")
with open("tap_summary.json", "w") as outfile:
    json.dump(summary, outfile, indent=2)

# Replace None with json.load() of "tap_summary.json"
with open("tap_summary.json", "r") as f:
 reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
# Yes, the overnight job can pull an individual card's count straight from this file without needing the raw log. We know this because `taps_by_card` survived the save-and-reload completely intact as a dictionary, meaning all the card totals are ready to look up right away.
# Step 6, answer 2:
# The dictionary survived the round trip unchanged, but the set came back as a list.
