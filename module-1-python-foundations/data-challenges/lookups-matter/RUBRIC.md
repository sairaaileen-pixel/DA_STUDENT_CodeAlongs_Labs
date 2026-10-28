# Rubric: Lookups Matter

**What you're graded on:** your one `.py` file, with the day's code, `ai_claim`, `verdict` and every written answer, submitted at the end of the day.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
4 skills x 4 points = **16 points at Meets**, more with any Exceeds earned.

## Algorithmic Complexity, Big-O (`algorithmic-complexity-big-o`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus predicts how the pay-off swipe would move with twice the members, and explains why. |
| **Meets** | 4 | The Step 3 race includes the build cost, and `verdict` names `O(n)` and `O(1) Average-Case` with one of your counts. |
| **Approaching** | 2 | The race runs, but the dict total leaves out the build cost, or `verdict` names labels with no count. |
| **Below Expectations** | 1 | `find_linear()` or the Step 3 race does not run, or `verdict` is missing. |

## Critical Thinking (`critical-thinking`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus a comment explains why any wrong prediction was wrong, naming the rule it missed. |
| **Meets** | 4 | Steps 1 to 3 each have answer 1 written before the run, with the reasoning behind each predicted count. |
| **Approaching** | 2 | Predictions are written with no reasoning, or one of the three steps has none. |
| **Below Expectations** | 1 | No step has a written prediction. |

## AI Output Validation (`ai-output-validation`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus `verdict` names what the speed-up depends on, using two of your three comparisons. |
| **Meets** | 4 | `ai_claim` is pasted word for word, and Step 4 checks it against all three comparisons and the build cost. |
| **Approaching** | 2 | The claim is pasted, but the check uses fewer than three comparisons or skips the build cost. |
| **Below Expectations** | 1 | `ai_claim` or `verdict` is still a placeholder, or the claim is never checked. |

## Data Structures Selection (`data-structures-selection`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus backs the list-wins morning with numbers: the build cost against that morning's swipe counts. |
| **Meets** | 4 | Step 3 explains why a dict keyed on `member_id` fits, quotes the pay-off swipe, and names a list-wins morning. |
| **Approaching** | 2 | Step 3 explains why the dict fits but quotes no swipe, or names no morning where a list wins. |
| **Below Expectations** | 1 | `members_by_id` is missing, or Step 3 answers 2 and 3 are blank. |
