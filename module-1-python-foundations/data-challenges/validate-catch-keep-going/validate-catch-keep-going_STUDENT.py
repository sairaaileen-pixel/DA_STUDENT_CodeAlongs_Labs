#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]


def validate_request(row):
    # TODO: assign `fields` to `row` split on commas
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    # TODO: unpack `fields` into the five names in the CSV header
    # TODO: if `borough` is empty, return False and "borough is empty"
    # TODO: if `status` is not in ALLOWED_STATUS, return False and a reason
    # TODO: make that reason "status not allowed: " plus `status`
    # TODO: return True and "ok"
    pass


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
#
# Step 1, answer 2:
#


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# TODO: assign `valid` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if `ok`, add 1 to `valid`
# TODO: else print row.split(",")[0], "REJECTED -" and `reason`

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
#
# Step 2, answer 2:
#


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# TODO: assign `total_days` and `counted` to 0
# TODO: loop over `rows`; `continue` past any row validate_request() rejects
# TODO: assign `days_open` to int() of the row's fourth field
# TODO: add `days_open` to `total_days` and 1 to `counted`
# TODO: print the row's ID, "days open:" and `days_open`
# TODO: after your answers, comment out this step so Step 4 can run

print("average days open:", total_days / counted)

# Step 3, answer 1:
#
# Step 3, answer 2:
#
# Step 3, answer 3:
#


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    # TODO: in a try, assign `days` to int(value)
    # TODO: in except ValueError, return False and a reason
    # TODO: make that reason "days_open is not a number: " plus `value`
    # TODO: if `days` is below 0, return False and a reason
    # TODO: make that reason "days_open is negative: " plus `value`
    # TODO: return True and "ok"
    pass


# TODO: assign `total_days`, `counted` and `skipped` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
# TODO: if still ok, add the days to `total_days` and 1 to `counted`
# TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
