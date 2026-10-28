# Data Challenge: Lookups Matter

**GitBook quest:** [Quest 1.9: Lookups Matter](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-09-big-o-practice) (quest runs Days 16-17)

**Vocabulary from the reading** (use these words in your shareout): `Linear Search`, `Dictionary Lookup`, `Input Size`, `O(n)`, `O(1) Average-Case`, `Scale`, `Complexity`

**Skills assessed:** Algorithmic Complexity (Big-O), Critical Thinking, AI Output Validation, Data Structures Selection (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes (15 min intro · 30 min group work · 15 min shareout)

## Scenario

Brightwork Makerspace runs four locations off one member directory. Every
badge swipe at the front door asks one question: is this ID a member?
You count what a whole morning of swipes costs with a linear search and
with a dictionary, then use your totals to check an AI's speed claim.

**You will build**

- One function, `find_linear()`, that returns a member's row and the comparisons it took.
- One loop that goes through every swipe and totals the morning's comparisons.
- One dictionary, `members_by_id`, that maps member ID to row, and counts its own build cost.
- One loop that races the two searches and finds the swipe where the dictionary pulls ahead.
- One verdict, in your own words, on an AI's claim about how much faster a dictionary is.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **This day**: Count a whole morning of swipes both ways, including the dictionary's build cost, and find the swipe where it pays off. Then use your totals to check an AI's speed claim.
  - *Assessed today: Algorithmic Complexity (Big-O), Critical Thinking, AI Output Validation, Data Structures Selection*

## Ground Rules

- **Do not use AI to write the code.** This challenge grades Algorithmic Complexity (Big-O) and Critical Thinking.
- **Use AI to understand, then check what it says.** The AI Toolkit below shows how.
- **New here:** You hold your own totals, so you can check a speed claim instead of taking it on faith. Step 4 does that, and it is graded.
- **Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Working as a pair</summary>

- Before Step 2 runs, each of you writes your own predictions. Compare them, then run.
- One of you drives the linear search, the other the dictionary. Whoever did not type a search explains its numbers in the shareout.
- Each of you submits your own copy, and has to be able to explain it alone.

</details>

## AI Toolkit

<details>
<summary>Open when you use AI: prompts to try and how to check what comes back</summary>

> **AI techniques you have so far** (taught by Day 16)
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

**Spell out the spec** (Algorithmic Complexity (Big-O)) · Technique: **Plan mode**, you learned this on Day 12

```text
Plan only. Do not write code, and do not give me a final number.

I search a list of members by walking it from the top. I could build a
dictionary keyed on member ID first instead. Building it touches every
row once. List the steps, one line each, to work out by hand when the
dictionary does less total work for N swipes on a list of M members.
```

**Check:** Follow its plan with your own counts from Steps 2 and 3, and see if it lands on the same pay-off swipe your code printed.

**Prompt to understand** (Critical Thinking) · Technique: **Prompt to understand**, you learned this in Module 0

```text
In plain words, what does O(n) mean, and what does O(1) average case
mean? Use a phone contacts list as the example, not code.
```

**Check:** Restate each one in a single sentence that uses a count you measured yourself.

**Validate against your own work** (AI Output Validation) · Technique: **XML tags**, you learned this on Day 12

```text
<question>
What is the average-case cost of looking up a key in a Python
dictionary, and what is the worst case?
</question>

<output>
Both costs, and the source for each one. Say which page of the source
I should read.
</output>
```

**Check:** Open the source it names and find the line that gives each cost.

**Spell out the spec** (Data Structures Selection) · Technique: **Task, Context, Evidence, Output (TCEO)**, you learned this on Day 5

```text
Task: Question my choice of container. Do not write code.

Context: A front door asks one question on every badge swipe, all
morning: is this ID a member? The directory starts as a list of
member records.

Evidence: Here is the container I built for that question, the key I
used, and why:
[paste your members_by_id loop and your one-line reason]

Output: Ask me 2 questions about how the door looks members up. Then
name one morning where a plain list would be the better choice.
```

**Check:** Check its list-is-better morning against your Step 3 race. Would the dict have paid off by the end of that morning?

</details>

## The Data

- **File:** `member_directory.csv` (CSV)
- **Second file:** `door_checkins.txt` (TXT)
- **Where it comes from:** Both files were created for this challenge. No real person is in either one.
- **Setup:** Put `member_directory.csv` and `door_checkins.txt` in the same folder as your `lookups-matter_STUDENT.py`, or edit `DATA_FILE` and `CHECKINS_FILE` at the top to their paths.

The top of your .py already reads the directory for you. `members` is a list with one dictionary per row, keyed by column name, so `members[0]["member_id"]` is `"M1001"`. Step 2 reads the second file, `CHECKINS_FILE`, itself. A `FileNotFoundError` means a constant at the top does not point at its file yet.

**Before you write any code, open the file with your partner and answer these together:**

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

## Steps

### Step 1: Write `find_linear()` to Return the Member and Its Comparisons

1. **Predict the count for `M1150`.** IDs run in order from `M1001`, so a member's row number is the ID minus 1000.
2. **Write one function, `find_linear(members, member_id)`,** with one loop that adds 1 to `comparisons` for every row it checks. (`def` from Day 3; `for` from Day 1)
3. **Return two things when the ID matches:** the row and the count. When nothing matches, return `None` and the count. (`return a, b` from *Validate, Catch, Keep Going*, Step 1; `None` from Day 3)
4. **Run the file** and compare the count with your prediction.

*Work under `# Step 1` in `lookups-matter_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 1, answer 1:` in the .py, and so on:

1. Before you run: your predicted count for `M1150`, and how you got it.

<details>
<summary>Stuck? Open this.</summary>

Look up `M1001` and `M1002`: they should report 1 and 2. If both report the same count, move the counter above the `if`. Then look up `M9999` and check that you get a count back, not a bare `None`.

</details>

### Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`

1. **Open `door_checkins.txt` with your partner.** How many swipes are there, and do any look odd?
2. **Predict three costs** with the ID-minus-1000 rule: each of the first three swipes, their sum, and a swipe that is not a member.
3. **Read the swipes into one list, `swipes`,** inside a `with open(CHECKINS_FILE)` block. (`with open()` from Day 1; `.splitlines()` from *One Job at a Time*, Step 1)
4. **Write one loop over `swipes`** that calls `find_linear()` and prints a line like `M1004 | Dev Okafor | comparisons: 4`, or `M1313 | NOT A MEMBER | comparisons: 312` when there is no row. (`a, b = f()` from *Validate, Catch, Keep Going*, Step 1)
5. **Total the morning:** add every count to `linear_total`, and count the swipes that are not members.

*Work under `# Step 2` in `lookups-matter_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 2, answer 1:` in the .py, and so on:

1. Before you run: the cost of each of the first three swipes, their sum, and the cost of a swipe that is not a member.
2. Which swipe cost the most, and why?

<details>
<summary>Stuck? Open this.</summary>

The first swipe is `M1004`, so it should cost 4. Every `NOT A MEMBER` line should cost exactly `len(members)`. If your total looks too small, print `linear_total` inside the loop and watch it grow.

</details>

### Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off

1. **Predict the pay-off swipe** from your Step 2 counts and a build cost of one step per member.
2. **Make one dictionary, `members_by_id`,** that maps each member ID to its row, with one loop that adds 1 to `build_steps` per row. (`dict` from Day 7)
3. **Write one function, `find_dict(members_by_id, member_id)`,** that returns the row and a count of `1`. There is no loop inside it to count. (`.get()` from Day 16)
4. **Race the two searches with one loop over `swipes`.** The linear total starts at 0. The dictionary total starts at `build_steps`, because you paid that before the first swipe. The two `_, ... =` lines that run each search are given. Print a line per swipe like `swipe 1 M1004 | linear so far: 4 | dict so far: 313`.
   - **New: `_`** is a variable name for a value you will not use. `_, count = find_linear(members, "M1001")` keeps only the count, `1`. It's written for you in Step 3 of your .py; you'll write it yourself next time.
5. **Save the number of the first swipe where the dictionary total is lower** in `pays_off_at`. (`is None` from Day 3)

*Work under `# Step 3` in `lookups-matter_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 3, answer 1:` in the .py, and so on:

1. Before you run: at which swipe does the dict total first drop below the linear total?
2. Why a dictionary keyed on `member_id` fits the door's job. Quote the swipe where it pulled ahead.
3. A morning where the plain list would be the better choice.

<details>
<summary>Stuck? Open this.</summary>

After swipe 1, the dictionary total should be your build cost plus 1, and the linear total should be 4. If the dictionary wins at swipe 1, you started `dict_running` at 0 and left out the build.

</details>

### Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict

1. **Ask an AI tool** how much faster a dict lookup is than a linear search. Ask about 20 lookups in a list of 312 rows.
2. **Paste its claim into `ai_claim`, word for word.**
3. **Get three comparisons:** the first swipe alone, one non-member swipe alone, and the whole morning with the build cost. (`_` from Step 3; `swipes[0]` from *Trace the Path*, Step 1; `round()` from *Validate, Catch, Keep Going*, Step 4)
4. **Ask the AI whether its number counted the build cost.** Then paste your totals back and see if it changes its number.
5. **Write `verdict` in your own words.** Name `O(n)` and `O(1) Average-Case`, and quote at least one of your counts.

*Work under `# Step 4` in `lookups-matter_STUDENT.py`.*

**Answer in writing.** Type answer 1 as `#` comments under `# Step 4, answer 1:` in the .py, and so on:

1. Hold the AI's claim against your three comparisons. Which one did it match, and which did it miss?
2. Did its number count the cost of building the dictionary? What did it say when you pasted your totals back?

<details>
<summary>Stuck? Open this.</summary>

Work out three ratios by hand: the first swipe's count over 1, a non-member's count over 1, and your linear morning total over your dictionary total. If the AI's number matches only one of them, say which.

</details>

## Share Out

**Last 15 minutes, back together as a class. Bring:**

- Share your three numbers: the linear total, the dictionary total with its build cost, and the swipe where the dictionary pulled ahead.
- Explain how you checked the AI's claim. Quote it, give your verdict, and name the one total that settles it.
- How did `find_linear()` and `find_dict()` together answer when the door should build the dictionary? Describe a morning where it is not worth it.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `lookups-matter_STUDENT.py` (you may rename it `lookups-matter.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
