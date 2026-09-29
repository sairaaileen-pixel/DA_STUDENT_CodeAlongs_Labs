# Data Analytics Code-Alongs & Labs
Hi Hello Hola 
This is your working repo for code-alongs (from lecture) and labs
(in-class practice) — starter files you actually type into, not a reference
you just read.

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

```
<module-slug>/
  data/
    <dataset files used across this module's lectures and labs>
  lectures/
    <lecture-slug>/
      TERMINAL_WORKSHEET_STUDENT.md      # terminal/bash-based lecture
      ...STUDENT.ipynb                    # Python-based lecture (Jupyter notebook)
  labs/
    <lab-slug>/
      TERMINAL_WORKSHEET_STUDENT.md      # (or a notebook, same pattern as lectures)
```

Each `module-*-.../` folder is one module (e.g. `module-0-foundations`).
Inside it, `lectures/` holds one folder per class day, `labs/` holds one
folder per hands-on practice session, and `data/` holds the dataset(s) that
module's lectures/labs actually use.

**A module only shows up here once its content is ready** — new modules get
added over the course of the program, so don't expect the whole curriculum
on day one.

## The `data/` folder — read this before running any command

Every worksheet/notebook references a dataset with a short path like
`data/energy_sample.csv` — **that path is relative to the module's own root
folder** (e.g. `module-0-foundations/`), **not** to the worksheet file's own
location inside `lectures/<slug>/` or `labs/<lab-slug>/`.

Before running a command that touches a dataset, either:
- `cd` into the module folder itself first (e.g. `cd module-0-foundations`),
  then run the command from there, **or**
- adjust the path to point up and over into `data/`, e.g.
  `../../data/energy_sample.csv` if you're running from inside a
  `lectures/<slug>/` or `labs/<lab-slug>/` folder.

If a command can't find the file, this is almost always why — double check
where your terminal actually is (`pwd`) before assuming the file is missing.

## Reading a terminal worksheet (the ` ``` ` blocks)

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
