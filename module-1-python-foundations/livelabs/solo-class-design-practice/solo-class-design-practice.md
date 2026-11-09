# Lab: Solo Class Design Rep

*Stubbed by the `plan-module` skill from Module 1's Lecture & Lab Map (see
`module_sources/module-1-python-foundations/INSTRUCTOR_MODULE_SUMMARY.md`).
See "Labs" in `content_spec/SCHEMA.md`. This is formative practice, not the
graded project
(`module_sources/module-1-python-foundations/PROJECT.md`).*

**~85 minutes, one day.** The time splits three ways:

- 10 min instructor framing.
- 55 min work time, with each Fellow completing and committing their own
  copy.
- 20 min full-class shareout.

The exact budget lives in `solo-class-design-practice.yaml`'s
`estimated_minutes`. The rendered worksheets state it too.

**Minimally scaffolded on purpose.** The lab design philosophy in
`content_spec/SCHEMA.md`'s "Labs" section limits the student worksheet to
three things: the scenario, each step's objective, and one hint. Fellows
work in `solo-class-design-practice_STUDENT.py`, which holds a banner per
step and nothing else: no class signature and no code to retype. The
instructor worksheet (`LiveLabOverview&Steps_INSTRUCTOR.md`) and
`solo-class-design-practice_SOLUTION.py` carry the validated answer key for
circulating with. That key is one valid design, not *the* design.

## Follows

Day 13's "OOP: Building a Class With a Partner" lecture and Day 14's "Magic
Methods" lecture. This lab is the solo escalation right after both.

## Why this lab exists

This lab fills one of the two bridging gaps
`INSTRUCTOR_MODULE_SUMMARY.md` flags explicitly. Objective 6's own content
on Day 13 is done **with a partner**. Fellows follow a worked template with
the attributes already decided. The project asks for more. A Fellow has to
**independently design** a class's attributes from a stated stakeholder
need. The project's starter code gives no class signature to lean on. That
is a materially harder ask. This lab is the missing solo rep, done once
before the project asks for it unguided.

## Scaffolding level

From `collaborative` toward `independent`. Fellows work solo on the design
decision itself, which is the whole point of the day. Instructor and peer
support is still in the room. That puts this lab one notch short of
`PROJECT.md`'s fully independent, graded version of the same skill.

## Dataset / use case

One short written paragraph stating a stakeholder need. The scenario is a
community tool-lending library, and it is **distinct from all 4 project
scenarios**: bookstore, restaurant, healthcare, and athletic wear. It is
also distinct from the two demo domains lecture already used, a board-game
collection and an office-supply tracker (see
`module_sources/module-1-python-foundations/DATASET.md`). Fellows read the
prompt paragraph at the start of the lab. The paragraph lives in
`solo-class-design-practice.yaml`'s top-level `scenario` field, and it
renders as the "## Scenario" section at the top of both worksheets:

> A local community center runs a tool-lending library. Neighbors borrow
> drills, ladders and pressure washers for a project, then bring them back.
> The volunteer coordinator wants a simple way to track each tool. They have
> asked you for three things:
>
> - What the tool is.
> - How many are free to borrow right now.
> - Whether it needs a safety check before it goes out again. Power tools
>   need a quick inspection after every use. Most other tools do not.

No attribute names and no method signature are given. Working out what to
track, and how to check it, from that paragraph alone is the exercise.

## Day-by-day milestones (1 day: Day 15)

| Day | Goal |
|---|---|
| 15 | Design a class for a stated stakeholder need, solo, then defend that design to the room. |

What a Fellow does on Day 15:

- Read a one-paragraph stakeholder need. It is not one of the 4 project
  scenarios.
- Decide independently what a class for that need should track. Choose real
  attributes, not just names, and tie each one back to the stated need.
- Write `__init__` and at least one method from scratch, with no signature
  given.
- Instantiate 2 or more objects. Confirm each object stores its attributes
  independently.
- Justify the design in 2-3 written sentences. That rehearses the project
  deck's design-reasoning slide.

The day closes with a 20-min full-class shareout. The shareout puts 2-3
Fellows' *different, equally valid* designs side by side. The discussion
prompt lives in `solo-class-design-practice.yaml`'s `shareout`.

## Skills / rubric criteria this lab exercises

`object-oriented-programming`. See
`module_sources/module-1-python-foundations/INSTRUCTOR_MODULE_SUMMARY.md`'s
rubric distillation table. This lab rehearses the `PROJECT.md` "Meets" bar:
*"the class's attributes are a genuinely reasonable answer to this
stakeholder's actual stated need... the class is used consistently, with no
parallel raw dicts or lists holding the same data elsewhere."*

## Common mistakes to preempt

From `module_sources/module-1-python-foundations/PROJECT.md`'s
common-mistakes list:
3. Holding item data in loose parallel lists instead of actually using the
   class consistently throughout.

One more thing is worth watching for here: generic attributes that do not
clearly connect back to the stated need. That one comes from the upstream
brief's "Approaching" rubric tier, not from a full common-mistake entry. The
usual form of the mistake is a Fellow copying whichever fields felt familiar
from Day 13's partnered example, whether or not this stakeholder needs them.
