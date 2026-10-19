# Rubric: Build It Once, Use It Again

Quest 1.2 · Days 3-5 · submitted once at the end of Day 5, with all three
days of work still in the same file.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. It shows you and your instructor which reps
you already own, before the project asks for them unaided. Your instructor
grades from these same tables.

---

## Functions & Modular Programming (`functions-modular-programming`)

*Can you build a piece once, give it a name, and hand it what it needs?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you say what the decomposition buys you. You name `sessions_in` as the single place that knows the sessions column, so you can point at the one line you would change if the file moved that column, and say why there is only one. Or you restructure Day 3 into a defensibly different shape and say why it is better. You answer the quest's Interview Arena question from your own code, not in the abstract. |
| **Meets** | 4 | Every function returns its answer rather than printing it. Day 1's values are right, and you can back each one up by hand off the file: the total across every class, the same total for Swim only, and the long-booking count at a cutoff of 4 and again at a cutoff of 2. You point at your own `def` line and name the parameters, and at your own call line and name the arguments. Day 3's `total_for` is genuinely composed from `sessions_in` and `signups_for` rather than re-implementing them. |
| **Approaching** | 2 | Your functions work, but one or more print instead of returning, so the answer cannot be used in arithmetic. A printing function hands back `None`, so `handed_back` cannot be used in arithmetic or compared with a count. Or Day 3 is one function doing all three jobs. Or you cannot reliably separate parameter from argument when asked. |
| **Below Expectations** | 1 | Loops left inline with a `def` bolted on and no `return`. Or a `return` sits inside the loop body, so `total_sessions` hands back the first record's own count, which looks plausible until you check it against the whole-file total. Or you used `global` to pass values around, which is banned here. Or Day 1's numbers are wrong and you never reconcile the difference against the file. Or you pasted an AI-written function you cannot walk through parameter by parameter. |

## Attention to Detail (`attention-to-detail`)

*Can you tell a wrong answer from a loud one?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you name a detection method that scales past eyeballing a small file. Say how you would have caught the lowercase bug on a 430-row file where you cannot read the answers off the screen: assert that the per-member totals sum to the whole-file total, or assert that a known member's lookup is non-zero. That is the habit your project needs. |
| **Meets** | 4 | You record, for each of Day 3's four unrequested inputs, whether the result is actually correct or merely did not crash. You catch that looking up a real member's name in the wrong case returns `0` instead of that member's actual total, and you can say what the total should have been. You read Day 2's traceback properly: name the exception (`UnboundLocalError`), name the variable, and state the scope rule in your own words, that reading a module-level name inside a function is fine but assigning to it anywhere in the body makes it local for the whole body, even on a `print` line above the assignment. Your per-member totals add up to the whole-file total, and that check is visible in your file. Your submission opens with two or three sentences on what is actually in `data/rec_center_signups.txt`: what one row represents, which fields are numbers versus text, and anything that already looks off. |
| **Approaching** | 2 | You run the edge cases and report "no errors" without judging whether each result is correct. Four of those lines run clean and at least two of them are wrong. Or you notice the lowercase result is odd but cannot say what the right answer would be. Or you patch it with `.lower()` without saying what else that change breaks, when one member logged under two different capitalizations would silently merge. Or you fix Day 2's error by renaming the variable without stating the rule. |
| **Below Expectations** | 1 | Edge cases not run, or `0` accepted as correct across the board. Day 2's traceback not read past "it broke." The file description skipped, so the sessions column is a guess. |

## Collaboration (`collaboration`)

*Both of you understand the whole file, or neither of you does. This is the
first module where teamwork itself is graded.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus your submission records a real disagreement about whether one of Day 3's results is correct. The made-up name that is not in the file at all is the likeliest one to argue about, because what that call should hand back is genuinely debatable. Write down what each of you thought, and how you settled it. |
| **Meets** | 4 | The partner who did not write a function told the other one its parameters and return value before it was run. You swapped driver and navigator at least once per day. On Day 3 you each wrote down two breaking inputs privately before comparing lists, and the file shows whose was whose. Both of you can explain any line cold, with the screen turned away. |
| **Approaching** | 2 | You worked together, but one person wrote every function while the other watched. Or Day 3's edge cases were brainstormed jointly, so only one person's instincts are represented. |
| **Below Expectations** | 1 | One of you did the work and the other submitted a copy. Or neither of you can explain your own file. |

## How this connects

- This challenge heads off the project's common mistake #1, one long
  function doing everything. Day 3's composed `sessions_in`, `signups_for`,
  and `total_for` are that mistake's structural opposite, on a small file
  you can check by hand.
- It also rehearses the project's common mistake #4, only testing the happy
  path. All four of Day 3's unrequested inputs run clean, and two of them
  are arguably wrong.
- Quest 1.2 vocabulary graded here: `Function`, `Parameter`, `Argument`,
  `Return Value`, `Local Variable`, `Global Variable`, `Scope`.
- Day 2's error is the flip side of the quest's own Bug Hunt. Here you
  assign to a module-level name inside a function. That is the version you
  will hit in your own project code.
