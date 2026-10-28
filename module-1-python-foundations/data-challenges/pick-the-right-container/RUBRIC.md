# Rubric: Pick the Right Container

**What you're graded on:** your one `.py` file, with Day 1 to Day 3 code and every written answer, submitted at the end of Day 3.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
4 skills x 4 points = **16 points at Meets**, more with any Exceeds earned.

## Algorithmic Complexity (Big-O) (`algorithmic-complexity-big-o`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus runs `scan_for()` on a doubled list and shows the count follows the predicted pattern. |
| **Meets** | 4 | Step 2 predicts every count with arithmetic, and Step 4 finishes "As the Input Size grows..." for both containers. |
| **Approaching** | 2 | Counts are predicted with no arithmetic, or a growth sentence names no measured count. |
| **Below Expectations** | 1 | No counts are predicted before running, or the 400-row costs are missing. |

## Control Flow & Loops (`control-flow-loops`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus code checks that every card has the same count in both tallies. |
| **Meets** | 4 | `scan_for()` returns the moment it matches, and Steps 3 and 4 give the same count for every card. |
| **Approaching** | 2 | Both tallies run but disagree on a card, or `scan_for()` counts only on a match. |
| **Below Expectations** | 1 | `scan_for()` or the Step 3 loop inside a loop is missing or does not run. |

## AI Output Validation (`ai-output-validation`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus records one AI answer that was wrong or incomplete and names exactly what was off. |
| **Meets** | 4 | Step 5 explains the broken key in your own words, and each quoted AI answer has a written check. |
| **Approaching** | 2 | The Step 5 explanation is pasted or reworded from AI, or an AI answer is quoted with no check. |
| **Below Expectations** | 1 | Step 5 answer 1 has no error message, or Step 6 deletes the `stations` key instead of converting it. |

## Data Structures Selection (`data-structures-selection`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus names one case where the parallel lists would be the better choice, and why. |
| **Meets** | 4 | Step 4 answer 3 names each container's job, how it finds what it needs, and what a list would cost. |
| **Approaching** | 2 | Step 4 answer 3 names the containers but not their jobs, or skips what a list would cost. |
| **Below Expectations** | 1 | `taps_by_card` or `stations` is missing, or `stations` is built as a list. |
