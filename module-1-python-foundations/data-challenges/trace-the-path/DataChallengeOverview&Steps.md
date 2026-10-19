# Data Challenge: Trace the Path

**GitBook quest:** [Quest 1.1: Trace the Path](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-01-control-flow) (quest runs Days 1-2)

**Vocabulary from the reading** (use these words in your shareout): `Conditional`, `Iteration`, `Loop`, `Loop Body`, `Nested Loop`, `Off-by-One Error`

**Skills assessed:** Control Flow & Loops, Attention to Detail, Collaboration (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 2 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 2.** The rubric grades all 2 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

You volunteer at the Riverside Community Center. The shift log there is a
plain text file, typed by hand at the end of each day. The coordinator
wants three numbers out of that log:

- How many long shifts got worked?
- How many hours did the week come to?
- How many cells does a grid of every volunteer against every weekday
  need?

**What you already did, and what is different here.** Quest 1.1 had you
trace loops and conditionals over short examples the reading picked, with
the right answer printed a paragraph later. Here the file is real, nobody
tells you what is in it, and the last step hands you a loop that runs
clean, raises nothing, and still drops a record. Same loops. Data you have
to inspect first, and no answer key on the page.

So the rule for these two days: **you say what your code will print
before you run it**. Every step asks for a written prediction first. You
run the code to check whether you read it right, not to find out what it
does.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Trace one loop with a conditional inside it, by hand. Predict the exact output, then run the loop and account for any difference. Follow one variable's value through every pass.
  - *Assessed today: Control Flow & Loops, Attention to Detail*
- **Day 2**: Predict how many times a nested loop's inner body runs, before you run it. Then find an off-by-one error and fix it. That bug drops a record quietly, with nothing raised at all.
  - *Assessed today: Control Flow & Loops, Attention to Detail, Collaboration*

## Ground Rules

**Do not use AI to write the code.** This challenge grades Control Flow & Loops and Attention to Detail. If AI writes it, nothing has been measured.

**Use AI to understand, then check what it says.** The AI Toolkit below shows how, one skill at a time.

**New here:** `.split(",")`, which step 1 has you research as a team. The loops and conditionals are the LiveLab's; the file is new, and nobody tells you what is in it.

**Swap driver and navigator every step.** Whoever is not typing asks the questions.

<details>
<summary>Using AI, and working as a pair - the standing rules</summary>

**AI is for understanding, not for answers.**

- Fair game: explain a concept, explain an error message, show you a *different* example than the one you need.
- Not fair game: pasting the task in and shipping what comes back. If you cannot explain a line without the screen, you do not have it.
- Always run it, and check it against a case you worked out by hand. AI will hand you code that runs and is wrong. That is the exact thing this module trains you to catch.

**How to challenge an explanation.** Ask for the source and go read it. Ask "what would make that wrong?" Ask the same question a second way in a new chat and see whether the answer holds. An answer that changes when you rephrase the question was never knowledge.

**If you do end up with AI-written code, interrogate it before you keep a line of it.**

- Ask it to explain the code line by line, then check that story against what the code does when you run it.
- Ask "what input breaks this?" Then feed it that input. An empty list, a missing field, a zero, a name that is not there.
- Hand it a case you worked out by hand and ask it to predict the output. If its prediction disagrees with your arithmetic, one of you is wrong and you need to know which.
- Ask for a second, different approach, then make it argue against the first one. Keep whichever you can defend yourself.

**Working as a pair.**

- The navigator owns the questions: "Why that comparison?" "What happens on the last row?"
- Say *why* before you agree. If neither of you can give a reason, test both ways.
- Go through AI output together, line by line, and say what each line does. Never one person pasting and the other nodding.
- Each of you submits your own copy, and has to be able to explain it alone.

- Predict separately, in writing, *before* comparing. Predict together and you will just converge on whoever sounds more confident. Then you both learn nothing when you are both wrong.
- When your predictions differ, do not run the code to settle it yet. Each person first says which line makes them think that. The disagreement is the most useful 90 seconds of the day.

</details>

> **AI techniques you have so far** (taught by Day 1)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.
>
> The tips below use only these.

## AI Toolkit

Each tip below pairs one skill this challenge grades with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Prompt to understand** (Control Flow & Loops) · Technique: **Prompt to understand**, you learned this in Module 0

```text
I am learning Python loops. Explain what range(len(my_list) - 1) loops
over. Use a list of 4 made-up names as the example, and list every value
i takes. Then name the Python docs page that explains where range stops.
Do not look at or fix any code of mine.
```

**Check:** Write out the values of `i` for a 4-item list yourself first. Then open the docs page it names and find the sentence about where `range` stops. If the page does not exist or does not say that, do not trust the rest.

**Make it explain the output** (Control Flow & Loops) · Technique: **Make it explain**, you learned this in Module 0

```text
Here is my loop and the first three rows of the file it reads:
[paste your step 1 loop]
[paste three rows]

Before anything runs, walk me through each pass. For every pass, tell me
the value of hours, whether the if test is true, and the counter after
that pass.
```

**Check:** Hold its pass-by-pass story against your own hand count of those three rows, then run your code. Where its story and the real run disagree, the run wins. Ask it which pass it got wrong.

**Validate against your own work** (Attention to Detail) · Technique: **Verify against your own work**, you learned this in Module 0

```text
Here are the first three rows of a volunteer shift log:
[paste three rows]

Count how many have 4 or more in the third field. Show the number you
read from each row before you give the count.
```

**Check:** Do those three rows by hand and write your count down before you ask. If the two counts differ, find the row where you disagree and reread the rule. Is a 4 counted or not?

**Validate against your own work** (Attention to Detail) · Technique: **Verify against your own work**, you learned this in Module 0

```text
Here is a made-up list of 5 shift lengths: 3, 8, 4, 6, 2.

List every item with its position, starting from 0. Then tell me how
many items the list holds.
```

**Check:** Write the positions yourself before you ask. Then print every position your own Day 2 loop reaches on the real file. Any position you wrote that the loop never reaches is a record that went missing.

**Prompt to understand** (Collaboration) · Technique: **Prompt to understand**, you learned this in Module 0

```text
My partner and I disagree about how many times this nested loop runs:
[paste the nested loop]
[paste both of your predictions]

Do not tell us who is right. Ask each of us one question that would help
us find out for ourselves.
```

**Check:** Answer its questions on paper as a pair, then run the code. Bring to the shareout whose reasoning held up, and which question helped most.

## The Data

- **File:** `data/volunteer_shifts.txt` (TXT)
- **Where it comes from:** Created for this challenge.

**Before you write any code, open the file and look at it.** You will not be told what is in here. Finding out is the first part of the work. Answer these three:

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

*Answer them at the top of `trace-the-path_STUDENT.py`, under THE DATA.*

Quest 1.1 is about predicting what code does before you run it. Loading
the file is **not** the work here, so this is the line that does it.
Paste it and move on. A later LiveLab explains what `open()` is
actually doing.

```python
with open("data/volunteer_shifts.txt") as f:
    shifts = [line for line in f.read().splitlines()
              if line and not line.startswith("#")]
```

What `shifts` ends up holding is yours to work out. Open the file and
read it. A `FileNotFoundError` means you are running from the wrong
folder. Check where the file actually sits relative to the folder you ran `python3` from.

## Your Objectives

## Day 1

- **Step 1: Count the Shifts of 4+ Hours, Prediction First**
  - *The coordinator counts any shift of 4 hours or more as a long shift.*
    1. **Research `.split(",")` as a team.** It is new, and the line that pulls out `hours` uses it. Look it up, then run it on one line of this file and print what comes back. **Under `# Your answer:`, type 2-3 bullets**: what `.split()` hands back, what the `","` controls, and where you found that out.
    2. **Predict the count by reading the file, not the code.** You opened `data/volunteer_shifts.txt` above and it holds 12 shift rows. Read the third field on each row and count the rows where it is 4 or more. Write that one number in a comment at the top of this step, before you run a single line.
    3. **Write the test for a long shift** in the first TODO. "4 hours or more" is the rule, word for word.
    4. **Write the counting line** in the second TODO, moving `long_shifts` on by one.
    5. **Run it, and compare the printed count** against the number in your comment.

  *If the two differ, say which line you mis-read. Do not edit the prediction.*

  *Work in `trace-the-path_STUDENT.py` under Step 1: complete its TODOs. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  If the printed count does not match your comment, add `print(shift, hours >= 4)` on the line just under `hours = ...`, inside the loop. Run it, then go down the printed lines and compare each `True` or `False` against the rows you counted by hand. The first row where they disagree shows you whether the code or your reading is off.

  </details>

- **Step 2: Total the Week's Hours, Printing the Running Total Each Pass**
  - *You already wrote a loop that counts. This one adds up instead, and you watch the variable move as it goes.*
    1. **Predict two numbers in a comment**, both worked out by hand off the file. The week's total hours: add the third field down all 12 rows. The number of lines that will print: the loop prints once per row it visits, so count the rows.
    2. **Add this shift's hours onto the running total** in the first TODO. Everything that came out of `shift.split(",")` is a string, so something has to convert it.
    3. **Print one line per pass** in the second TODO: the day, the volunteer, and the total so far.
    4. **Run it, and check the line count** against your prediction first, then the final total.

  *That printed line per pass is a tracing tool, not decoration.*

  *Work in `trace-the-path_STUDENT.py` under Step 2: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  A `TypeError` that mentions `str` and `int` means `hours` is still text. Add `print(type(hours))` inside the loop and read what it says. Only one line of output instead of one per row is a different problem: line up your `print` with `total = ...` and check whether both sit indented inside the loop body.

  </details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- **Your two predictions, exactly as you first wrote them.**
  Un-edited. Say whether each one was right.
- **What you mis-traced, if one was wrong.** A condition read
  backwards, a variable you forgot updates every pass, a loop you
  thought ran one more time than it does.
- **Your observations on the data file**, from the three questions
  you answered before writing any code. Say whether anything
  turned out different from what you assumed.
- **How you traced it.** Did you print a line per pass, or hold
  the loop in your head? Say which you would use on 430 rows.

Be ready to answer **"why did you do it that way?"**

## Day 2

- **Step 3: Count Every Volunteer-Weekday Pair, Predicted as a Multiplication**
  - *The coordinator wants a grid of every volunteer against every weekday, to spot the slots nobody covered. First, how big is that grid?*
    1. **Predict the number of cells as a multiplication, not a guess.** Count the distinct volunteer names in the file, count the distinct weekdays, and multiply the two. Write it in a comment as `<volunteers> x <days> = <cells>` before you write or run anything.
    2. **Collect the distinct volunteers** in the first `if` TODO: one entry per volunteer, no repeats.
    3. **Collect the distinct weekdays** in the second `if` TODO, the same way.
    4. **Write the inner loop header** so it runs once per weekday, for every volunteer.
    5. **Run it, and compare `checks`** against the multiplication you wrote.

  *If your prediction was a number of records rather than a number of pairs, that gap is the thing to bring to the shareout.*

  *Work in `trace-the-path_STUDENT.py` under Step 3: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Add `print(volunteers)` and `print(days)` just above `checks = 0`, and count the entries in each list. If a name shows up twice, your `not in` test is not doing its job. Then add `print(volunteer, day)` inside the inner loop and count the printed lines for the first volunteer only. That count, times the number of volunteers, should match `checks`.

  </details>

- **Step 4: Fix the Off-by-One and Print the Row It Never Reached**
  - *An earlier version of this report was quietly missing a volunteer's last shift, and nothing ever errored. The broken loop is handed to you in the skeleton.*
    1. **Predict from the code this time, not the file.** Read `range(len(shifts) - 1)` and work out the rule: what is the first value of `i`, and what is the last? Then write two things in a comment: how many rows the buggy loop visits, and which row it never reaches.
    2. **Write the loop header that visits every row.** Only the range changes; the body below it is already right.
    3. **Print the row the broken loop never reached**, reaching into `shifts` by position rather than retyping the row by hand.
    4. **Run it, and compare all three counts** (rows in the file, buggy visits, fixed visits) against your prediction.

  *Both loops run clean, with no traceback from either. Only one of them is right.*

  *Work in `trace-the-path_STUDENT.py` under Step 4: complete its TODOs.*

  **Try with AI:** *Prompt to understand, you learned this in Module 0.* Ask AI which values `i` takes in `range(len(x) - 1)` for a 4-item list, then hold its list against the values you wrote down.

  <details>
  <summary>Stuck? Open this.</summary>

  When a count is off by exactly one, suspect the range before you suspect the condition. Print `i` on every pass of the buggy loop. Compare the first and last values of `i` against the positions the list actually has.

  </details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- **Your pair prediction, stated as a multiplication.** Say whether
  you predicted a number of rows or a number of pairs, and which
  one the code actually counted.
- **How you found the off-by-one.** By reading the range, or by
  noticing the count was short? Say which of those you would still
  trust on a file too long to eyeball.
- **Anything AI told you that your own counts contradicted.** If
  you asked it about `range()`, say whether it gave you a source
  and whether the source said what it claimed.
- **One thing you would do differently** starting these two days
  over. If you are still holding a question, bring the question.
  You will not be the only one.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `trace-the-path_STUDENT.py` (you may rename it `trace-the-path.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
