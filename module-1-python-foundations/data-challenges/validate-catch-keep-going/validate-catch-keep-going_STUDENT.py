#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# Assign `EXPECTED_FIELDS` to 5
EXPECTED_FIELDS = 5
# Assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]

def validate_request(row):
    # Assign `fields` to `row` split on commas
    fields = row.split(",")
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    # Unpack `fields` into the five names in the CSV header
    request_id,complaint_type,borough,days_open,status = fields
    # If `borough` is empty, return False and "borough is empty"
    if borough == "":
        return False, "borough is empty"
    # If `status` is not in ALLOWED_STATUS, return False and a reason
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    # Make that reason "status not allowed: " plus `status`
    # Return True and "ok"

    return True, "ok"



print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# The file has 15 rows of 311 complaints. Each line has info like an ID, what the complaint
# is, which borough it's from, how many days it's been open, and its status. Looking at the file 
# with my partner, we noticed some rows are missing a borough, some have bad statuses like "Escalated", 
# and one row is missing a whole field.

# Step 1, answer 2:
# We unpack the two returned values into two variables on one line like `ok, reason = validate_request(row)`.
# Under the hood, Python is actually just handing back a single tuple (like `(True, "ok")`) with both items inside.



# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# Assign `valid` to 0
valid = 0
# Loop over `rows`; unpack validate_request(row) into ok, reason
for row in rows:
    ok, reason = validate_request(row)
# If `ok`, add 1 to `valid`
    if ok:
        valid += 1
# Else print row.split(",")[0], "REJECTED -" and `reason`
    else:
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1: 
# 3 rows fail: SR-1004 because its borough is empty, SR-1009 because its status ("Escalated") 
# is not in the allowed list, and SR-1011 because it has 4 fields instead of the expected 5. 
# (We also checked the last row of the file, SR-1015, and its status is a plain "Open", so it passes).
#

# Step 2, answer 2:
# Rows SR-1007 ("3 days") and SR-1013 ("-3") slipped through because our validator only checks 
# structure and status names, not whether the days column is a proper positive number.


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# Assign `total_days` and `counted` to 0
#total_days = 0
#counted = 0
# Loop over `rows`; `continue` past any row validate_request() rejects
#for row in rows:
#    ok, reason = validate_request(row)
#    if not ok:
#        continue
# Assign `days_open` to int() of the row's fourth field
#    days_open = int(row.split(",")[3])
# Add `days_open` to `total_days` and 1 to `counted`
#    total_days += days_open
#    counted += 1
# Print the row's ID, "days open:" and `days_open`
#    print(row.split(",")[0], "days open:", days_open)
# After your answers, comment out this step so Step 4 can run

#print("average days open:", total_days / counted)

# Step 3, answer 1:
# It prints 6 lines before crashing on row SR-1007 because `int()` can't convert letters like "3 days".

# Step 3, answer 2:
# ValueError: invalid literal for int() with base 10: '3 days' 
# (5 rows were counted before it crashed).

# Step 3, answer 3:
# The program crashes immediately and stops running, so the remaining rows are never reached.


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    # In a try, assign `days` to int(value)
    try:
        days = int(value)
    # In except ValueError, return False and a reason
    except ValueError:
        return False, "days_open is not a number: " + value
    # Make that reason "days_open is not a number: " plus `value`
    # If `days` is below 0, return False and a reason
    if days < 0:
        return False, "days_open is negative: " + value
    # Make that reason "days_open is negative: " plus `value`
    # Return True and "ok"
    return True, "ok"
    


# Assign `total_days`, `counted` and `skipped` to 0
total_days = 0
counted = 0
skipped = 0
# Loop over `rows`; unpack validate_request(row) into ok, reason
for row in rows:
    ok, reason = validate_request(row) 
# If ok, unpack check_days_open() of the fourth field into ok, reason
    if ok:
        ok, reason = check_days_open(row.split(",")[3])
# If still ok, add the days to `total_days` and 1 to `counted`
    if ok:
       days_val = int(row.split(",")[3])
       total_days += days_val
       counted += 1
# Else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
    else:
       skipped += 1
       print(row.split(",")[0], "SKIPPED -", reason)

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
# 5 rows are skipped total (the 3 bad ones from Day 1: SR-1004, SR-1009, SR-1011, plus the two that slipped through: SR-1007 and SR-1013).

# Step 4, answer 2:
# "3 days" triggers `except ValueError` because `int()` fails on text. "-3" passes `int()` but fails the `days < 0` rule. They cannot swap roles.


# Step 4, answer 3:
# Yes: 10 counted + 5 skipped = 15 total rows.