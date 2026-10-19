# Data Challenge: Build It Once, Use It Again

**GitBook quest:** [Quest 1.2: Build It Once, Use It Again](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-02-functions-scope) (quest runs Days 3-5)

**Vocabulary from the reading** (use these words in your shareout): `Function`, `Parameter`, `Argument`, `Return Value`, `Local Variable`, `Global Variable`, `Scope`

**Skills assessed:** Functions & Modular Programming, Attention to Detail, Collaboration (see this lab's own `RUBRIC.md`)

**Estimated time:** ~60 minutes per day, across 3 days (15 min intro · 30 min group work · 15 min shareout, each day)

**Submitted once, at the end of Day 3.** The rubric grades all 3 days of this challenge together, so keep everything in one file and keep your earlier days' work visible.

## Scenario

The coordinator at the Fairhaven Recreation Center keeps a class sign-up
log, and the board keeps changing its mind. The coordinator wants four
answers out of that one file.

- Total sessions booked across every class.
- Total sessions for Swim only.
- Total sessions per member.
- A count of the long bookings, with the cutoff moved from 4 sessions to
  2 because the board revised the policy.

**What you already did, and what is different here.** In Quest 1.1 you
wrote a loop that answers one question. Answer these four the same way
and you write four nearly identical loops, differing by a column index or
a number. Then the board moves the cutoff from 4 to 2. Now you have to
find and edit every copy that used the old number, with no way to tell
which copies you already fixed.

This challenge answers the same four questions with functions instead. You
write the loop once, give it a name, hand it the thing that changes as an
argument, and get an answer back. When the board moves the cutoff, you
change the argument at the call, not the loop. Same file, same arithmetic,
one copy of each piece of logic.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## What Each Day Is For

- **Day 1**: Turn the totaling and counting loops you already know how to write into real functions. Each one should return a value instead of printing one. Call each function twice on different inputs, to prove the function was worth writing. Then agree with your partner on which name is the parameter and which value is the argument.
  - *Assessed today: Functions & Modular Programming, Attention to Detail*
- **Day 2**: Two functions can answer the same question. One reaches out to a module-level name. The other takes that same value as a parameter. Compare the two. Then trigger an `UnboundLocalError` on a line that only reads a name, and explain the scope rule behind it.
  - *Assessed today: Functions & Modular Programming, Attention to Detail*
- **Day 3**: Compose two small functions into a third. Then run the result against inputs nobody asked for: an empty list, a single record, and a name that is not in the file. For each result, decide whether the answer is correct or just quiet.
  - *Assessed today: Functions & Modular Programming, Attention to Detail, Collaboration*

## Ground Rules

**Do not use AI to write the code.** This challenge grades Functions & Modular Programming and Attention to Detail. If AI writes it, nothing has been measured.

**Use AI to understand, then check what it says.** The AI Toolkit below shows how, one skill at a time.

**New here:** None of the Python is new: the LiveLabs cover `def`, `return` and scope. What is new is running your functions on a real file and on inputs nobody asked for, then judging whether a quiet `0` is right.

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

- The person who did NOT write a function has to tell their partner its parameters and what it returns, before either of you runs it. If they cannot, the function needs a better name or a shorter body. Fix that before moving on.
- On the last day, split the edge cases. Each partner privately writes down two inputs they think will break the composed function. Then trade lists and run each other's. The case you did not think of is the whole reason you have a partner.

</details>

> **AI techniques you have so far** (taught by Day 3)
>
> - **Verify against your own work** *(Module 0)*: Check every AI answer against a hand count, the data file, or a run of your own code.
> - **Make it explain** *(Module 0)*: Paste real output or a traceback and ask why. Make it predict before you run.
> - **Prompt to understand** *(Module 0)*: Ask about the idea on a made-up example, not your code, and ask for a source to read.
>
> The tips below use only these.

## AI Toolkit

Each tip below pairs one skill this challenge grades with one way to use AI on it. Copy the prompt, then do the check. A prompt you never check is just a guess.

**Prompt to understand** (Functions & Modular Programming) · Technique: **Prompt to understand**, you learned this in Module 0

```text
Explain the difference between return and print inside a Python
function. Use a tiny made-up function that doubles a number, not my code.
Show what a variable holds when I store the result of each version. Which
Python docs page covers return?
```

**Check:** Type both tiny versions yourself and print what each one hands back. Then check whether that matches what your own `show_long_bookings` handed back in step 2.

**Make it explain the output** (Functions & Modular Programming) · Technique: **Make it explain**, you learned this in Module 0

```text
Here is a function and the error it raises:
[paste log_signup_broken]
[paste the last three lines of the traceback]

In plain words, why does Python treat this name as local inside the
function? Point at the exact line that makes it local. Do not rewrite the
function.
```

**Check:** Find the line it points at in your own file. Compare its reason with the one you wrote in step 4. If it tells you to add `global`, remember the step already says that is not the fix.

**Validate against your own work** (Attention to Detail) · Technique: **Verify against your own work**, you learned this in Module 0

```text
Here is a sign-up log:
[paste the data rows]

Add up the sessions for the Swim rows only. List each Swim row you used
before you give the total.
```

**Check:** Add up Swim by hand first. If its list of rows differs from yours, open the file and recount. Then check both against what your `total_sessions(swim_only)` prints.

**Make it explain the output** (Attention to Detail) · Technique: **Make it explain**, you learned this in Module 0

```text
Here is my function total_for(records, member), one input I gave it,
and what it returned:
[paste the function]
[paste the input and the printed result]

Walk me through the function line by line for that input, and say why
it returns that value. Do not tell me whether the answer is right. I
will decide that.
```

**Check:** Trace the same input through your function on paper. If its walk and your trace differ, add a `print` inside the loop and run it. Then write your own verdict beside the result, as step 6 asks.

**Prompt to understand** (Collaboration) · Technique: **Prompt to understand**, you learned this in Module 0

```text
I am the navigator. My partner wrote total_for so it calls two smaller
functions:
[paste all three]

Give me three questions to ask my partner that check whether each
function does exactly one job. Do not answer them.
```

**Check:** Ask your partner the questions and have them point at the lines. If neither of you can answer one, run that function on its own and see what it returns.

## The Data

- **File:** `data/rec_center_signups.txt` (TXT)
- **Where it comes from:** Created for this challenge.

**Before you write any code, open the file and look at it.** You will not be told what is in here. Finding out is the first part of the work. Answer these three:

1. What does one row represent?
2. Which fields hold numbers, and which hold text?
3. What already looks wrong, missing or inconsistent?

*Answer them at the top of `build-it-once_STUDENT.py`, under THE DATA.*

Loading the file is **not** the work here, so this is the code that
does it. Paste it and move on. A later LiveLab explains what `open()`
is actually doing.

```python
with open("data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]
```

What `signups` ends up holding is yours to work out. Open the file and
read it. A `FileNotFoundError` means you are running from the wrong
folder, not that the file is missing.

## Your Objectives

## Day 1

- **Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only**
  - *One function that adds up a sessions column, called twice: once on every record, once on just the Swim records.*
    1. **Predict two numbers by hand off the file.** Total sessions across every class: add the third field down all 13 records. Total sessions for Swim only: add that same field, but only on the records whose class is `Swim`. Write both in a comment before you run anything.
    2. **Write `total_sessions(records)`** so it adds up the sessions column across every record in `records` and hands the total back with `return`, not `print`.
    3. **Build `swim_only`**: the records whose class is `Swim`, and nothing else.
    4. **Run it, and check both printed numbers** against your two predictions.

  *The arithmetic is the same arithmetic a plain loop would do. What changes is that the answer comes back to you instead of going to the screen.*

  *Work in `build-it-once_STUDENT.py` under Step 1: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  If `every class` prints `None`, your function never reaches a `return`. If it prints a number smaller than your hand total, add `print(record, total)` as the first line inside the loop and run it again. Count the printed lines: does the loop visit every record, or does it stop early? Check how far your `return` is indented.

  </details>

- **Step 2: Count Long Bookings at Two Different Cutoffs With One Function**
  - *The board changed the long-booking cutoff from 4 sessions to 2. Answering both should cost you one extra argument, not a second function.*
    1. **Predict both `returned:` counts in a comment**, reading the third field down the file: once for 4 or more, once for 2 or more.
    2. **Write `count_long_bookings(records, minimum)`** so it counts the records whose sessions number is `minimum` or more, and returns that count.
    3. **Write `show_long_bookings(records, minimum)`** so it prints a sentence with the same count in it. Only print. Do not add a `return`.
    4. **Run the whole file**, including the lines at the bottom that were written for you.
    5. **Write down what `handed_back` holds, and why.** It is on the last printed line.
    6. **Name the parameter and the arguments**, pointing at the lines: which name is `minimum`, and which values are the 4 and the 2.

  *One of the two functions you just wrote gives you something back. The other only puts something on the screen.*

  *Work in `build-it-once_STUDENT.py` under Step 2: complete its TODOs. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  Add `print(type(handed_back))` under the last line and run it again. Then add `print(handed_back == count_long_bookings(signups, 4))` and compare its answer with the two counts already on your screen. Both functions put the same number on the screen. Only one of them handed it back.

  </details>

### Share Out: Day 1

**Last 15 minutes, back together as a class. Bring:**

- **Your two totals.** Whole file, and Swim only. If your numbers
  differ from another group's, say so. You read the same file, so
  one of you has a bug worth finding.
- **Your function next to the loop it replaced.** Name the
  specific thing that got easier. Not "cleaner."
- **What `show_long_bookings` handed back, and why.** Say what
  that tells you about `return` versus `print`.
- **Which name is the parameter and which value is the
  argument**, pointing at your own two lines.

Be ready to answer **"why did you do it that way?"**

## Day 2

- **Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare**
  - *Two functions that answer the same question. The one you wrote on Day 1 takes the cutoff as a parameter. This one takes no cutoff at all.*
    1. **Predict both printed counts with no new arithmetic.** You already produced the count at a cutoff of 4 and the count at a cutoff of 2 in Day 1's second step. All you are predicting here is which of those two numbers each of the two identical-looking calls prints. Write both in a comment, and write why.
    2. **Write `count_reaching_outside(records)`** so it counts the same thing `count_long_bookings` does, but takes no `minimum` parameter. It reads `sessions_cutoff` from outside the function instead.
    3. **Call it once at a cutoff of 4**, printing the result.
    4. **Call it again, unchanged, after `sessions_cutoff` becomes 2**, and print that result too. The call line is identical both times.
    5. **Print `count_long_bookings(signups, 4)` underneath** for comparison.

  *Both versions run clean. Decide which of the two you would trust in a file you did not write, and say what in the call line told you.*

  *Work in `build-it-once_STUDENT.py` under Step 3: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Nothing here is broken, so there is nothing to fix. Put `count_reaching_outside(signups)` and `count_long_bookings(signups, 4)` side by side and ask of each: what cutoff is this using? One call line answers that on its face. For the other, find every line in the file that sets `sessions_cutoff`, and note which one ran last before each call.

  </details>

- **Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError** *(expect this to raise `UnboundLocalError`. That is the point, not a bug.)*
  - *The coordinator wants each sign-up printed next to the one before it. The top half is yours to write. The bottom half is written for you, and is supposed to raise.*
    1. **Write `log_signup(record, previous_member)`** so it pulls the member name out of `record`, prints the previous member and this one on one line, and returns this member's name.
    2. **Call it on `signups[0]`, then on `signups[1]`**, storing what it returns back into `last_member` each time. Predict both printed lines in a comment first, reading the names off the top of the file.
    3. **Leave `log_signup_broken` exactly as written.** It tries the same job by reading and then updating `last_seen`, a name defined above the function.
    4. **Predict in a comment whether its `print` line will work.** The step above showed a function reading an outside name just fine.
    5. **Run the file, read the traceback, and write down the exception name, the variable and the line it points at**, in your own words, before you look anything up.

  *`global` is not the fix. The working half of this same step already shows what is: pass the value in, return it back out.*

  *Work in `build-it-once_STUDENT.py` under Step 4: complete its TODOs. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  The traceback points at a `print` line, and a `print` only reads. Before you change anything, find every line inside `log_signup_broken` where `last_seen` appears on the LEFT of an `=`. Then delete that line, run the file again, and compare. The rule you need is about the whole function body, not just the failing line.

  </details>

### Share Out: Day 2

**Last 15 minutes, back together as a class. Bring:**

- **Which of the two functions you would trust** in a file you
  did not write, and what in the call line decided it.
- **The exception name and the variable it named**, plus your own
  one-sentence account of the rule. Written before you looked
  anything up.
- **Why the `print` line failed** when it only reads `last_seen`,
  and what deleting the line below it changed.
- **Anything AI told you about `global`.** Say whether it offered
  it as the fix, and what you did instead.

Be ready to answer **"why did you do it that way?"**

## Day 3

- **Step 5: Build Per-Member Totals Out of Three Functions, Not One**
  - *The coordinator wants per-member totals. Write this as three functions, not one.*
    1. **Write `sessions_in(record)`** so it pulls the sessions number out of a single record and returns it.
    2. **Write `signups_for(records, member)`** so it returns just the records belonging to one member.
    3. **Write `total_for(records, member)`** so it returns that member's total sessions, doing almost nothing itself. It gets its work done by calling the other two.
    4. **Predict Gwen's total in a comment**, adding up Gwen's rows in the file by hand.
    5. **Print one line per member** for Nia, Omar, Tess, Rafi and Gwen, and check Gwen's line against your comment.

  *Before you run it, show your partner the line where each of the three functions gets called.*

  *Work in `build-it-once_STUDENT.py` under Step 5: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Test each function on its own before `total_for` uses it. `print(sessions_in(signups[0]))` should print the third field of the file's first record, as a number. `print(signups_for(signups, "Gwen"))` should list only records that start with `Gwen`. Whichever one disagrees with the file is the one to fix first.

  </details>

- **Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer**
  - *No new functions. Call the ones you already have on inputs nobody asked for, and write a verdict beside each printed result.*
    1. **`total_for` on an empty list.** Print the result.
    2. **`total_for` on a list holding exactly one record.**
    3. **`total_for` with a member name that is not in the file at all**, such as `"Marco"`.
    4. **`total_for` with a name differing from a real member's only by capitalization**, such as `"nia"` for Nia.
    5. **`signups_for` on the empty list.**
    6. **Add up the per-member totals for all five members**, and print that sum beside `total_sessions(signups)`. The two should agree.
    7. **Write a verdict beside each of the five results** in a comment: right, or just a number that did not crash? Argue each one with your partner first.

  *Every line runs clean. Two of them deserve a different answer than they get.*

  *Work in `build-it-once_STUDENT.py` under Step 6: complete its TODOs.*

  <details>
  <summary>Stuck? Open this.</summary>

  Next to each result, write what the coordinator would expect to hear if they asked you that question at the front desk. Where the code says one thing and the coordinator expects another, you found a quiet wrong answer. Nothing has to crash for that to count.

  </details>

### Share Out: Day 3

**Last 15 minutes, back together as a class. Bring:**

- **Your verdict on one edge case.** Pick the strangest result.
  Say whether the answer is right or just quiet, and what you
  would change if this were the center's real data. If you and
  your partner disagreed, bring both positions.
- **Your cross-check.** Did the five per-member totals add up to
  the whole-file total? Say how you would run that check on a
  430-row file you cannot eyeball.
- **Three functions or one?** Say which you wrote and what it
  cost or saved you.
- **One question you could not settle**, or one thing you would
  do differently starting over. Half-finished thinking is what
  this slot is for.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `build-it-once_STUDENT.py` (you may rename it `build-it-once.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
