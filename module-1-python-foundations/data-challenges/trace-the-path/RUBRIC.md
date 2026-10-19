# Rubric: Trace the Path

Quest 1.1 · Days 1-2 · submitted once at the end of Day 2, with both days of
work still in the same file.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
3 skills x 4 points = **12 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. It shows you and your instructor which reps
you already own, before the project asks for them unaided. Your instructor
grades from these same tables.

---

## Control Flow & Loops (`control-flow-loops`)

*Can you say what a loop will do before you run it?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you trace a case nobody asked you to trace and state the result before running it. Good candidates: a volunteer with no shifts at all, a weekday that never appears in the log, or a volunteer with exactly one shift. |
| **Meets** | 4 | A written prediction comes before every step, right or wrong. A wrong prediction you then explain is worth more here than a right one you never wrote down. All four steps produce counts that the rows actually support, and you can hand-check at least one of them against the file. You can state the nested count as a multiplication of the two list lengths, rather than by counting printed lines. |
| **Approaching** | 2 | Your code produces the right answers, but predictions are missing, vague, or visibly written after the fact. Or you predict the nested count by running it first. Or you predict the number of records instead of the number of volunteer-and-weekday pairs, which means records and combinations are not separated yet. |
| **Below Expectations** | 1 | No predictions at all. Or counts are wrong and left unreconciled. Or you pasted an AI answer you cannot walk through line by line. |

## Attention to Detail (`attention-to-detail`)

*Do you notice when a number is quietly wrong?*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus you name a detection method that scales past eyeballing. Say how you would have caught this bug on a 430-row file where you cannot check the last row by eye: compare the loop's visit count to `len(shifts)`, or assert that the last row is reached. That habit is the one the project needs. |
| **Meets** | 4 | You find the off-by-one, name which row the buggy loop drops, and point at that row in the file. You explain that `range(n)` already stops at `n - 1`, so the `- 1` in `range(len(shifts) - 1)` is the bug. The broken loop is handed to you in the step 4 skeleton, so read it before you rewrite it. You also handle the `>= 4` boundary correctly on Day 1: a 4-hour shift counts. |
| **Approaching** | 2 | You notice the count is one short but cannot say which row is missing or why. Or you fix it by trial and error without being able to state the rule. |
| **Below Expectations** | 1 | You never notice that the buggy loop visited fewer rows than the file actually holds. Or you read `>=` as `>` on Day 1, so a 4-hour shift is left out of your count, and you never reconcile that count against the file. |

## Collaboration (`collaboration`)

*This is the first challenge where how you work together is graded.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Meets, plus your file records a moment where the two of you disagreed: what each of you predicted, and how you settled it. Settling it by testing beats one of you deferring to the other. |
| **Meets** | 4 | You each predicted separately before comparing. You swapped driver and navigator at least once per day. Both of you can explain any line in the file when asked cold, with the screen turned away and no prompting from the other. If one of you typed everything, neither of you meets this bar. |
| **Approaching** | 2 | You worked together but never swapped roles. Or you predicted jointly, so only one person's reasoning is represented. |
| **Below Expectations** | 1 | One of you did the work and the other submitted a copy. Or neither of you can explain your own file. |

## How this connects

- This challenge heads off the project's common mistake #4, only testing the
  happy path. The off-by-one step is that same mistake on a file small
  enough that you can still catch it by hand.
- Quest 1.1 vocabulary graded here: `Conditional`, `Iteration`,
  `Loop Body`, `Nested Loop`, `Off-by-One Error`.
