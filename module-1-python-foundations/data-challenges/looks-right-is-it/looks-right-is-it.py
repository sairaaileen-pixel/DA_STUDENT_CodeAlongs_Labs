#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# What does one row represent?
# One employee's work log for a single day (employee_id,name,day,hours,rate).

# Which fields hold numbers, and which hold text?
# - employee_id, name, and day are text (string).
# - hours whole numbers (integer).
# - rate decimal numbers (float).

# What already looks wrong, missing or inconsistent?
# Me and my group did not find something wrong with the dataset at first sight.


# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    # print(repr(hours))  # temporary debug print
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Exceeds: Print-based test call for Step 1 fix (fails before fix, passes after)
rosa_hours = weekly_hours(lines, "E101")
if rosa_hours == 40:
    print("PASS: weekly_hours for E101 is 40")
else:
    print("FAIL: expected 40 for E101, got", rosa_hours)

# Exceeds: Step 1 test call — fails before fix (TypeError on 'Mon' + 0), passes after (returns 40)

assert weekly_hours(lines, "E101") == 40, "Step 1 failed: expected 40 hours for E101"

# Step 1, answer 1:
# Rosa's weekly hours (E101) by hand: 8 * 5 = 40 hours.

# Step 1, answer 2:
# - The last line of a traceback shows the exception type and message explaining why Python stopped.
# - Each block above it shows a file, line number, function name, and code line in the call chain (reading bottom-up traces from where Python gave up back to callers).
# - Learned from Day 10 traceback notes and reading call stacks bottom-up.

# Step 1, answer 3:
# The traceback ended inside add_hours() on `return total + hours` (TypeError), while the real bug was in weekly_hours() reading `parts[2]` (the day column as a string) instead of `int(parts[3])` (the hours column as an integer).


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)

def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = []
for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)


# Exceeds: Warn if staff count differs from expected 5 employees

if len(staff) != 5:
    print("WARNING: expected 5 employees, found", len(staff))

print("employees in the file:", len(staff))

print("staff IDs:", staff) # temporary debug print

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1:
# Employees counted by eye in the CSV: 5 (E101, E102, E103, E104, E105).

# Step 2, answer 2:
# 3 lines printed before the crash (E101, E102, E103), and it stopped on E106 with ZeroDivisionError.

# Step 2, answer 3:
# The bug lived above the division line in the hand-typed `staff` list ("E106" instead of "E104")/ line 84


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

for emp in employee_ids:
    total = 0
    # print("starting", emp, "total is", total)
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Exceeds: Test call for Step 3 fix (fails before fix because total accumulates across employees)
assert weekly_hours(lines, "E103") == 32, "Expected Mei (E103) weekly hours to be 32"

# Step 3, answer 1:
# Hand-counted hours: Rosa (E101) = 40 (8*5); Mei (E103) = 32 (6+7+8+6+5).

# Step 3, answer 2:
# Before each employee's count, `total` held the running sum from previous employees (0, 40, 86, 118, 156) because `total = 0` was placed outside the outer `for emp in employee_ids:` loop instead of inside it.

# Step 3, answer 3:
# Rosa is first so `total` starts at 0 and reaches 40; Priya is last so `total` keeps accumulating every employee's hours up to 200 (the whole staff's weekly total).


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours > 40:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1:
# Hand worked weekly pay (all 5 employees for Exceeds):
# - Rosa Alvarez (E101, 40 hrs @ $24.00): 40 * 24.00 = $960.00
# - Darnell Pierce (E102, 46 hrs @ $31.50): 40 * 31.50 + 6 * 31.50 * 1.5 = $1,543.50
# - Mei Tanaka (E103, 32 hrs @ $28.00): 32 * 28.00 = $896.00
# - Samuel Okafor (E104, 38 hrs @ $22.00): 38 * 22.00 = $836.00
# - Priya Raman (E105, 44 hrs @ $35.00): 40 * 35.00 + 4 * 35.00 * 1.5 = $1,610.00

# Step 4, answer 2:
# I found 2 logic bugs:
# 1) Overtime-on-all-hours bug on `return hours * rate * 1.5` (and `if hours >= 40:`) inside `weekly_pay(hours, rate)`:
# Multiplied all hours by 1.5x instead of paying straight time on the first 40 hours and 1.5x only on hours over 40.
# Fix: Changed `if hours >= 40: return hours * rate * 1.5` to `if hours > 40: return (40 * rate) + ((hours - 40) * rate * 1.5)`.
# 2) Overtime-boundary (`>=` vs `>`) bug on `if total >= 40:` inside the `for emp in employee_ids:` loop:
# Counted 40 hours as overtime instead of requiring strictly more than 40 hours (`total > 40`).
# Fix: Changed `if total >= 40:` to `if total > 40:` on the line right before `owed_overtime = owed_overtime + 1`.
# Step 4, answer 3:
# Rosa is the only employee with exactly 40 hours, which is the only case where `>= 40` differs from `> 40` (under 40 is False for both, over 40 is True for both). She only catches the `>= 40` boundary bug because she has no overtime hours to trigger the `hours * rate * 1.5` formula bug.