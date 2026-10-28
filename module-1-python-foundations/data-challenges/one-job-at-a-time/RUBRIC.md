# Rubric: One Job at a Time

**What you're graded on:** your one `.py` file, with Day 1 and Day 2 code and every written answer, submitted at the end of Day 2.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

## Functions & Modular Programming (`functions-modular-programming`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus writes a third summarizer, like pounds per item, and swaps it in with no other edits. |
| **Meets** | 4 | `run_pipeline()` calls the summarizer through `summarize`, and swapping in `summarize_by_day()` edits no other function. |
| **Approaching** | 2 | The swap runs, but `run_pipeline()` names a summarizer inside it, or another function needed an edit. |
| **Below Expectations** | 1 | `run_pipeline()` or `summarize_by_day()` is missing or does not run. |

## Control Flow & Loops (`control-flow-loops`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus code checks that the category pounds add up to `total_pounds`. |
| **Meets** | 4 | `summarize_donations()` fills `by_category` and `total_pounds` in one loop, and Step 2 hand-checks one category's pounds. |
| **Approaching** | 2 | Totals print, but the data is looped more than once, or no category is hand-checked. |
| **Below Expectations** | 1 | `summarize_donations()` does not run, or it totals rows the validator rejected. |

## Documentation (`documentation`)

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus one docstring states what its function is not responsible for, like validating records. |
| **Meets** | 4 | Every function has a one-sentence docstring naming one job, and Step 3 answer 2 checks each for a double "and". |
| **Approaching** | 2 | A function lacks a docstring, or a docstring walks through the code instead of naming a job. |
| **Below Expectations** | 1 | Most functions have no docstring, or comments replace them, so the roll-call fails. |
