# Rubric: Stress-Test Your Code: Timing & Efficiency

Quest 1.9 · Lookups Matter · Day 17 · a LiveLab session that is itself the
lab, worked and submitted in the same session.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
2 skills x 4 points = **8 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. Read it before you start. Your instructor
grades from these same tables.

---

## Algorithmic Complexity (Big-O) (`algorithmic-complexity-big-o`)

*You prove a Big-O claim with real timing data, not just by reasoning about
it. Your exact numbers will differ from everyone else's, because you time a
class on your own laptop. The shape of the result and your reasoning are
what get graded, not the specific timing values.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Everything at Meets, plus you complete the optional AI-verification stretch and actually re-time to confirm or refute what the AI suggested. |
| **Meets** | 4 | You time both searches at all 3 sizes (10, 1,000 and 100,000), on a target that is *not* in the batch, which is the worst case. Your dict-lookup time stays near zero at every size while your linear-scan time grows with batch size. Your one-sentence reflection names O(1) vs. O(n) correctly and ties each one to your own numbers. |
| **Approaching** | 2 | You time at only 1 or 2 sizes, or you search for a target near the front of the batch, which masks the trend. Your reflection says "the dict was faster" without connecting that to growth shape. |
| **Below Expectations** | 1 | You record no real timing data, or your reflection says one approach "felt faster" with no numbers behind it. |

## Control Flow & Loops (`control-flow-loops`)

*You write a correct linear scan and a working dict-keyed lookup over a real
batch of your own objects.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Everything at Meets, plus your batch generation uses varied, non-identical attribute values rather than one repeated instance. |
| **Meets** | 4 | You write a working `for`-loop linear scan and a dict-comprehension lookup, both over a class of your choice (your own, or the sample `LibraryTool`). Both return the same result for the same target. Both handle a target that is not present: they return `None` or no match, and neither one crashes. |
| **Approaching** | 2 | One of your two searches has a real bug, such as a wrong return value or a crash on a missing target. The other one works. |
| **Below Expectations** | 1 | You write only one search function, or neither one runs without error. |

## How this connects

- The project warns against testing only the happy path. Timing one small
  size and assuming the pattern holds is that same habit. Here you scale up
  far enough to watch the two approaches diverge.
- "It ran fast this once" is not the same claim as "it does not grow with
  size." One is a single stopwatch reading. The other is a trend across
  sizes, and the project asks you to defend it about your own `find_item`.
- Quest 1.9 vocabulary you are assessed on here: linear search, dictionary
  lookup, input size, O(n), O(1) average-case, scale, and complexity.
