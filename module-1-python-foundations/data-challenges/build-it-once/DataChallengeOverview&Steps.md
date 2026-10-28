# Data Challenge: Build It Once, Use It Again

**GitBook quest:** [Quest 1.2: Build It Once, Use It Again](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-02-functions-scope) (quest runs Days 3-5)

**Vocabulary from the reading** (use these words in your shareout): `Function`, `Parameter`, `Argument`, `Return Value`, `Local Variable`, `Global Variable`, `Scope`

**Skills assessed:** Functions & Modular Programming, Attention to Detail, Collaboration (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 3 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 3.** The rubric grades all 3 days together, so keep every day's work in `build-it-once_STUDENT.py`.

## Scenario

The coordinator at the Fairhaven Recreation Center keeps a class sign-up
log, and the board keeps changing its mind. You will write each loop once,
give it a name, and hand it the part that changes as an argument. When the
board moves the long-booking cutoff from 4 sessions to 2, you change the
call, not the loop.

**You will build**

- One function, `total_sessions()`, that returns the total sessions for any list of records.
- One list, `swim_only`, that holds just the Swim records.
- One function, `count_long_bookings()`, that takes the records and a cutoff and returns a count.
- One function, `show_long_bookings()`, that only prints that count, so you can see what a function with no `return` hands back.
- One function, `count_reaching_outside()`, that reads the cutoff from outside instead of taking it as a parameter.
- One function, `log_signup()`, that takes the last member in and returns the next one out.
- Three small functions, `sessions_in()`, `signups_for()` and `total_for()`, where `total_for()` calls the other two.
- Five calls on inputs nobody asked for, each with your verdict beside it.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1** (Module Day 3): Turn totaling and counting loops into functions that return a value. Call each one twice on different inputs.
  - *Assessed today: Functions & Modular Programming, Attention to Detail*
- **Day 2** (Module Day 4): Compare a function that reads an outside name with one that takes it as a parameter. Then trigger an `UnboundLocalError` and state its rule.
  - *Assessed today: Functions & Modular Programming, Attention to Detail*
- **Day 3** (Module Day 5): Build one function out of two smaller ones. Then judge its answers on inputs nobody asked for: right, or just quiet?
  - *Assessed today: Functions & Modular Programming, Attention to Detail, Collaboration*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Functions & Modular Programming and Attention to Detail. If AI writes it, nothing has been measured.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** None of the Python is new. The LiveLabs cover `def`, `return` and scope. What is new is judging whether a quiet `0` from your own function is right.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.
- **Do not use `global`.** It is banned in this challenge. Pass values in and return them out.

<details>
<summary>Working as a pair</summary>

- Before a function runs, the partner who did not write it names its parameters and what it returns. If they cannot, the function needs a better name or a shorter body.
- On Day 3, each of you writes down two inputs that might break `total_for()` on your own. Then trade lists and run each other's. Label whose is whose in your file.
- Each of you submits your own copy, and has to be able to explain any line alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 3)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.

Each tip pairs one graded skill with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Prompt to understand** (Functions & Modular Programming)

```text
Explain the difference between return and print inside a Python
function. Use a tiny made-up function that doubles a number, not my code.
Show what a variable holds when I store the result of each version. Which
Python docs page covers return?
```

**Check:** Type both tiny versions yourself, then compare what each hands back with what `show_long_bookings()` handed back in Step 2.

**Make it explain** (Functions & Modular Programming)

```text
Here is a function and the error it raises:
[paste log_signup_broken]
[paste the last three lines of the traceback]

In plain words, why does Python treat this name as local inside the
function? Point at the exact line that makes it local. Do not rewrite the
function.
```

**Check:** Find that line in your own file and compare its reason with the one you wrote in Step 4. If it tells you to add `global`, that is not the fix here.

**Verify against your own work** (Attention to Detail)

```text
Here is a sign-up log:
[paste the data rows]

Add up the sessions for the Swim rows only. List each Swim row you used
before you give the total.
```

**Check:** Add up Swim by hand first. Then check its total and yours against what `total_sessions(swim_only)` prints.

**Make it explain** (Attention to Detail)

```text
Here is my function total_for(records, member), one input I gave it,
and what it returned:
[paste the function]
[paste the input and the printed result]

Walk me through the function line by line for that input, and say why
it returns that value. Do not tell me whether the answer is right. I
will decide that.
```

**Check:** Trace the same input on paper. Then write your own verdict beside the result, as Step 6 asks.

**Prompt to understand** (Collaboration)

```text
I am the navigator. My partner wrote total_for so it calls two smaller
functions:
[paste all three]

Give me three questions to ask my partner that check whether each
function does exactly one job. Do not answer them.
```

**Check:** Ask your partner the questions and have them point at the lines that answer each one.

</details>

## The Data

- **File:** `data/rec_center_signups.txt` (TXT)
- **Where it comes from:** Created for this challenge.
- **How to run:** The .py opens `data/rec_center_signups.txt`, so run it from the `data-challenges/` folder, the one that holds `data/`:

  ```
  cd module-1-python-foundations/data-challenges
  python3 build-it-once/build-it-once_STUDENT.py
  ```

  A `FileNotFoundError` means your terminal is in the wrong folder, not that the file is missing.

Loading the file is not the work here. The `with open(...)` lines at the top of Step 1 are already written for you and fill the list `signups`. What each item in `signups` holds is yours to work out.

**Before you write any code, open the file with your partner.** Answer these under THE DATA at the top of your .py, each under its `# Your answer:` line:

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 3)

### Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only

<<<<<<< HEAD
```python
with open("rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]
```
=======
1. **Predict two totals by hand** and write both in a `#` comment under the Step 1 banner, before you run anything:
   - the sessions across all 13 records (add the third field down the file), and
   - the sessions on the records whose class is `Swim` only.
2. **Fill in `total_sessions(records)`.** Replace `pass` with one loop over `records` that adds each record's sessions number to a running total. (`def` from the Day 3 LiveLab; `.split(",")` and `int()` from *Trace the Path*, Step 1)
3. **Return the total after the loop ends.** Use `return`, not `print`. (`return` from the Day 3 LiveLab)
4. **Fill `swim_only`** under its TODO with one loop over `signups` that appends each record whose class, the second field, is `Swim`. (`.append()` from *Trace the Path*, Step 3; `[i]` from *Trace the Path*, Step 1)
5. **Run the file.** Check the `every class:` and `swim only:` lines against your two predictions.
>>>>>>> upstream/main

*Work under `# ===== Step 1` in `build-it-once_STUDENT.py`: complete its TODOs.*

<details>
<summary>Stuck? Open this.</summary>

Test one record first: `print(signups[0].split(","))` should show three pieces, and the sessions number is the last one. If `every class:` prints `None`, your function never reaches a `return`. If it prints a number smaller than your hand total, add `print(record, total)` as the first line inside the loop. Count the printed lines. If you see only one, your `return` is indented inside the loop.

</details>

### Step 2: Count Long Bookings at Two Different Cutoffs With One Function

1. **Predict both `returned:` counts** in a `#` comment, reading the third field down the file: records with 4 or more sessions, then records with 2 or more.
2. **Fill in `count_long_bookings(records, minimum)`.** Count each record whose sessions number is `minimum` or more, then return the count. (`>=` from the Day 1 LiveLab)
3. **Fill in `show_long_bookings(records, minimum)`** so it prints a sentence with the same count in it. Only print. Do not add a `return`.
4. **Run the whole file**, including the `print` and `handed_back` lines at the bottom of Step 2 that were written for you.
5. **Answer in writing** under Step 2's `# Your answer:` line:
   - What does `handed_back` hold, and why? It is on the last printed line. (`None` from the Day 3 LiveLab)
   - Point at your lines: which name is the parameter `minimum`, and which values are the arguments `4` and `2`?

*Work under `# ===== Step 2` in `build-it-once_STUDENT.py`: complete its TODOs.*

<details>
<summary>Stuck? Open this.</summary>

Add `print(type(handed_back))` under the last line of Step 2 and run it. Then add `print(handed_back == count_long_bookings(signups, 4))`. Both functions put the same number on the screen. Only one of them handed it back.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Share your two `total_sessions()` results and how you checked each one by hand. If your numbers differ from another group's, one of you has a bug worth finding.
- Explain what `show_long_bookings()` handed back, and what that tells you about `return` and `print`.
- Point at your own `count_long_bookings(signups, 4)` line: which is the parameter, and which is the argument?

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 4)

### Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare

1. **Predict both `cutoff` lines** in a `#` comment, with no new arithmetic. You already have the counts at 4 and at 2 from Step 2. Write which one each identical call prints, and why.
2. **Fill in `count_reaching_outside(records)`.** Count the same thing `count_long_bookings()` does, but use `sessions_cutoff` instead of a `minimum` parameter. `sessions_cutoff` is set outside the function. (global variable from the Day 4 LiveLab)
3. **Run the file once.** The first call is written for you, while `sessions_cutoff = 4`.
4. **Under the first TODO after `sessions_cutoff = 2`,** print `count_reaching_outside(signups)` again, with the call line unchanged.
5. **Under the second TODO,** print `count_long_bookings(signups, 4)` for comparison.
6. **Answer in writing** in a `#` comment: which of the two functions would you trust in a file you did not write, and what in the call line told you?

*Work under `# ===== Step 3` in `build-it-once_STUDENT.py`: complete its TODOs.*

<details>
<summary>Stuck? Open this.</summary>

Nothing here is broken. For each call to `count_reaching_outside(signups)`, find the line that last set `sessions_cutoff` before it ran. Then look at `count_long_bookings(signups, 4)`. Where does its cutoff show up?

</details>

### Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError

1. **Fill in `log_signup(record, previous_member)`.** Pull the member name out of `record` (the first field), print `previous_member` and this member on one line, and return this member's name.
2. **Predict both printed lines** in a `#` comment, reading the names off the top of the file.
3. **Under the TODO after `last_member = "nobody yet"`,** call `log_signup()` on `signups[0]`, then on `signups[1]`. Store what it returns back into `last_member` each time, and pass `last_member` in as `previous_member`.
4. **Leave `log_signup_broken()` exactly as written.** It reads `last_seen`, a name set above the function, then assigns to it.
5. **Predict in a comment** whether its `print` line will work. Step 3 showed a function reading an outside name just fine.
6. **Run the file and read the whole traceback.** It is supposed to raise. (`UnboundLocalError` from the Day 4 LiveLab)
7. **Answer in writing** under Step 4's `# Your answer:` line, in your own words, before you look anything up: the exception name, the variable, and the line it points at.
8. **Put a `#` in front of the call `log_signup_broken(signups[2])`** so Day 3's steps can run. Do not add `global`. Your `log_signup()` already shows the fix: pass the value in, return it back out.

*Work under `# ===== Step 4` in `build-it-once_STUDENT.py`: complete its TODOs.*

<details>
<summary>Stuck? Open this.</summary>

The traceback points at a `print` line, and a `print` only reads. Find the line inside `log_signup_broken()` where `last_seen` sits on the left of an `=`. Delete it in a scratch copy, run again, and compare. The rule is about the whole function body, not just the failing line.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share how the output of `count_reaching_outside(signups)` changed when `sessions_cutoff` changed, with the same call line. Which function do you trust, and why?
- Explain the `UnboundLocalError` in your own words: which variable, which line, and why a line that only reads failed.
- How did `log_signup()` do the same job without the error? Say whether AI offered `global` as the fix.

Be ready to answer **"why did you do it that way?"**

## Day 3 (Module Day 5)

### Step 5: Build Per-Member Totals Out of Three Functions, Not One

1. **Predict Gwen's total** in a `#` comment, adding up Gwen's rows in the file by hand.
2. **Fill in `sessions_in(record)`** so it returns one record's sessions number, as a number.
3. **Fill in `signups_for(records, member)`** so it returns a list of only the records belonging to `member`.
4. **Fill in `total_for(records, member)`** so it calls `signups_for()` and `sessions_in()` to do its work. It should hold no `.split()` of its own.
5. **Under `# TODO: print a line per member`,** print one line each for Nia, Omar, Tess, Rafi and Gwen. Check Gwen's line against your comment.
6. **Before you run,** show your partner the line where each of the three functions gets called.

*Work under `# ===== Step 5` in `build-it-once_STUDENT.py`: replace each `pass`, then complete the TODO.*

<details>
<summary>Stuck? Open this.</summary>

Test each function alone before `total_for()` uses it. `print(sessions_in(signups[0]))` should print `4`, the sessions on Nia's Yoga row. `print(signups_for(signups, "Gwen"))` should list only records that start with `Gwen`. Whichever one disagrees with the file is the one to fix first.

</details>

### Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer

No new functions. Call the ones you already have, and print each result.

1. **Under `# TODO: an empty list`,** print `total_for([], "Nia")`.
2. **Under `# TODO: a list holding exactly one record`,** print `total_for([signups[0]], "Nia")`.
3. **Under `# TODO: a member name that is not in the file at all`,** print `total_for(signups, "Marco")`.
4. **Under `# TODO: a name that differs from a real member's only by capitalization`,** print `total_for(signups, "nia")`.
5. **Below those, print `signups_for([], "Nia")`.**
6. **Under `# TODO: then: do the per-member totals add up to the whole-file total?`,** add up `total_for()` for all five members and print that sum beside `total_sessions(signups)`. The two should agree.
7. **Answer in writing** in a `#` comment beside each of the five results: right, or just a number that did not crash? Argue each one with your partner first.

*Every line runs clean. Two of them deserve a different answer than they get.*

*Work under `# ===== Step 6` in `build-it-once_STUDENT.py`: complete its TODOs.*

<details>
<summary>Stuck? Open this.</summary>

Next to each result, write what the coordinator would expect to hear if they asked that question at the front desk. For `"nia"`, ask: is there a member called Nia in the file, and what is that member's real total? Where the code and the coordinator disagree, you found a quiet wrong answer. Nothing has to crash for that to count.

</details>

### Share Out: Day 3

**Last 15 minutes, back together as a class. Bring:**

- Share your verdict on the strangest edge case: is the answer right, or just quiet? If you and your partner disagreed, bring both positions.
- Explain how you built `total_for()` from `sessions_in()` and `signups_for()`, and how you tested each one alone.
- Did the five per-member totals add up to `total_sessions(signups)`? Say how you would run that check on a 430-row file you cannot eyeball.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `build-it-once_STUDENT.py` (you may rename it `build-it-once.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
