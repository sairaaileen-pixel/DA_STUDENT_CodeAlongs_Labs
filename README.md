<<<<<<< HEAD
# Data Analytics Code-Alongs & Labs
Hi Hello Hola 
This is your working repo for code-alongs (from lecture) and labs
(in-class practice) — starter files you actually type into, not a reference
you just read.
=======
# Data Analytics Code-Alongs & Data Challenges

This is your working repo for **code-alongs** (the code you type with your
instructor during each LiveLab) and **Data Challenges** (the hands-on
practice block after it). These are starter files you actually type into,
not a reference you just read.
>>>>>>> upstream/main

## Getting Set Up

You'll do your own work in **your own fork** of this repo, not in this one
directly — that way you can commit and push freely without needing write
access here, and you can still pull in new modules as they're added.

1. **Fork it**: on this repo's GitHub page, click **Fork** (top right) →
   confirm. This creates `https://github.com/<your-username>/DA_STUDENT_CodeAlongs_Labs`
   under your own account.
2. **Clone your fork** to your machine:
   ```
   git clone https://github.com/<your-username>/DA_STUDENT_CodeAlongs_Labs.git
   cd DA_STUDENT_CodeAlongs_Labs
   ```
3. **Point at the original repo too** (so you can pull new modules later —
   this is called an `upstream` remote):
   ```
   git remote add upstream https://github.com/The-Marcy-Lab-School/DA_STUDENT_CodeAlongs_Labs.git
   ```
4. **Do your work, then commit and push to your own fork** (`origin`, not
   `upstream` — you don't have write access to the original, and you
   shouldn't):
   ```
   git add .
   git commit -m "Complete Module 0 dev environment worksheet"
   git push origin main
   ```

### Getting new modules later

Only the module(s) currently in progress live in this repo — a new module
gets added once it's ready, not all at once. When that happens, pull it into
your fork:

```
git fetch upstream
git merge upstream/main
git push origin main
```

If you've been editing files that also changed upstream, git will ask you to
resolve the conflict the normal way — keep your own answers/work, take the
new files/structure from upstream.

## Repo structure

Each `module-*-.../` folder is one module. **A module only shows up here
once it's ready**, so don't expect the whole program on day one.

Module 1 onward:

```
module-1-python-foundations/
  livelabs/
    <livelab-slug>/
      Module1_LessonN_<slug>_STUDENT.py   # THE CODE-ALONG: type into this during class
      <slug>.pdf                          # the day's slides
  data-challenges/
    data/                                 # the data files the challenges read
    <challenge-slug>/
      DataChallengeOverview&Steps.md      # START HERE: scenario, steps, hints, AI tips
      <slug>_STUDENT.py                   # the file you complete and submit
      RUBRIC.md                           # what you're graded on
```

Module 0 uses older folder names (`lectures/` for the code-alongs and
`labs/` for practice) and Markdown terminal worksheets instead of `.py`
files. Everything below about running files applies from Module 1 on.

## Running a `.py` file

Open a terminal in the folder that holds the file and run:

```
python3 Module1_Lesson1_control-flow-conditionals_STUDENT.py
```

Every `.py` file here starts with `#!/usr/bin/env python3`. That first
line is called a **shebang**. It lets you run the file directly, like a
command, once you've made it executable:

```
chmod +x Module1_Lesson1_control-flow-conditionals_STUDENT.py   # once
./Module1_Lesson1_control-flow-conditionals_STUDENT.py          # from then on
```

`python3 file.py` treats that line as a comment, so both ways work.

## Doing a Data Challenge

1. Open the challenge's `DataChallengeOverview&Steps.md` and read the
   scenario and Day 1 steps. Hints are tucked under each step: open one
   only when you're stuck.
2. Work in `<slug>_STUDENT.py`. Code goes under each step's banner; written
   answers go in the `# Your answer:` comments.
3. **Run it from the `data-challenges/` folder**, so the path
   `data/<file>` points at the right place:
   ```
   cd module-1-python-foundations/data-challenges
   python3 trace-the-path/trace-the-path_STUDENT.py
   ```
   A `FileNotFoundError` almost always means your terminal is in the wrong
   folder. Check with `pwd`.
4. Submit the way the overview's **Submitting Your Work** section says.

## Module 0: reading a terminal worksheet (the ` ``` ` blocks)

A `TERMINAL_WORKSHEET_STUDENT.md` file uses shaded blocks that start with
three backtick marks and the word `bash`, like this:

<pre>
```bash
$ pwd
$ ls
```
</pre>

Everything **inside** the block is a real command — type it into your own
terminal, one line at a time. The backtick fence marks themselves aren't
something you type; they just tell this file "this is code." Each command
line starts with a `$ ` in the worksheet the same way your real terminal
prompt does — don't type the `$ ` itself, it's just showing you where a new
command begins. A `# TODO:` line means: replace it with the real command
before running it.

A `...STUDENT.ipynb` notebook doesn't need this — each cell is already a
real, runnable code cell in Jupyter, no fence syntax involved.
