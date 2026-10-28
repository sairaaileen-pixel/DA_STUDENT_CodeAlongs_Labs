# Data Challenge: Validate, Catch, Keep Going

**GitBook quest:** [Quest 1.6: Validate, Catch, Keep Going](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-06-validation-errors) (quest runs Days 9-10)

**Vocabulary from the reading** (use these words in your shareout): `Validation`, `Valid Input`, `Invalid Input`, `Malformed Input`, `Exception`, `Error Handling`, `try`, `except`

**Skills assessed:** Functions & Modular Programming, Attention to Detail, Problem Solving (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 2 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 2.** The rubric grades all 2 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

The city's 311 line exports every service request as one line of CSV,
typed by hand at a dozen intake desks. The operations team wants the
average number of days a request stays open. Your report may not crash,
and no bad row may vanish without a reason.

**You will build**

- One function, `validate_request()`, that returns a verdict and a reason for one row.
- One loop that sends every row through the validator and prints each rejection.
- One report loop with no protection, which you run until it crashes.
- One second function, `check_days_open()`, that uses `try`/`except` on the `days_open` field.
- One rebuilt report where every row is either counted or skipped with a reason.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Write a validator that returns a verdict and a reason. Run all 15 rows through it and report what is wrong with each rejected row.
  - *Assessed today: Functions & Modular Programming, Attention to Detail*
- **Day 2**: Watch one bad field crash a working report. Then rebuild it so every row is either counted or skipped with a reason.
  - *Assessed today: Functions & Modular Programming, Problem Solving, Attention to Detail*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Functions & Modular Programming and Attention to Detail.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** Returning two values from one function. Choosing, for each bad value, between an `if` and a `try`, and defending the choice.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- One partner writes the validator and the other writes the loop that calls it, without seeing each other's code. If the halves do not fit, talk through the return shape.
- Before anyone writes a `try`, each of you writes down which rows the rebuilt report will skip. Then compare.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 9)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.
> - **How LLMs work** *(Day 5)*: It reads tokens, sees only its context window, stops at a training cutoff, and can answer differently each time.
> - **Task, Context, Evidence, Output (TCEO)** *(Day 5)*: Say the task, give the context, paste the evidence, and name the output you want.
> - **One-shot prompting** *(Day 5)*: Show one example of the answer shape you want, taken from a different problem.
>
> The tips below use only these.

Each tip below pairs one skill this challenge grades with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Spell out the spec** (Functions & Modular Programming) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Help me test my spec. Do not write the function.

Context: validate_request(row) takes one CSV line split into fields. It
returns (True, "ok") when the row has 5 fields, a borough that is not
empty, and a status of Open, In Progress or Closed. Otherwise it returns
False and a short reason.

Evidence: That spec is all I have so far.

Output: Ask me about anything the spec leaves unclear. Then give me 6
test rows, each with the pair a correct function should return.
```

**Check:** Check each expected pair against the spec yourself, then run your function on all six.

**Validate against your own work** (Attention to Detail) · Technique: **One-shot prompting**, you learned this on Day 5

```text
For each made-up value below, tell me whether int() can convert it, and
whether the result makes sense as a number of days a request was open.
Answer in exactly this shape:

Example: "12" | int() works: yes | makes sense: yes

Now do these: "3.0", "-4", "  9", "nine", "0"
```

**Check:** Predict each line yourself, then run `int()` on each value; where the AI and the run disagree, the run wins.

**Prompt to understand** (Problem Solving) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Show me two tiny Python functions that turn a string into an int. One
lets the ValueError happen. One catches it and returns a default. Use
made-up strings, not my data. When is each one the right choice? Which
one can lose information without anyone noticing?
```

**Check:** Run both on "7", "abc" and an empty string, then decide which one your report needs.

**Make it explain the output** (Problem Solving) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Explain my traceback. Do not rewrite my loop.

Context: My report averages a days_open column. It crashed partway
through the file.

Evidence:
[paste the traceback]

Output: The exception Python raised and the line it raised on. Then
name the except clause that would catch exactly that and nothing else.
```

**Check:** The exception it names must match the last line of your own traceback, word for word.

</details>

## The Data

- **File:** `service_requests.csv` (CSV)
- **Where it comes from:** Created for this challenge.
- **Setup:** Put `service_requests.csv` in the same folder as your `validate-catch-keep-going_STUDENT.py`, or edit `DATA_FILE` at the top to its path.

The top of your .py already reads the file for you. `header` is the column-name line. `rows` holds every line after it, one request per string, with blank lines dropped. A `FileNotFoundError` means `DATA_FILE` does not point at the file yet.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 9)

### Step 1: Write `validate_request()` to Return a Verdict and a Reason

1. **Make two constants:** `EXPECTED_FIELDS` set to 5, and `ALLOWED_STATUS`, a list of the three statuses the team allows. (`list` from Day 7)
2. **Write one function, `validate_request(row)`,** that splits `row` on commas into `fields`. (`def` from Day 3; `.split()` from *Trace the Path*, Step 1)
3. **Read the field-count check, given first.** It returns `False` and a reason when `len(fields)` is not `EXPECTED_FIELDS`. (`len()` from *Trace the Path*, Step 3; `!=` from Day 9)
   - **New: `return a, b`** hands back two values at once, as a tuple. If `pair()` ends with `return True, "ok"`, then `ok, reason = pair()` sets `ok` to `True` and `reason` to `"ok"`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
   - **New: `str()`** turns a value into text so you can join it to other text. `"count: " + str(4)` gives `"count: 4"`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
4. **Unpack the five fields into five names** that match the header: `request_id`, `complaint_type`, `borough`, `days_open`, `status`. Return `False` and a reason for an empty borough, or for a status not in `ALLOWED_STATUS`. (`not in` from *Trace the Path*, Step 3)
5. **Return `True` and `"ok"`** when every check passes.
6. **Run the three test rows** at the bottom of the step before you point the validator at the whole file.

*Work under `# Step 1` in `validate-catch-keep-going_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Before you code: two or three sentences on what is in the file. What does one row hold, and what already looks wrong?
2. How does the caller take the two returned values apart in one line, and what is the function really handing back?

<details>
<summary>Stuck? Open this.</summary>

`print(type(validate_request("SR-1,Rodent,Bronx,2,Open")))` should show a tuple. If it shows `bool` or `NoneType`, a `return` is missing its reason. A `ValueError` about unpacking on a four-field row means your field-count check runs after the unpack line.

</details>

### Step 2: Run All 15 Rows Through the Validator and Report Each Rejection

1. **Hand-count the bad rows first.** Check each of the 15 rows for five fields, a borough, and an allowed status.
2. **Write one loop over `rows`** that unpacks `validate_request(row)` into `ok` and `reason`. (`for` from Day 1; `return a, b` from Step 1)
3. **Add 1 to `valid`** for every row that passes.
4. **Print the request ID and the reason** for every row that fails. The ID is `row.split(",")[0]`. (`row[0]` from *Trace the Path*, Step 1)
5. **Run it** and compare `valid` with your hand count.
6. **Read every row that passed, one by one,** and ask whether any got through that should not have.

*Work under `# Step 2` in `validate-catch-keep-going_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Before you run: how many rows fail your three rules by your own hand count, and which rule does each break?
2. Read the rows that passed. Which ones got through that should not have, and why can your validator not see them?

<details>
<summary>Stuck? Open this.</summary>

Print `validate_request(rows[0])` on its own before you write the loop. If `ok, reason = ...` raises `cannot unpack non-iterable bool object`, one path in your validator returns a bare `True` or `False`.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Share your pass count and your three rejection reasons. Did every row that passed deserve to?
- Explain how you wrote and tested `validate_request()`. Which test row did you check by hand first?
- Share what happens when you move the field-count check below the line that unpacks the row.

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 10)

### Step 3: Build the Days-Open Report With No Protection and Watch It Crash

*Expect this step to raise `ValueError`. That is the point, not a bug.*

1. **Predict** how many report lines print before it crashes. Walk the rows your validator passes and find the first `days_open` that `int()` cannot convert. (`int()` from *Trace the Path*, Step 1)
2. **Set `total_days` and `counted` to 0,** then write one loop over `rows`.
3. **Skip every row `validate_request()` rejects** with `continue`. (`continue` from Day 1)
4. **Convert the fourth field, `days_open`, with `int()`.** Add it to `total_days`, add 1 to `counted`, and print the ID with the number.
5. **Add no protection at all.** No `try`, no extra `if`. Run it and read the whole traceback.
6. **Comment out this step's code** once you have your answers, so Step 4 can run.

*Work under `# Step 3` in `validate-catch-keep-going_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. Before you run: how many report lines print before it crashes, and which row stops it?
2. The last line of the traceback, exactly as printed, and how many rows were counted before it.
3. What happens to the rows the loop never reached?

<details>
<summary>Stuck? Open this.</summary>

If it runs to the end, print `row.split(",")[3]` for each surviving row and check that is the field you pass to `int()`. The count to bring is the number of ID lines above the traceback.

</details>

### Step 4: Rebuild the Report So Every Row Is Counted or Skipped

1. **Predict** how many rows get skipped now. Re-read `days_open` in all 15 rows first.
2. **Write a second function, `check_days_open(value)`,** that returns a verdict and a reason for one `days_open` value. (`return a, b` from Step 1)
3. **Put `int(value)` inside a `try`,** and return `False` with a reason in `except ValueError`. Never use a bare `except:`. (`try/except` from Day 10)
4. **Return `False` with a reason** when the number is below 0.
5. **Rebuild the loop** so `validate_request()` runs first, and `check_days_open()` runs only on rows that pass it.
6. **Count every row:** add 1 to `counted` or to `skipped`, and print the ID and reason for each skip.
7. **Run it** and check that `counted` plus `skipped` is 15.
   - **New: `round()`** rounds a number to the number of decimal places you give it. `round(8.24, 1)` gives `8.2`. It's written for you in Step 4 of your .py; you'll write it yourself next time.

*Work under `# Step 4` in `validate-catch-keep-going_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. Before you run: how many rows get skipped now, and which ones did your Day 1 validator let through?
2. For `3 days` and for `-3`: did an `if` or a `try` catch it, and could the other tool have?
3. Does `counted` plus `skipped` account for every row? Show the sum.

<details>
<summary>Stuck? Open this.</summary>

Run `int("-3")`, `int("3 days")` and `"-3".isdigit()` on their own. An `except` only runs when something raises, so check which one raises. If `counted` plus `skipped` is not 15, find the branch that skips a row without adding to `skipped`.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share the last line of your traceback, and how many rows your report counted before it crashed.
- Explain how you created and tested `check_days_open()`. Which tool caught `3 days`, and which caught `-3`?
- How did `validate_request()` and `check_days_open()` together account for all 15 rows?

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `validate-catch-keep-going_STUDENT.py` (you may rename it `validate-catch-keep-going.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
