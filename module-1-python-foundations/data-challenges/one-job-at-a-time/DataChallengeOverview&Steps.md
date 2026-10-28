# Data Challenge: One Job at a Time

**GitBook quest:** [Quest 1.7: One Job at a Time](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-07-second-function) (quest runs Days 11-12)

**Vocabulary from the reading** (use these words in your shareout): `Function`, `Parameter`, `Return Value`, `Accumulator`, `Validation`, `Single-Purpose Function`

**Skills assessed:** Functions & Modular Programming, Control Flow & Loops, Documentation (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 2 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 2.** The rubric grades all 2 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

The Eastside Neighborhood Pantry logs every donation on a laptop at the
intake table. The coordinator needs a category breakdown for the food bank
and a JSON copy for the website. An earlier volunteer wrote it all as one
huge function. Nobody could change one part without breaking the rest.

**You will build**

- One function, `validate_donation()`, that returns a verdict and a reason for one record.
- One function, `summarize_donations()`, with one loop and one dict that totals pounds per category.
- One function, `export_summary()`, that writes a summary to a JSON file.
- One function, `run_pipeline()`, that calls the others in order. The summarizer is one of its parameters.
- A second summarizer, `summarize_by_day()`, that you swap in. You edit nothing else.
- One docstring on every function, naming its one job in one sentence.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Write a second, single-purpose function that builds the category summary in one loop. Give every function a docstring naming its one job.
  - *Assessed today: Functions & Modular Programming, Control Flow & Loops, Documentation*
- **Day 2**: Join read, validate, summarize and export into one pipeline. Then swap in a new summarizer. Edit none of the other functions.
  - *Assessed today: Functions & Modular Programming, Documentation*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Functions & Modular Programming and Control Flow & Loops.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** Docstrings, and passing a function as an argument. Your docstrings are graded, and on Day 2 the program prints them.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- Before any code, each of you writes the summarizer's contract on paper: Input, Job, Output. Compare your two Job lines before you start.
- One partner writes `summarize_by_day()` while the other does not look. Then plug it into the pipeline cold.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 11)
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

**Validate against your own work** (Documentation) · Technique: **Verify against your own work**, you learned this in Module 0

```text
Here is one of my functions:
[paste it]

Describe its job in one sentence without using the word "and". If you
cannot, tell me which lines are doing a second job. Do not rewrite it.
```

**Check:** Put its sentence next to your own docstring; if they name different jobs, follow the return value to find out who misread it.

**Prompt to understand** (Functions & Modular Programming) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Explain what it means to pass a function as an argument in Python. Use
len and one made-up function, not my code. What is the difference between
len and len("abc")? Which docs page explains it?
```

**Check:** Run `print(len)` and `print(len("abc"))` yourself and check that the two printed lines match its story.

**Validate against your own work** (Control Flow & Loops) · Technique: **One-shot prompting**, you learned this on Day 5

```text
Total the pounds per category for each made-up list of donation
records. Answer in exactly this shape:

Example: (Rice, Grains, 2), (Oats, Grains, 3) | Grains: 5

Now do these:
(Beans, Canned, 4), (Soup, Canned, 1.5), (Apples, Produce, 2)
(Pears, Produce, 0.5)
```

**Check:** Do the totals by hand first, then hand-count one category off the CSV and check your own printed total for it.

**Make it explain the output** (Functions & Modular Programming) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Predict which of my functions a new request would change. Do not
write code.

Context: My donations report is four small functions, and run_pipeline
calls them in order. The food bank now wants a by-date breakdown.

Evidence:
[paste your four docstrings]

Output: One line per function: does it change, and why?
```

**Check:** After Step 4, compare its prediction with the functions you actually had to edit.

</details>

## The Data

- **File:** `pantry_donations.csv` (CSV)
- **Where it comes from:** Created for this challenge.
- **Setup:** Put `pantry_donations.csv` in the same folder as your `one-job-at-a-time_STUDENT.py`, or edit `DATA_FILE` at the top to its path.

Step 1 gives you `read_donations(path)`, which reads the file. Call it with `DATA_FILE` and it returns a list of strings, one record per line, with the header row and blank lines dropped. A `FileNotFoundError` means `DATA_FILE` does not point at the file yet.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 11)

### Step 1: Write the Read-and-Validate Pair, Each With a Docstring

1. **Read `read_donations()`.** It is given in full. Its docstring, the first line in triple quotes, names its one job.
   - **New: `docstring`** is a string in triple quotes on a function's first line that says what the function does. `def total(): """Add up the pounds."""` documents `total()`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
   - **New: `.splitlines()`** splits text into a list of its lines. `"a\nb".splitlines()` gives `['a', 'b']`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
   - **New: `.strip()`** removes spaces from both ends of a string. `" rice ".strip()` gives `"rice"`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
2. **Write one function, `validate_donation(record)`,** with its own docstring, that returns a verdict and a reason. (`docstring` from Step 1; `return a, b` from *Validate, Catch, Keep Going*, Step 1)
3. **Check the field count before any check that reads a field.** On a short row, every later field slides over one place. (`len()` from *Trace the Path*, Step 3)
4. **Reject a blank category, then a pounds value `float()` cannot convert,** catching it with `except ValueError`. (`float()` from Day 8; `try/except` from Day 10)
5. **Write one loop over the records** that appends usable ones to `valid` and prints the ID and reason for each rejection. (`.append()` from *Trace the Path*, Step 3)

*Work under `# Step 1` in `one-job-at-a-time_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Before you code: what does one record hold, and which records already look wrong?
2. Name three things your validator promises about each record it keeps.

<details>
<summary>Stuck? Open this.</summary>

Move your field-count check to the bottom of the validator and run it again. Compare the reason printed for `D017` with the one you got before, then read `D017`'s line in the file. Which reason is true?

</details>

### Step 2: Write `summarize_donations()` for the Category Breakdown Only

1. **Write the docstring first:** one sentence naming the function's one job. If it needs "and" twice, it is two jobs.
2. **Make one dict, `by_category`,** that maps each category to its donation count and pounds, inside one loop over `valid_records`. (`dict` from Day 7; `float()` from Day 8)
3. **Create a category's entry the first time it shows up,** before you add into it. (`not in` from *Trace the Path*, Step 3)
4. **Add each record's pounds to `total_pounds`** in the same loop. No second pass. (`+=` from Day 5)
5. **Return one dict** with the record count, `total_pounds` and `by_category`.
6. **Put no validation inside it.** `validate_donation()` already did that job.
7. **Run it** on `valid` and hand-check one category's pounds off the CSV. (`.items()` from Day 7)

*Work under `# Step 2` in `one-job-at-a-time_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Hand-count one category's pounds off the CSV. Which category, what did you get, and does it match your printed line?

<details>
<summary>Stuck? Open this.</summary>

In a scratch file, run `d = {}` and then `d["grains"] += 1`, and read the error. Your loop needs a line that runs before the `+= 1` the first time a category shows up.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Share the one-sentence job of `summarize_donations()`. Is it really one job, or is there a quiet "and also"?
- Explain how you created and tested `summarize_donations()`. Which category did you hand-count, and did it match?
- How do `validate_donation()` and `summarize_donations()` split the work? Name one thing the summarizer can trust because of the validator.

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 12)

### Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings

1. **Run `print(len)` and `print(len("abc"))`** in a scratch file and compare the two lines.
   - **New: `passing a function`** means handing a function's name, without `()`, to another function that calls it later. If `apply(job, x)` returns `job(x)`, then `apply(len, "abc")` gives `3`. It's written for you in Step 3 of your .py; you'll write it yourself next time.
2. **Write `export_summary(summary, path)`** with a docstring. It writes the dict to `path` as JSON and does nothing else. (`json.dump()` from Day 8; `with open()` from Day 1)
3. **Write `run_pipeline(in_path, out_path, summarize)`** with a docstring. It reads, keeps the valid records, and exports `summarize(kept)`.
4. **Use the `summarize` parameter** to call the summarizer. Do not write its name inside `run_pipeline`.
5. **Run the given roll-call loop.** It prints each function's name and the first line of its docstring. (`.__name__` from *Pick the Right Container*, Step 6)
   - **New: `.__doc__`** holds a function's docstring as text. If `total()` has the docstring `"Add up the pounds."`, then `total.__doc__` gives `'Add up the pounds.'`. It's written for you in Step 3 of your .py; you'll write it yourself next time.

*Work under `# Step 3` in `one-job-at-a-time_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. What did `print(len)` and `print(len("abc"))` each print, and what do the parentheses do?
2. Read the four printed docstring lines with your partner. Does any one need "and" twice?

<details>
<summary>Stuck? Open this.</summary>

In a scratch file, write `def shout(word): return word.upper()` and `def apply(job, value): return job(value)`, then run `print(apply(shout, "pantry"))`. Find the line where `shout` actually ran. `run_pipeline` takes its summarizer the same way.

</details>

### Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited

1. **Write `summarize_by_day(valid_records)`** with its own docstring. Same input and output shape as `summarize_donations()`, but a `"by_day"` dict keyed by the date in `parts[4]` replaces `"by_category"`.
2. **Call the same `run_pipeline()`,** handing it `summarize_by_day` instead. (`passing a function` from Step 3)
3. **Read `donation_summary.json` back** with `json.load()`, inside a `with open()` block, rather than trusting the dict in memory. (`json.load()` from Day 8)
4. **Run the given prints:** the totals, then one line per date in order. (`sorted()` from *Pick the Right Container*, Step 4)
5. **Count how many of your other functions you had to edit** for the swap.

*Work under `# Step 4` in `one-job-at-a-time_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. How many of your other functions did you edit for the swap? If any, what was the summarizer reaching into?
2. Three dates show only 1 donation. Why, and what should the coordinator see?

<details>
<summary>Stuck? Open this.</summary>

Right after `json.load`, add `print(reloaded.keys())` and compare it with the keys `summarize_by_day` returns. If they differ, the file came from a different summarizer than the one you passed in.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share how many of your other functions you edited for the swap. If any, what was the summarizer reaching into?
- Explain how you created and tested `run_pipeline()`. How did you prove the JSON file held what you wrote?
- How did `summarize_donations()` and `summarize_by_day()` answer two different questions through the same pipeline?

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `one-job-at-a-time_STUDENT.py` (you may rename it `one-job-at-a-time.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
