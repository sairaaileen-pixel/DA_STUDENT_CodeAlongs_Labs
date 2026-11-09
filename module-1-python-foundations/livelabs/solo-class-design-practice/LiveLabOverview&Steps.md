# Lab: Solo Class Design Rep

**GitBook quest:** [Quest 1.8: Meet the Objects](https://marcylabschool-da.gitbook.io/marcylabschool_da-docs/modules/module-01/quest-08-oop) (quest runs Days 13-15)

**Vocabulary from the reading** (use these words in your shareout): `Object-Oriented Programming (OOP)`, `Class`, `Object`, `Instance`, `Attribute`, `Method`, `self`, `__init__`, `__str__`, `__repr__`

**Skills assessed:** Object-Oriented Programming (see this lab's own `RUBRIC.md`)

**Estimated time:** ~85 minutes (10 min intro · 55 min group work · 20 min shareout)

## Scenario

A local community center runs a tool-lending library. Neighbors borrow
drills, ladders and pressure washers for a project, then bring them back.
The volunteer coordinator wants a simple way to track each tool. They have
asked you for three things:

- What the tool is.
- How many are free to borrow right now.
- Whether it needs a safety check before it goes out again. Power tools
  need a quick inspection after every use. Most other tools do not.

Nothing in this lab gives you attribute names or a method signature.
Working out what to track, and how to check it, from that paragraph alone
is the exercise.

There is no single correct design. Two Fellows can hand in different
attribute lists and both be right, so long as every choice traces back to
something the coordinator actually said.

*Work in a group of 2-3, but complete and submit your own copy. Collaboration is encouraged, a shared submission isn't.*

## Ground Rules

**Do not use AI to write the code.** This challenge grades Object-Oriented Programming. If AI writes it, nothing has been measured.

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

- **Step 1: Read the Stakeholder Need**
  - *A new stakeholder need. Not the board-game or office-supply domain from lecture, and not one of the project's own 4 scenarios.*

  *Work in `solo-class-design-practice_STUDENT.py` under Step 1. Write your answer as `#` comments under its `# Your answer:` line.*

- **Step 2: Decide Your Attributes, Each With a Reason From the Scenario**

  *Work in `solo-class-design-practice_STUDENT.py` under Step 2. Write your answer as `#` comments under its `# Your answer:` line.*

- **Step 3: Write __init__ and a Method, From Scratch**
  - *There is no single correct design here. Your class name, your attribute names and your method can all differ from everyone else's and still be right. The test is whether each one traces back to the stakeholder paragraph.*

  *Work in `solo-class-design-practice_STUDENT.py` under Step 3.*

- **Step 4: Instantiate 2+ Objects, Confirm Independent Storage**
  - *The same proof Day 13's lecture asked for, now on a class you designed yourself. Predict what each `print()` will show before you run it.*

  *Work in `solo-class-design-practice_STUDENT.py` under Step 4.*

  <details>
  <summary>Stuck? Open this.</summary>

  To prove independence, change one object's attribute directly. Then call your method on both objects. The one you did not touch should be unaffected.

  </details>

- **Step 5: Justify Your Design Choice in 2-3 Sentences**

  *Work in `solo-class-design-practice_STUDENT.py` under Step 5. Write your answer as `#` comments under its `# Your answer:` line.*

## Share Out

**Last 15 minutes, back together as a class. Bring:**

Come ready to show your class and defend it. Specifically:
- The attribute list you chose, and for each one, the phrase in the
  coordinator's request it came from. If you can't point at a phrase for
  an attribute, say so - that's a real finding, not a failure.
- One attribute you considered and rejected, and why. - Your method: what question does it answer, and why would the
  coordinator reach for it first?
- Anything you got stuck on. Designing from a paragraph with nobody to
  check against is genuinely hard, and naming where it was hard is worth
  more to the room than a tidy answer.

Expect to be asked "why that attribute and not another?" - there is no single right list here, so the reasoning IS the answer.

Be ready to answer **"why did you do it that way?"**

## Submitting Your Work

- Commit `solo-class-design-practice_STUDENT.py` (you may rename it `solo-class-design-practice.py`) to your own data challenge repo, inside your **Module 1** folder. Use one repo for the whole program, not a new repo per challenge.
- On GitHub, open that file and copy the URL that points **directly at it**, not the repo root.
- Paste that URL into the LMS as your submission.
