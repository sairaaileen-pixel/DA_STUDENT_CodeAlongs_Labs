#!/usr/bin/env python3
"""Data Challenge: Trace the Path
GitBook Quest 1.1: Trace the Path

HOW TO RUN
    Open a terminal in the folder that holds data/ and run:
        python3 trace-the-path_STUDENT.py
    If this file sits one folder below data/, run it from the folder
    above instead:  python3 trace-the-path/trace-the-path_STUDENT.py
    Or make it executable once:
        chmod +x trace-the-path_STUDENT.py
    and from then on run it directly:
        ./trace-the-path_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

THE DATA      data/volunteer_shifts.txt

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (DataChallengeOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

AI TOOLKIT: prompts to try and how to check them are in
DataChallengeOverview&Steps.md.

SUBMIT
    Commit this file (you may rename it trace-the-path.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
    Submit once, at the end of Day 2. Keep every day's work in here.
"""

############################################################################
#  THE DATA: open data/volunteer_shifts.txt and look at it
#  before you write any code. The worksheet's "The Data" section
#  shows how to load it.
############################################################################

# 1. What does one row represent?
# Your answer:
#
#

# 2. Which fields hold numbers, and which hold text?
# Your answer:
#
#

# 3. What already looks wrong, missing or inconsistent?
# Your answer:
#
#

############################################################################
#  DAY 1
############################################################################

# ===== Step 1: Count the Shifts of 4+ Hours, Prediction First =====
# The coordinator counts any shift of 4 hours or more as a long shift.
#
# 1. Research .split(",") as a team. It is new, and the line that pulls out
#    hours uses it. Look it up, then run it on one line of this file and
#    print what comes back. Under the "# Your answer:" line below, type 2-3
#    bullets: what .split() hands back, what the "," controls, and where you
#    found that out.
# 2. Predict the count by reading the file, not the code. You opened
#    data/volunteer_shifts.txt above and it holds 12 shift rows. Read the
#    third field on each row and count the rows where it is 4 or more. Write
#    that one number in a comment at the top of this step, before you run a
#    single line.
# 3. Write the test for a long shift in the first TODO. "4 hours or more" is
#    the rule, word for word.
# 4. Write the counting line in the second TODO, moving long_shifts on by
#    one.
# 5. Run it, and compare the printed count against the number in your
#    comment.
#
# If the two differ, say which line you mis-read. Do not edit the
# prediction.

with open("data/volunteer_shifts.txt") as f:
    shifts = [line for line in f.read().splitlines()
              if line and not line.startswith("#")]

long_shifts = 0
for shift in shifts:
    hours = int(shift.split(",")[2])
    # TODO: write the test for a long shift. The coordinator counts a
    #       shift of 4 hours or more.
    if None:
        # TODO: this is the counting line. Move long_shifts on by one.
        long_shifts = None

print("shifts of 4+ hours:", long_shifts)

# Your answer:
#
#

# ===== Step 2: Total the Week's Hours, Printing the Running Total Each Pass =====
# You already wrote a loop that counts. This one adds up instead, and you
# watch the variable move as it goes.
#
# 1. Predict two numbers in a comment, both worked out by hand off the file.
#    The week's total hours: add the third field down all 12 rows. The
#    number of lines that will print: the loop prints once per row it
#    visits, so count the rows.
# 2. Add this shift's hours onto the running total in the first TODO.
#    Everything that came out of shift.split(",") is a string, so something
#    has to convert it.
# 3. Print one line per pass in the second TODO: the day, the volunteer, and
#    the total so far.
# 4. Run it, and check the line count against your prediction first, then
#    the final total.
#
# That printed line per pass is a tracing tool, not decoration.

total = 0
for shift in shifts:
    volunteer, day, hours = shift.split(",")
    # TODO: add this shift's hours onto the running total. Mind the
    #       type: everything that came out of that split is a string.
    total = None
    # TODO: print one line per pass: the day, the volunteer, and the
    #       total so far. This printed line IS the tracing tool.
    print(day, volunteer, "| running total:", None)

print("total hours logged this week:", total)

# ----- Share Out: Day 1 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your two predictions, exactly as you first wrote them. Un-edited. Say
#   whether each one was right.
# - What you mis-traced, if one was wrong. A condition read backwards, a
#   variable you forgot updates every pass, a loop you thought ran one more
#   time than it does.
# - Your observations on the data file, from the three questions you
#   answered before writing any code. Say whether anything turned out
#   different from what you assumed.
# - How you traced it. Did you print a line per pass, or hold the loop in
#   your head? Say which you would use on 430 rows.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

############################################################################
#  DAY 2
############################################################################

# ===== Step 3: Count Every Volunteer-Weekday Pair, Predicted as a Multiplication =====
# The coordinator wants a grid of every volunteer against every weekday, to
# spot the slots nobody covered. First, how big is that grid?
#
# 1. Predict the number of cells as a multiplication, not a guess. Count the
#    distinct volunteer names in the file, count the distinct weekdays, and
#    multiply the two. Write it in a comment as <volunteers> x <days> =
#    <cells> before you write or run anything.
# 2. Collect the distinct volunteers in the first if TODO: one entry per
#    volunteer, no repeats.
# 3. Collect the distinct weekdays in the second if TODO, the same way.
# 4. Write the inner loop header so it runs once per weekday, for every
#    volunteer.
# 5. Run it, and compare checks against the multiplication you wrote.
#
# If your prediction was a number of records rather than a number of pairs,
# that gap is the thing to bring to the shareout.

volunteers = []
days = []
for shift in shifts:
    volunteer, day, hours = shift.split(",")
    # TODO: only append a volunteer this list does not already have.
    if None:
        volunteers.append(volunteer)
    # TODO: the same test again, for the day.
    if None:
        days.append(day)

checks = 0
for volunteer in volunteers:
    # TODO: the inner loop. One pass per weekday, for each volunteer.
    for day in None:
        checks = checks + 1

print(len(volunteers), "volunteers x", len(days), "days =", checks)

# ===== Step 4: Fix the Off-by-One and Print the Row It Never Reached =====
# An earlier version of this report was quietly missing a volunteer's last
# shift, and nothing ever errored. The broken loop is handed to you in the
# skeleton.
#
# 1. Predict from the code this time, not the file. Read range(len(shifts) -
#    1) and work out the rule: what is the first value of i, and what is the
#    last? Then write two things in a comment: how many rows the buggy loop
#    visits, and which row it never reaches.
# 2. Write the loop header that visits every row. Only the range changes;
#    the body below it is already right.
# 3. Print the row the broken loop never reached, reaching into shifts by
#    position rather than retyping the row by hand.
# 4. Run it, and compare all three counts (rows in the file, buggy visits,
#    fixed visits) against your prediction.
#
# Both loops run clean, with no traceback from either. Only one of them is
# right.

buggy_seen = 0
for i in range(len(shifts) - 1):
    buggy_seen = buggy_seen + 1

fixed_seen = 0
# TODO: write the loop header that visits EVERY row, not all but one.
#       The body below is already correct. Only the range changes.
for i in None:
    fixed_seen = fixed_seen + 1

print("rows in the file:   ", len(shifts))
print("buggy loop visited: ", buggy_seen)
print("fixed loop visited: ", fixed_seen)
# TODO: print the one row the buggy loop never reached. Reach into the
#       list by position; do not retype the row by hand.
print("the row it never saw:", None)

# ----- Share Out: Day 2 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your pair prediction, stated as a multiplication. Say whether you
#   predicted a number of rows or a number of pairs, and which one the code
#   actually counted.
# - How you found the off-by-one. By reading the range, or by noticing the
#   count was short? Say which of those you would still trust on a file too
#   long to eyeball.
# - Anything AI told you that your own counts contradicted. If you asked it
#   about range(), say whether it gave you a source and whether the source
#   said what it claimed.
# - One thing you would do differently starting these two days over. If you
#   are still holding a question, bring the question. You will not be the
#   only one.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
