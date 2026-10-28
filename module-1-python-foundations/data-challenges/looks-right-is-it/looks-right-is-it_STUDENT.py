#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, parts[2])
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Step 1, answer 1:
#
# Step 1, answer 2:
#
# Step 1, answer 3:
#


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


staff = ["E101", "E102", "E103", "E106", "E105"]
for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#


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

total = 0
for emp in employee_ids:
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Step 3, answer 1:
#
# Step 3, answer 2:
#
# Step 3, answer 3:
#


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours >= 40:
        return hours * rate * 1.5
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
    if total >= 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
