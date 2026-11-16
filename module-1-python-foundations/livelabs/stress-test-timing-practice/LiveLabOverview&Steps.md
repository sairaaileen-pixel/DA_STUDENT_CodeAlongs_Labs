# Lab: Stress-Test Your Code: Timing & Efficiency

**GitBook quest:** [Quest 1.9: Lookups Matter](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-09-big-o-practice) (quest runs Days 16-17)

**Vocabulary from the reading** (use these words in your shareout): `Linear Search`, `Dictionary Lookup`, `Input Size`, `O(n)`, `O(1) Average-Case`, `Scale`, `Complexity`

**Skills assessed:** Algorithmic Complexity (Big-O), Control Flow & Loops (see this lab's own `RUBRIC.md`)

**Estimated time:** ~90 minutes (10 min intro · 65 min group work · 15 min shareout)

## Scenario

The class you designed in Day 15's lab works. Your manager has one question before it goes near real users: "this is fine with ten records. Will it still be fine with a hundred thousand?"
Nobody on the team can answer that by reading the code. "It feels fast on my laptop" is not an answer either. So you find out the way engineers actually find out:
- Build a scaled-up batch of your own objects. - Write the search two different ways. - Put a stopwatch on both. - Let the numbers say which one survives the jump from 10 records to
  100,000.

By the end of lab you should be able to tell your manager what happens at scale, and show the timings that prove it.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## Ground Rules

**Do not use AI to write the code.** This challenge grades Algorithmic Complexity (Big-O) and Control Flow & Loops. If AI writes it, nothing has been measured.

**You can use AI to** explain a concept, explain an error message, or show you a different example than the one you need.

**Make it prove it.** When AI explains a concept, ask "what is your source for that?" and go read what it names. If it cannot name one, or names something that does not exist, you have learned something about the answer.

**Run everything and check it yourself.** AI will hand you code that runs and is wrong.

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

</details>

## Your Objectives

- **Step 1: Generate Batches of Your Own Day 15 Class at Three Sizes (10, 1,000, and 100,000)**
  - *Use your own class from Day 15's lab - your batch should be full of YOUR objects, not a shared template's.*

  *Work in `stress-test-timing-practice_STUDENT.py` under Step 1.*

  <details>
  <summary>Stuck? Open this.</summary>

  One function that takes a size and returns that many instances is enough. Call it three times. Give the instances varied attribute values rather than a hundred thousand identical ones, and reach for `random` if that helps. Whatever attribute you plan to search on must be unique per instance. Otherwise Step 2's two searches will not be comparable.

  </details>

- **Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree**
  - *Same two functions Day 16's lecture wrote over SupplyItem - now over your own class and a much bigger batch.*

  *Work in `stress-test-timing-practice_STUDENT.py` under Step 2.*

  <details>
  <summary>Stuck? Open this.</summary>

  Day 16's dict version was a comprehension, `{item.name: item for item in supplies}`. It was keyed on the same attribute the linear scan compares against. Both of your searches should hand back the same object for the same target. Both should also cope with a target that is not in the batch. Step 3 needs that second case.

  </details>

- **Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers**
  - *Predict the pattern before running: which column should grow as size grows, and which should stay roughly flat?*

  *Work in `stress-test-timing-practice_STUDENT.py` under Step 3.*

  <details>
  <summary>Stuck? Open this.</summary>

  `time.perf_counter()` is new. It returns a number of seconds, so you time something by reading it before and after, then subtracting.
  Search for a value that is NOT in your batch. A search that finds its answer on the first try tells you nothing about scale, and the worst case is what makes the growth show up. End with three rows, one per size, each with both times. A single row cannot show a trend.

  </details>

- **Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms**

  *Work in `stress-test-timing-practice_STUDENT.py` under Step 4. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  Use your own Step 3 numbers, and name both Big-O classes. "The dict was faster" is not the answer your manager asked for. They asked what happens at 100,000. That is a question about what each column DID as the size grew, not about which one won a single race.

  </details>

- **Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It**
  - *Stretch work only - beyond the core lab budget. Take it if you finish Steps 1-4 early. Same 'verify before trusting' habit from Module 0's AI-literacy lesson, now applied to a code-optimization claim instead of a chatbot fact claim.*

  *Work in `stress-test-timing-practice_STUDENT.py` under Step 5. Write your answer as `#` comments under its `# Your answer:` line.*

  <details>
  <summary>Stuck? Open this.</summary>

  Apply the suggestion, then re-run Step 3's timing setup unchanged, so the before and after are actually comparable. If the numbers don't move, the claim didn't hold - and saying so is a correct answer here.

  </details>

## Share Out

**Last 15 minutes, back together as a class. Bring:**

Bring your numbers, not a summary of them. Specifically:
- Your timings at each batch size, for both searches. Everyone tested a
  different class on a different laptop, so the raw numbers won't match -
  put yours up anyway.
- Which column changed as the batch grew, and which one didn't. - The batch size where the difference stopped being something you had to
  squint at.
- Whether anything surprised you. A linear scan that looked suspiciously
  flat is worth raising - say what you found out was going on.
- If you tried the AI stretch: what it claimed, and whether your own
  timings actually backed it up. "It was wrong" is a good answer if you
  can show the number that proves it.

Be ready for "why does that happen?" - the timings are evidence, and the explanation is what's being assessed.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `stress-test-timing-practice_STUDENT.py` (you may rename it `stress-test-timing-practice.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
