# Data Challenge: Looks Right. Is It?

**GitBook quest:** [Quest 1.10: Looks Right. Is It?](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-10-debugging) (quest runs Days 18-19)

**Vocabulary from the reading** (use these words in your shareout): `Bug`, `Logic Error`, `Off-by-One Error`, `Scope Bug`, `Undefined Attribute`, `Refactor`, `Expected Behavior`, `Actual Behavior`

**Skills assessed:** Attention to Detail, Control Flow & Loops, Problem Solving (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 2 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 2.** The rubric grades all 2 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

You are on the payroll desk at Harlow & Vance, a 5-person consulting firm
that runs its week off a hand-typed timesheet CSV. Your predecessor left
you their scripts, and somebody signs the checks against what they print.
On Day 1 the scripts crash. On Day 2 they run clean and print the wrong
numbers.

**You will build**

- One number you work out by hand for each step, before you run it.
- One fix to `weekly_hours()`, so it adds up the hours column as numbers.
- One loop that builds the `staff` list from the file, instead of a list typed by hand.
- One fix to the weekly-hours loop, so `total` starts at 0 for every employee.
- One fix to `weekly_pay()` and the overtime counter, so both follow the handbook rule.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Follow two tracebacks back to the line that made the bad value. Fix the bug there, not where Python gave up.
  - *Assessed today: Attention to Detail, Problem Solving*
- **Day 2**: Find two bugs that never raise anything. Work out the right number by hand first, then fix the line that breaks it.
  - *Assessed today: Attention to Detail, Control Flow & Loops, Problem Solving*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Attention to Detail and Control Flow & Loops.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** You cannot trust the output. Code that runs, reads well and is neatly indented can still overpay somebody by $1,810 a week.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- One partner owns expected and writes down what the number should be. The other owns actual and runs the code.
- Whoever finds a bug does not fix it. Tell your partner the line, the value, and what it should be, and they make the edit.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 18)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.
> - **How LLMs work** *(Day 5)*: It reads tokens, sees only its context window, stops at a training cutoff, and can answer differently each time.
> - **Task, Context, Evidence, Output (TCEO)** *(Day 5)*: Say the task, give the context, paste the evidence, and name the output you want.
> - **One-shot prompting** *(Day 5)*: Show one example of the answer shape you want, taken from a different problem.
> - **XML tags** *(Day 12)*: Wrap each part of a long prompt in its own tag, like `<task>` and `<data>`.
> - **Plan mode** *(Day 12)*: Ask for a plan with no code, fix it and approve it, then write the code yourself.
> - **Asking for tests and edge cases** *(Day 12)*: Ask which inputs would break it. You decide the right answer for each one.
> - **Data privacy** *(Day 12)*: Never paste real personal data, passwords or keys. Use made-up rows in the same shape.
>
> The tips below use only these.

Each tip below pairs one skill this challenge grades with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Spell out the spec** (Problem Solving) · Technique: **XML tags**, you learned this on Day 12

```text
<task>
Give me three test weeks for this pay rule. Do not write code.
</task>

<rule>
The first 40 hours of a week are paid at base rate, and hours past 40
at 1.5 times base rate.
</rule>

<output>
One week under 40 hours, one at exactly 40, and one over 40. Pick a
base rate for each, and show the arithmetic for the correct pay.
</output>
```

**Check:** Work one of the three weeks on paper first, then run all three through your fixed `weekly_pay()` and compare.

**Make it explain the output** (Control Flow & Loops) · Technique: **Make it explain**, you learned this in Module 0

```text
Here is a loop and what it printed:
[paste the step 3 code]
[paste its output]

Before I run anything else, predict what total holds at the start of
each pass of the outer loop. Then tell me whether that is what the code
should do.
```

**Check:** Add `print(total)` as the first line inside the outer loop and check its prediction against the real printout.

**Prompt to understand** (Attention to Detail) · Technique: **Prompt to understand**, you learned this in Module 0

```text
How do I read a Python traceback? Use a made-up example where one
function calls another. Which line shows where Python gave up, and how do
I find where the bad value came from?
```

**Check:** Use it on your Step 1 traceback, print the bad value with `repr()`, and find that exact value in the CSV.

</details>

## The Data

- **File:** `timesheet_hours.csv` (CSV)
- **Where it comes from:** Created for this challenge.
- **Setup:** Put `timesheet_hours.csv` in the same folder as your `looks-right-is-it_STUDENT.py`, or edit `DATA_FILE` at the top to its path.

The top of your .py already reads the file for you. `lines` is a list of strings, one per line of the file, and `lines[0]` is the header row. What each field means is yours to find out. Read the CSV with your eyes first, because you will hand-check numbers against it on both days.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 18)

### Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause

*Expect this step to raise `TypeError`. That is the point, not a bug.*

1. **Add up Rosa's hours by hand.** Find every `E101` row in the CSV and write the total under `# Step 1, answer 1:`.
2. **Research how to read a traceback** with your group, before you run anything. (`traceback` from Day 10)
3. **Run the file as given** and read the traceback from the bottom up. Note the function and the line it ended on.
4. **Print the bad value.** Add `print(repr(hours))` as the first line of `add_hours()`, run again, and find that value in the CSV. (`repr()` from Day 14)
5. **Walk one frame up** to the line that picked that value. Fix it there: read the hours column, and turn it into a number. (`parts[i]` and `int()` from *Trace the Path*, Step 1)
6. **Re-run** and check the total against your hand count.

*Work under `# Step 1` in `looks-right-is-it_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Before you run: Rosa's weekly hours (E101), added up by hand from the CSV.
2. How to read a traceback, in 2-3 bullets: what the last line tells you, what each block above it tells you, and where you found that out.
3. Which function the traceback ended in, and which line really held the bug.

<details>
<summary>Stuck? Open this.</summary>

`print(repr(hours))` shows a value in quotes. Count which column of the header it sits in, starting from 0, and compare that with the number in `parts[...]`. If you only add `int()` inside `add_hours()`, run it and read the new error.

</details>

### Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List

*Expect this step to raise `ZeroDivisionError`. That is the point, not a bug.*

1. **Count the employees in the CSV by eye** and write the number down.
2. **Run the file as given.** Count the lines that print before it stops, and note the ID it stopped on.
3. **Compare `staff` with the file,** one ID at a time.
4. **Decide where the bug lives:** in the division the traceback names, or in a line above it.
5. **Replace the hand-typed `staff` list** with an empty list and one loop over `lines[1:]` that appends each employee ID once. (`.append()` and `not in` from *Trace the Path*, Step 3)
6. **Print how many employees `staff` holds,** and check that every employee in the file has a line. (`len()` from *Trace the Path*, Step 3)

*Work under `# Step 2` in `looks-right-is-it_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Before you run: how many employees are in the CSV, counted by eye?
2. How many lines printed before the crash, and which ID did it stop on?
3. Where the bug lives, in the division line or somewhere above it, and why, in one sentence.

<details>
<summary>Stuck? Open this.</summary>

Print `staff`, then print every ID in the file with `print(row.split(",")[0])` in a loop, and compare the two. If you added `if days == 0: continue`, count your output lines against your count from action 1.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Share where the `TypeError` traceback ended, which line really held the bug, and how `print(repr(hours))` led you there.
- Explain how you rebuilt `staff` and how you proved all 5 employees made it into the report.
- How did your fixed `weekly_hours()` and `days_worked()` together give Samuel's average of 7.6 hours a day?

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 19)

### Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong

1. **Add up Rosa's and Mei's hours by hand** before you read the code. Nothing in the output says it is wrong, so these two numbers are your only detector.
2. **Read how `records` is built:** one dict per row, made by unpacking the five fields of `row.split(",")`. (`a, b = ...` from *Trace the Path*, Step 2; `dict` from Day 7; `float()` from Day 8)
3. **Run the file** and compare the `E101` and `E103` lines with your two numbers.
4. **Print `total` at the start of each pass** of the outer loop, and look at what it holds before each count begins.
5. **Find the one line that explains the pattern** and move it, so every employee starts at 0.
6. **Re-run and check all five numbers** against the CSV, not just Rosa's.

*Work under `# Step 3` in `looks-right-is-it_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. Before you run: Rosa's and Mei's weekly hours, added up by hand from the CSV.
2. What `total` held at the start of each employee's count, and the one line that explains it.
3. Why is Rosa's number right while Priya's equals the whole staff's hours for the week?

<details>
<summary>Stuck? Open this.</summary>

With the "starting" print in place, `E102` should start at 0. If it starts at 40, compare that 40 with Rosa's week. Then count how many times `total = 0` runs: once, or once per employee?

</details>

### Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week

1. **Read the handbook rule:** the first 40 hours of a week are paid at base rate. Hours beyond 40 are paid at 1.5 times base rate.
2. **Work out three weeks of pay by hand** before you read the code: Rosa (exactly 40 hours), Darnell (a few hours past 40) and Mei (well under 40).
3. **Run the file** and read both bottom lines: the overtime headcount and the dollar total. (`f-strings` from Day 7)
   - **New: `:>9,.2f`** inside an f-string's braces lines a number up to the right in 9 spaces, adds commas and shows 2 decimals. `f"{1543.5:>9,.2f}"` gives `' 1,543.50'`. It's written for you in Step 4 of your .py; you'll write it yourself next time.
4. **Fix `weekly_pay()`** so it matches the rule word for word.
5. **Check every other line that compares against `40`** and fix it the same way.
6. **Re-run and check** all three hand-worked figures and the headcount.

*Work under `# Step 4` in `looks-right-is-it_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. Before you run: Rosa's, Darnell's and Mei's weekly pay, worked out by hand from the handbook rule.
2. The two bugs you found, each with its line and what you changed it to.
3. Why can only Rosa's exactly-40 week catch one of the two bugs?

<details>
<summary>Stuck? Open this.</summary>

Run `print(weekly_pay(40, 24.00))`. The rule says 40 hours earn 40 x 24 = 960. Then run `print(weekly_pay(41, 24.00))` and work out by hand what 41 hours should pay. There is more than one line that compares against `40`.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share the move that found the `total = 0` bug: the number you worked out by hand, or the print you added, and what it showed.
- Explain how you fixed `weekly_pay()` and how you tested it with Rosa's 40-hour week.
- How did the dollar total and the overtime headcount together show that one fix was not enough?

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `looks-right-is-it_STUDENT.py` (you may rename it `looks-right-is-it.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
