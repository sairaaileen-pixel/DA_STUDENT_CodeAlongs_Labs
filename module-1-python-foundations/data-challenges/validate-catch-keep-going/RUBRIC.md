# Rubric: Validate, Catch, Keep Going

**What you're graded on:** your one `.py` file, with Day 1 and Day 2 code and every written answer, submitted at the end of Day 2.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

## Functions & Modular Programming (`functions-modular-programming`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus adds a third check function for another field and calls it in the Step 4 loop. |
| **Meets** | 4 | `validate_request()` and `check_days_open()` each return a verdict and a reason, and the Step 4 loop calls both. |
| **Approaching** | 2 | Both functions run, but one returns only `True` or `False`, or prints its reason instead of returning it. |
| **Below Expectations** | 1 | `validate_request()` or `check_days_open()` is missing or does not run. |

## Attention to Detail (`attention-to-detail`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus adds code that prints a warning when `counted` plus `skipped` is not the row count. |
| **Meets** | 4 | Step 2 answer 2 names the rows wrongly passed, and Step 4 shows `counted` plus `skipped` equals 15. |
| **Approaching** | 2 | Only one of the two is there: rows named in Step 2, or the sum shown in Step 4. |
| **Below Expectations** | 1 | Neither is there: Step 2 answer 2 is blank and Step 4 shows no sum. |

## Problem Solving (`problem-solving`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus tests one more bad `days_open` value and predicts which tool catches it before running. |
| **Meets** | 4 | Step 3 quotes the traceback's last line, and Step 4 says which tool, `if` or `try`, catches each bad value. |
| **Approaching** | 2 | Step 3 paraphrases the traceback, or Step 4 names a tool for only one of the two values. |
| **Below Expectations** | 1 | Step 3 has no traceback, or `check_days_open()` uses a bare `except:`. |
