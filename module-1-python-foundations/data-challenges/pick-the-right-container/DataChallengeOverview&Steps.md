# Data Challenge: Pick the Right Container

**GitBook quest:** [Quest 1.3-1.5: When the Crowd Grows · Pick the Right Container · Make It Survive](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-04-data-structures) (quest runs Days 6-8)

**Vocabulary from the reading** (use these words in your shareout): `Input Size`, `Big-O`, `Linear Scan`, `Lookup`, `Data Structure`, `Dictionary`, `Set`, `Serialization`

**Skills assessed:** Algorithmic Complexity (Big-O), Control Flow & Loops, AI Output Validation, Data Structures Selection (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 3 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 3.** The rubric grades all 3 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

A city transit agency hands you one day of its turnstile tap log. The
analytics team wants the distinct cards, the repeat riders, and a summary
file the overnight job can read. Every version you write gets the right
answer, so you are graded on how much work each one does, counted and not
timed.

**You will build**

- One function, `scan_for()`, that counts the comparisons a Linear Scan makes.
- One loop inside a loop that counts every pair of taps.
- Two parallel lists that count taps per card, and count their own comparisons.
- One dictionary that maps card ID to tap count, and one set of unique stations.
- One JSON file, `tap_summary.json`, that you write, reload and check.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Count what a Linear Scan costs on 5, 10, 20 and 40 rows. Then say what it and a nested pair loop would cost on 400 rows.
  - *Assessed today: Algorithmic Complexity (Big-O), Control Flow & Loops*
- **Day 2**: Count taps per card twice, with two parallel lists and then a Dictionary, and compare the work each one does. Use a Set for the stations.
  - *Assessed today: Algorithmic Complexity (Big-O), Control Flow & Loops, Data Structures Selection*
- **Day 3**: Save the summary as JSON and read the error a Set causes. Fix it. Then reload the file and check which types came back.
  - *Assessed today: Control Flow & Loops, AI Output Validation*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Algorithmic Complexity (Big-O) and Control Flow & Loops.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** Counting the work, not guessing at it. Every search here reports how many records it looked at.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- Before the Dictionary version, each of you writes down a predicted lookup count on your own. Then compare the two guesses.
- Swap who types between the parallel-lists version and the Dictionary version. Whoever wrote the slower one defends it in the shareout.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 6)
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

**Make it explain the output** (Algorithmic Complexity (Big-O)) · Technique: **Make it explain**, you learned this in Module 0

```text
I counted comparisons for two versions of the same tap count on one
day's log. Parallel lists: [your count]. Dictionary: [your count]. Rows in
the log: [your row count].

Explain why these two numbers grow differently as the log gets longer.
Use my numbers, not a general rule.
```

**Check:** Ask it to predict both counts for 400 rows, then check its answer against your own arithmetic from Step 2.

**Validate against your own work** (Control Flow & Loops) · Technique: **One-shot prompting**, you learned this on Day 5

```text
A scan walks a list from the top and stops at the first match. For each
case, tell me how many comparisons it makes. Answer in exactly this
shape:

Example: list A, B, C, find B | comparisons: 2 | found: yes

Now do these:
list K, L, M, N, find K
list K, L, M, N, find N
list K, L, M, N, find Z
```

**Check:** Work all three on paper first, then run your `scan_for()` on `taps[:4]` and compare all three answers.

**Prompt to understand** (AI Output Validation) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Which Python types can JSON hold, and which can it not? Use a small
made-up dictionary as the example, not my code. Name the docs page that
lists the conversions.
```

**Check:** Find the conversion table on that docs page and check the type of the key that broke in Step 5 against it.

**Spell out the spec** (Data Structures Selection) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Question my container choices. Do not write code.

Context: I am counting taps per card and listing the unique stations
from one day's transit log.

Evidence: Here is each job, the container I picked for it, and why:
[paste each job, your container, and your one-line reason]

Output: Ask me 2 questions about how each job looks things up. Then
name one job where my choice would stop being the right one.
```

**Check:** Answer its questions with your own numbers from Step 4, and keep any choice your numbers back up.

</details>

## The Data

- **File:** `station_taps.csv` (CSV)
- **Where it comes from:** Created for this challenge.
- **Setup:** Put `station_taps.csv` in the same folder as your `pick-the-right-container_STUDENT.py`, or edit `DATA_FILE` at the top to its path.

The top of your .py already reads the file for you. `header` is the first row and `taps` is every row after it. Each row is a list of strings. A `FileNotFoundError` means `DATA_FILE` does not point at the file yet.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 6)

### Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs

1. **Predict** how many comparisons a scan makes to find `T001`, `T040` and `T999`. A tap's row number is the number in its ID, and `T999` is not in the file.
2. **Write one function, `scan_for(tap_id, records)`,** with one loop that goes through every row in `records`. (`def` from Day 3; `for` from Day 1)
3. **Add 1 to `comparisons` for every row,** before you check it.
4. **Return `comparisons` the moment `row[0]` equals `tap_id`.** The ID is the row's first field. (`row[0]` from *Trace the Path*, Step 1; `return` from Day 3)
5. **Return `comparisons` after the loop too,** so a tap that is never found still reports its work.
6. **Run the file** and compare the three printed counts with your predictions.

*Work under `# Step 1` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Before you run: your predicted counts for T001, T040 and T999, and how you got each.
2. Which of the three counts should you plan around, and why?

<details>
<summary>Stuck? Open this.</summary>

`scan_for("T001", taps)` must return 1, and `scan_for("T999", taps)` must equal `len(taps)`. If `T001` comes back the same as `T999`, your `return` is not inside the `if`. If `T999` comes back 0, your counter only moves on a match, so move it above the `if`.

</details>

### Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop

1. **Write every count down first** with its arithmetic: the scan at 5, 10, 20 and 40 rows, the pair loop on 40 rows, then both on 400 rows.
2. **Read the given loop over `[5, 10, 20, 40]`.** It runs `scan_for("T999", ...)` on the first `size` rows. Inside it, print `size` and `worst`.
   - **New: `[:n]`** (slicing) gives a new list holding the first `n` items. `[4, 7, 9][:2]` gives `[4, 7]`. It's written for you in Step 2 of your .py; you'll write it yourself next time.
3. **Write one loop inside a loop** that pairs every tap with every tap, itself included, and adds 1 to `pairs` each time. (`nested loops` from Day 2)
4. **Print the cost of both on 400 rows** using `len(taps) * 10`, since there is no bigger file.
5. **Say each pattern in one sentence:** one for the scan, one for the pair loop.

*Work under `# Step 2` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Before you run: every count you expect, with the arithmetic beside it.
2. The scan's pattern in one sentence, then the pair loop's, with no notation.

<details>
<summary>Stuck? Open this.</summary>

Count a tiny pair loop by hand. List every `(a, b)` pair for 3 rows, then for 4 rows, and compare each pair count with its row count. Then run your nested loop on `taps[:3]` and `taps[:4]` to check.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Share which of your three `scan_for()` counts you would plan around, and why `T999` costs as much as `T040`.
- Explain how you wrote and tested `scan_for()`. Which call did you check by hand first?
- How did the scan and the pair loop each change when the rows went from 40 to 400?

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 7)

### Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons

1. **Predict the comparison count** before you write the loops.
2. **Make two empty lists:** `card_ids` for each card in the order you first see it, and `tap_counts` for that card's count at the same position.
3. **Write one loop over `taps`** that sets `card` to the row's card ID, `row[1]`, and `found` to `False`.
4. **Inside it, write one loop over the positions in `card_ids`** that adds 1 to `comparisons` for every check. (`range()` from Day 1; `len()` from *Trace the Path*, Step 3)
5. **On a match,** add 1 to `tap_counts` at that position, set `found` to `True`, and `break`. (`break` from Day 1)
6. **With no match,** append the card to `card_ids` and `1` to `tap_counts`, so both lists stay the same length. (`.append()` from *Trace the Path*, Step 3)
7. **Run it.** The given `busiest` line finds the card with the most taps.
   - **New: `max()`** gives the largest item in a list. `max([3, 8, 5])` gives `8`. It's written for you in Step 3 of your .py; you'll write it yourself next time.
   - **New: `.index()`** gives the position of the first matching item. `[3, 8, 5].index(8)` gives `1`. It's written for you in Step 3 of your .py; you'll write it yourself next time.

*Work under `# Step 3` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. Before you run: how many comparisons do you expect?
2. After: the real count, and why it is bigger than the number of rows.

<details>
<summary>Stuck? Open this.</summary>

Count `C001`'s rows in the file by eye, then compare with `tap_counts[card_ids.index("C001")]`. If the totals are right but your comparison count differs from another group's, check whether your inner loop has a `break`.

</details>

### Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set

1. **Predict `lookups`** from the rule, not the file: a dictionary goes straight to a key.
2. **Make one dictionary, `taps_by_card`,** that maps each card ID to its tap count, with one loop over `taps` that adds 1 to `lookups` per row. (`dict` and `in` from Day 7)
3. **Make one set, `stations`,** and `.add()` each row's station, `row[2]`. Write no `if not in` check, because a set keeps only distinct values. (`set()` and `.add()` from Day 7)
4. **Write one loop over `taps_by_card`** that counts the cards with more than 1 tap into `repeat_riders`.
5. **Run it** and put `lookups` next to your Step 3 comparison count.
   - **New: `sorted()`** gives a new list with the items in order. `sorted({"b", "a"})` gives `['a', 'b']`. It's written for you in Step 4 of your .py; you'll write it yourself next time.

*Work under `# Step 4` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. Before you run: your `lookups` prediction and the rule behind it.
2. Finish "As the Input Size grows..." for the parallel lists, then for the dictionary.
3. For each container, name its job and how it finds what it needs. What would a list have cost you for `stations`?
4. Which card explains the gap between distinct cards and repeat riders?

<details>
<summary>Stuck? Open this.</summary>

Count `C001`'s rows in the file by eye and compare with `taps_by_card["C001"]`. If `stations.add(row)` raises `TypeError: unhashable type: 'list'`, you added the whole row instead of one field.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share your parallel-lists comparison count and your Dictionary `lookups` count. If another group got different numbers, find where your loops differ.
- Explain how `taps_by_card` and `stations` each find what they need without a scan.
- How did the two counts together answer which container the agency should use? Start with "As the Input Size grows..."

Be ready to answer **"why did you do it that way?"**

## Day 3 (Module Day 8)

### Step 5: Save the Summary as JSON and Read the TypeError a Set Causes

*Expect this step to raise `TypeError`. That is the point, not a bug.*

1. **Fill in the four `None` values** in `summary` from your Day 2 work. Keep `stations` a set for now.
2. **Run the file** and read the whole error before you change anything. (`json.dumps()` from Day 8)
3. **Name the key that broke and why,** in your own words, before you look anything up.
4. **Put `#` in front of** the `json.dumps` line and the `print(text)` line so Step 6 can run.

*Work under `# Step 5` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 5, answer 1:` in the .py, and so on:

1. The last line of the error, exactly as printed.
2. Which key caused it, and why, in your own words.
3. Did `about to serialize` print before the error? What does that tell you?

<details>
<summary>Stuck? Open this.</summary>

The error names a type. Add `for key in summary: print(key, type(summary[key]))` above the `json.dumps` line and find the value whose type matches the message.

</details>

### Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived

1. **Change `summary["stations"]`** into a type JSON can hold. Keep the key, because the agency asked for it. (`sorted()` from Step 4)
2. **Write `summary` to `tap_summary.json`** with `json.dump()` inside a `with open(..., "w")` block. (`json.dump()` from Day 8; `with open()` from Day 1)
3. **Read it back into `reloaded`** with `json.load()` in a second `with open(...)` block. (`json.load()` from Day 8)
4. **Open `tap_summary.json` in your editor** and read it. It is plain text.
5. **Run the five given prints** and compare each type with the one you built on Day 2.
   - **New: `.__name__`** on a type gives that type's name as text. `type([1, 2]).__name__` gives `list`. It's written for you in Step 6 of your .py; you'll write it yourself next time.

*Work under `# Step 6` in `pick-the-right-container_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 6, answer 1:` in the .py, and so on:

1. Can the overnight job get one card's count from this file without the raw log? How do you know?
2. Which container survived the round trip, and which came back as something else?

<details>
<summary>Stuck? Open this.</summary>

Print `type(stations)` next to `type(reloaded["stations"])`. Then run `reloaded["stations"].append("Union Sq")` and print its length. Would your Day 2 `stations` have let that happen?

</details>

### Share Out: Day 3

**Last 15 minutes, back together as a class. Bring:**

- Share the `TypeError` message and which key caused it, in your own words.
- Explain how you fixed it, and how you proved `tap_summary.json` held what you wrote.
- How did the round trip change `stations`, and what does the overnight job lose because of it?

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `pick-the-right-container_STUDENT.py` (you may rename it `pick-the-right-container.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
