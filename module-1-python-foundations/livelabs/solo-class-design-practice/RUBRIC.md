# Rubric: Solo Class Design Rep

Quest 1.8 · Meet the Objects · Day 15 · a LiveLab session that is itself the
lab, worked and submitted in the same session.

Point scale: Below Expectations = 1, Approaching = 2, Meets = 4, Exceeds = 5.
1 skill x 4 points = **4 points at Meets**, more with any Exceeds earned.

Practice, not a gradebook entry. Read it before you start. Your instructor
grades from these same tables.

---

## Object-Oriented Programming (`object-oriented-programming`)

*You decide a class's attributes and methods from a stated need, on your own.
No template, and no given signature. There is no single correct design. Two
Fellows can hand in different attribute lists and both be right, as long as
every choice traces back to something the coordinator actually asked for.*

| Level | Pts | What it looks like |
|---|---|---|
| **Exceeds** | 5 | Everything at Meets, plus you name a method beyond the minimum and can still trace it to a phrase in the paragraph. |
| **Meets** | 4 | Every attribute traces to a specific phrase in the paragraph, and none is copied from Day 13's `LibraryTool` example. You write `__init__` plus at least 1 method from scratch. You create 2 or more instances and confirm they store their state independently. Your 2-3 sentence justification ties each choice back to the stated need. |
| **Approaching** | 2 | Most of your attributes trace back, but 1 or more is generic and unexplained, such as `color`. You test only one instance, so you never really show independence. Your justification restates the design without tying it to the paragraph. |
| **Below Expectations** | 1 | You copy attributes from Day 13's example whether or not they fit the need. You have no working `__init__`. You write no justification. |

## How this connects

- The project expects you to keep item data inside your `Item` class instead
  of loose parallel lists. That is one of the project's most common mistakes,
  and designing a class straight from a stated need is the half of it you
  practice here.
- Choosing an attribute because it sounds reasonable, rather than because the
  stakeholder asked for it, is the other half.
- Quest 1.8 vocabulary you are assessed on here: class, object, instance,
  attribute, method, `self`, and `__init__`.
