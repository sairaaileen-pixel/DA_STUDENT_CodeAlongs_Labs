#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # Assign `comparisons` to 0
    comparisons =0
    # Loop over `members`; add 1 to `comparisons` for every row
    for row in members:
        comparisons += 1
    # Inside the loop, return row, comparisons on a member_id match
        if row["member_id"] == member_id:
            return row, comparisons
    # After the loop, return None, comparisons
    return None, comparisons 


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# Prediction: M1150 should take 150 comparisons
# Output: 
# members in the directory: 312
# found: Tomas Park at Eastside
# comparisons: 150

# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# Open CHECKINS_FILE in a with block as `f`
# Inside it, assign `swipes` to f.read().splitlines()
# Assign `linear_total` and `not_members` to 0
# Loop over `swipes`; call find_linear(members, member_id)
# Print the ID, the name or "NOT A MEMBER", and the comparisons
# Add each count to `linear_total`
# Add 1 to `not_members` for every swipe with no row

with open(CHECKINS_FILE) as f:
    swipes = f.read().splitlines()

linear_total = 0
not_members = 0

for member_id in swipes:
    row, comparisons = find_linear(members, member_id)
    if row:
        print(f"{member_id} | {row['name']} | comparisons: {comparisons}")
    else:
        print(f"{member_id} | NOT A MEMBER | comparisons: {comparisons}")
        not_members += 1
    linear_total += comparisons


print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)
     

# Step 2, answer 1:
# predictions based on the ID-minus-1000 rule: Swipe 1 = 4, Swipe 2 = 12, Swipe 3 = 23, Sum = 39, Non-member = 312.
# Step 2, answer 2:
# The non-member swipes cost the most because linear search has a worst-case time complexity of O(n) (must check all 312 rows).
# Step 2, answer 3 (Exceeds - prediction check):
# Any difference between my ID-minus-1000 prediction and the actual comparison count came from assuming IDs always map straight to row index (ID - 1000) without checking actual file order or missing/non-member IDs.
# When an ID is not in member_directory.csv, the ID-minus-1000 rule does not apply—linear search has to scan all 312 rows before returning None.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# Assign `members_by_id` to an empty dict and `build_steps` to 0
# Loop over `members`; store each row under row["member_id"]
# Add 1 to `build_steps` for every row
# Write find_dict(members_by_id, member_id)
# Make find_dict() return members_by_id.get(member_id), 1
 
members_by_id = {}
build_steps = 0

for row in members:
    members_by_id[row["member_id"]] = row
    build_steps += 1

def find_dict(members_by_id, member_id):
    return members_by_id.get(member_id), 1
 

print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# Assign `linear_running` to 0 and `dict_running` to build_steps
linear_running = 0
dict_running = build_steps
# Assign `pays_off_at` to None and `
pays_off_at = None
swipe_number = 0
for member_id in swipes:
    # Add 1 to `swipe_number`\
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    # Add each search's count to its running total
    linear_running += linear_count
    dict_running += dict_count
    # Print swipe_number, the ID and both running totals
    print(f"swipe: {swipe_number} | member ID: {member_id} | linear so far: {linear_running} | dict so far: {dict_running}")
    # The first time dict_running < linear_running, set `pays_off_at`
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# Prediction: The dictionary starts behind because of the 312-step setup cost, 
# so it will pay off once a few slow list searches and non-member checks add up past 312.

# Step 3, answer 2:
# A dictionary works great for checking IDs because it looks up people instantly 
# instead of searching through a list one by one. The dictionary pulled ahead at swipe 6.

# Step 3, answer 3:
# A plain list is better on a slow morning with only a few swipes, 
# because you avoid the 312 step setup cost.
# For example, on a 5 swipe morning
# where linear searches only take 4 + 12 + 23 + 8 + 10 = 57 total steps,
# the plain list costs 57 steps while the dictionary costs 312 + 5 = 317 steps.

# Step 3, answer 4 (Exceeds - doubling members):
# If the member list doubles from 312 to 624 rows, build_steps doubles to 624 and non-member/worst-case linear scans can reach up to 624 steps.
# The pay-off swipe would likely move later because the dictionary starts 624 steps behind instead of 312—unless early swipes include several non-members or IDs near the end of the 624-row list that rack up huge linear counts quickly.

# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# Replace the text below with your AI's claim, word for word
ai_claim = "A dict lookup is roughly 10-50x faster than a linear search through a list of 312 rows."
print("AI CLAIM:", ai_claim)

# Unpack find_linear() for swipes[0] into `_, front_count`
_, front_count = find_linear(members, swipes[0])
#Unpack find_linear() for "M1313" into `_, absent_count`
_, absent_count = find_linear(members, "M1313")
# Assign `ratio` to round(linear_running / dict_running, 1)
ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# Replace the text below with your own verdict
verdict = "Mostly true for single lookups (especially missing IDs like M1313 at 1 vs 312 steps), but slightly high for the whole morning because the 312-step setup cost brings the real speedup to 8.8x."

print("VERDICT:", verdict)

# Step 4, answer 1:
# It matched the non-member swipe (1 vs. 312 steps, well past 10-50x), missed the front-of-file swipe (1 vs. 4 steps), and slightly overshot the whole morning (8.8x vs. 10-50x).
# Step 4, answer 2:
# No, it only measured the lookup itself and left out the 312-step build cost. When I pasted my totals back, it noted that including the 312-step setup brings the real whole-morning speedup down to 8.8x.
