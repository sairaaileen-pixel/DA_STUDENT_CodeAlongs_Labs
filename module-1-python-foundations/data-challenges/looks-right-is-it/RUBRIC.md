# Rubric: Looks Right. Is It?

**What you're graded on:** your one `.py` file, with Day 1 and Day 2 fixes and every written answer, submitted at the end of Day 2.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

## Attention to Detail (`attention-to-detail`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus works out all five employees' pay by hand, not just the three the steps name. |
| **Meets** | 4 | Every step has a hand-worked number written before the run, and each fix is re-checked against that number. |
| **Approaching** | 2 | At least one step has no hand-worked number, or a fix is never re-checked against one. |
| **Below Expectations** | 1 | No step has a hand-worked number. |

## Control Flow & Loops (`control-flow-loops`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus adds a check that prints a warning when `len(staff)` differs from the employees in the file. |
| **Meets** | 4 | `staff` is built by a loop over `lines[1:]`, and every employee's Step 3 total starts at 0. |
| **Approaching** | 2 | One of the two loops is fixed, and the other still gives a wrong count or total. |
| **Below Expectations** | 1 | Neither loop is fixed, or Step 2 skips the crash with `continue` and drops an employee. |

## Problem Solving (`problem-solving`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus writes one test call per bug that fails before the fix and passes after. |
| **Meets** | 4 | Steps 1 and 2 name the traceback's line and the real bug line, and Step 4 gives both bugs' lines. |
| **Approaching** | 2 | Fixes run, but a step names only the traceback's line, or Step 4 finds one of the two bugs. |
| **Below Expectations** | 1 | No written answer names a bug's line, only what changed in the output. |
