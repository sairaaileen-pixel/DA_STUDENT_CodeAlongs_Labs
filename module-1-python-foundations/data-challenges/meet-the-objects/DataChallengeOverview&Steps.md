# Data Challenge: Meet the Objects

**GitBook quest:** [Quest 1.8: Meet the Objects](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-08-oop) (quest runs Days 13-15)

**Vocabulary from the reading** (use these words in your shareout): `Object-Oriented Programming (OOP)`, `Class`, `Object`, `Instance`, `Attribute`, `Method`, `self`, `__init__`, `__str__`, `__repr__`

**Skills assessed:** Object-Oriented Programming, Functions & Modular Programming, Collaboration (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 2 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 2.** The rubric grades all 2 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

A bike-share dispatcher decides each morning where to send help. Vans go
to stations that are nearly empty or jammed full, and a mechanic goes to
stations that need one. Their old report kept station names
and bike counts in two lists, lined up by position. Somebody removed a
station from one list, and the report has been quietly wrong ever since.

**You will build**

- Two parallel lists, `names` and `bikes`, that rebuild the broken report.
- One class, `Station`, with an `__init__` and one method, `needs_restock()`.
- One list, `fleet`, that holds one `Station` for every record in the file.
- Two display methods, `__str__()` and `__repr__()`, added to `Station`.
- One list, `van_list`, of the stations that need bikes, printed two ways.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Reproduce the parallel-list bug and name the stations it gets wrong. Then build a `Station` class and prove two Instances keep their own Attributes.
  - *Assessed today: Object-Oriented Programming, Functions & Modular Programming, Collaboration*
- **Day 2**: Add `__str__` and `__repr__`, and find out which one a list uses. Then print the dispatcher's van list once for you and once for them.
  - *Assessed today: Object-Oriented Programming, Collaboration*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Object-Oriented Programming and Functions & Modular Programming.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** You are designing something, not tracing it. What gets judged is whether each attribute you keep traces back to a phrase the dispatcher used.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- Each of you drafts an attribute list alone, with the dispatcher's phrase beside each one. Then compare and agree on one.
- Swap drivers between the two days. On Day 2 the partner who is not typing tells the driver each prediction before anything runs.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 13)
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

**Validate against your own work** (Object-Oriented Programming) · Technique: **Verify against your own work**, you learned this in Module 0

```text
Here is the dispatcher's request:
[paste it]
Here is my attribute list for a Station class:
[paste it]

For each attribute, quote the phrase in the request that justifies it.
Flag any attribute you cannot tie to a phrase. Do not write the class.
```

**Check:** Find each quoted phrase in the scenario yourself, and drop any claim that quotes words that are not there.

**Make it explain the output** (Object-Oriented Programming) · Technique: **Make it explain**, you learned this in Module 0

```text
Here is my Station class and the four lines my prints produced:
[paste the class]
[paste the four printed lines]

For each line, explain which method Python used to make that text, and
why. Which Python docs page says so?
```

**Check:** Print one Station, then a list of two, and see if its explanation matches what you get.

**Prompt to understand** (Functions & Modular Programming) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Explain what self is in a Python method. Use a Dog class with a name
and an age, not my code. Why would a method read a number from self
instead of taking it as a parameter?
```

**Check:** Change one station's bike count and call `needs_restock()` on two stations: only one answer should move.

**Ask for tests and edge cases** (Collaboration) · Technique: **XML tags**, you learned this on Day 12

```text
<task>
Give us 4 short dispatcher questions to test two attribute lists
against. Do not pick a list for us, and do not write code.
</task>

<request>
[paste the dispatcher's request]
</request>

<list_a>
[paste one partner's list]
</list_a>

<list_b>
[paste the other partner's list]
</list_b>

<output>
For each question, name the attributes it needs. We decide which list
can answer it.
</output>
```

**Check:** Run each question against both lists together, and agree on one list you can each defend.

</details>

## The Data

- **File:** `bike_stations.json` (JSON)
- **Where it comes from:** Created for this challenge.
- **Setup:** Put `bike_stations.json` in the same folder as your `meet-the-objects_STUDENT.py`, or edit `DATA_FILE` at the top to its path.

The top of your .py already reads the file for you. `stations` is a list with one dictionary per station. Open the file to see which fields each station holds. A `FileNotFoundError` means `DATA_FILE` does not point at the file yet.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Day 1 (Module Day 13)

### Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations

1. **Try `.pop(2)` on a short list of your own** and print the list before and after.
   - **New: `.pop()`** removes the item at a position and hands it back. After `nums = [4, 7, 9]`, `nums.pop(1)` gives `7` and leaves `nums` as `[4, 9]`. It's written for you in Step 1 of your .py; you'll write it yourself next time.
2. **Make two lists, `names` and `bikes`,** with one loop over `stations` that appends each station's `"name"` and `"bikes_available"`. (`.append()` from *Trace the Path*, Step 3; `dict["key"]` from Day 7)
3. **Read the `names.pop(2)` line.** It removes the third station from `names` only, the way somebody tidying up at the end of a shift would.
4. **Write one loop over `range(len(names))`** that prints each name beside the bike count at the same position. (`range()` from Day 1; `len()` from *Trace the Path*, Step 3)
5. **Check the report against the file, station by station.** Nothing raises an error, so your eyes are the only check.

*Work under `# Step 1` in `meet-the-objects_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Describe the data file in two or three sentences. What is one record? Which fields are numbers, and which are text? What looks wrong?
2. What `.pop(2)` removes, what it hands back, and what happens to the positions after it.
3. Which stations got a bike count that was never theirs? Whose real count does nobody see?

<details>
<summary>Stuck? Open this.</summary>

Add a second loop that prints `stations[i]["name"]` and `stations[i]["bikes_available"]`. Line the two printouts up, find the first line where they disagree, then check every line after it.

</details>

### Step 2: Define the Station Class and Prove Two Instances Are Independent

1. **Draft your own attribute list on paper, alone,** with the dispatcher's phrase beside each one. Then compare with your partner and agree on one list.
2. **Write one class, `Station`,** with an `__init__` that takes `name` (text), `capacity` and `bikes_available` (whole numbers), plus any field your list keeps. (`class`, `__init__` and `self` from Day 13)
3. **Write one method, `needs_restock()`,** that returns `True` when the station holds fewer bikes than a quarter of its capacity. Read both numbers from `self`, not from parameters.
4. **Build one list, `fleet`,** with one loop that makes a `Station` from every record, passing any extra field you added.
5. **Pick two stations whose `needs_restock()` answers match.** Print both, set one station's bike count to 0, and print both again. Exactly one answer should move.

*Work under `# Step 2` in `meet-the-objects_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Your own list, made before you compared. Put the dispatcher's words beside each attribute.
2. Where your two lists differed, what each of you argued, and which list you kept.
3. Which field from the file you left out, and why the dispatcher does not need it.
4. Why your two stations prove independence, with their answers before and after.

<details>
<summary>Stuck? Open this.</summary>

`self` is the Object the method was called on. Print `fleet[0].name` and `fleet[0].needs_restock()` and say which station `self` was. If your two stations already disagree before the change, pick another pair.

</details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- Name every station that got a bike count that was never its own, and the one real count nobody sees.
- Explain how you created and tested `needs_restock()`. Which two stations did you check, and why could they prove anything?
- Share one attribute you kept with the dispatcher's phrase behind it, and one field you left out.

Be ready to answer **"why did you do it that way?"**

## Day 2 (Module Day 14)

### Step 3: Add `__str__` and Find Out Which of Four Prints It Changes

1. **Predict the shape of all four prints** before you run anything. The first two run before you add `__str__`. (`[:n]` from *Pick the Right Container*, Step 2)
2. **Copy your `Station` class into this step** and add one method, `__str__()`, that returns text like `Grand Army Plaza: 6 of 48 bikes`. (`__str__` from Day 14; `f-strings` from Day 7)
3. **Rebuild `fleet` from the new class,** right below it. Stations built from the old class keep the old behavior.
4. **Run the file** and compare the four prints with your predictions.

*Work under `# Step 3` in `meet-the-objects_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. Before you run: the shape you expect from each of the four prints, in order.
2. Which prediction was wrong, and which method does a list use instead of `__str__`?

<details>
<summary>Stuck? Open this.</summary>

Before you decide your `__str__` is broken, print `str(fleet[0])` and `repr(fleet[0])`. Compare each with what the list showed for that same station.

</details>

### Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher

1. **Agree with your partner what each display method is for.** One reader wants the answer. The other wants to know which object they are holding.
2. **Predict how many stations need a van** by comparing each `bikes_available` in the file with a quarter of its `capacity`.
3. **Copy your class into this step** and add one method, `__repr__()`, that returns text like `Station('Grand Army Plaza', 6)`. (`__repr__` from Day 14)
4. **Rebuild `fleet`, then build one list, `van_list`,** with one loop that appends every station whose `needs_restock()` returns `True`.
5. **Run the two given prints:** the whole list first, then one station per line.

*Work under `# Step 4` in `meet-the-objects_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. Before you run: how many stations land in `van_list`, and which method `print(van_list)` will use.
2. What each display method is for, and who reads it.
3. Which printout you would hand the dispatcher, and why.

<details>
<summary>Stuck? Open this.</summary>

If `print(van_list)` still shows `object at 0x...`, print `repr(van_list[0])`. If that shows the address too, your `fleet` was built from the old class, so rebuild it below the new one.

</details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- Share your four Step 3 predictions, including the one that turned out wrong.
- Explain how your two van-list printouts prove which method a list uses.
- How did `__str__()` and `__repr__()` together serve both the dispatcher and you? Say who reads each one.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `meet-the-objects_STUDENT.py` (you may rename it `meet-the-objects.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
