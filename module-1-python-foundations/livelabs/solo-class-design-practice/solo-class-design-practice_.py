#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
# 1. What the tool is (name/identifier).
# 2. How many are free to borrow right now (availability status / quantity).
# 3. Whether it needs a safety check before going out again (power tools require a quick inspection after every use, while most other tools do not).


# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
# - tool_id: Tracks individual tool records uniquely.
# - tool_name: "What the tool is."
# - tool_quantity: "How many are free to borrow right now."
# - tool_available: Availability status for borrowing.
# - is_power_tool: "Power tools need a quick inspection after every use. Most other tools do not."


# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.

# Write __init__ and a Method, From Scratch
import json

class Tool:
    def __init__ (self, tool_id, tool_name, tool_quantity, tool_available, is_power_tool=False):
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_quantity = tool_quantity
        self.tool_available = tool_available
        self.is_power_tool = is_power_tool

    def needs_safety_check(self):
        return self.is_power_tool
    
    def __str__(self):
        status = "Available" if self.tool_available else "Checked Out"
        check_status = "Needs Inspection" if self.needs_safety_check() else "Standard"
        return f"[{self.tool_id}] {self.tool_name}: {status} ({check_status})"
    
with open("tools.json") as f:
    tools_data = json.load(f)

tool_fleet = []
for t in tools_data:
    tool_fleet.append(Tool(
        t["tool_id"],
        t["tool_name"],
        t["tool_quantity"],
        t["tool_available"],
        t["is_power_tool"]
    ))   

for tool in tool_fleet:
    print(f"{tool} Safety Check Required: {tool.needs_safety_check()}")


# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.

# Instantiate 2+ Objects, Confirm Independent Storage

# Prediction: Changing tool_fleet[0]'s availability to False 
# should change only the first tool. tool_fleet[1] should remain True.


tool_one = Tool("dr1", "cordless drill", 2, True, True)
tool_two = Tool("hm1", "hammer", 1, True, False)

print()
print("--- Before Any Changes ---")
print(f"Tool 1: {tool_one.tool_name} Is available = {tool_one.tool_available}")
print(f"Tool 2: {tool_two.tool_name} Is available = {tool_two.tool_available}")

tool_one.tool_available = False # changing the first object.

print("\n--- After Modifying Tool One ---")
print(f"Tool 1 (Modified): {tool_one.tool_name} Is available = {tool_one.tool_available}")
print(f"Tool 2 (Untouched): {tool_two.tool_name} Is available = {tool_two.tool_available}")

# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
# This design directly matches the stakeholder needs by tracking each tool's name and ID, 
# its availability, and whether it requires a safety check after use. 
# Bundling these specific details into a class keeps the library inventory organized, 
# readable, and easy to update.

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
# Attribute list and stakeholder phrases:
# - tool_id: From "name/identifier" (to track records uniquely).
# - tool_name: From "What the tool is."
# - tool_quantity: From "How many are free to borrow right now."
# - tool_available: From the availability status needed for borrowing.
# - is_power_tool: From "Power tools require a quick inspection after every use."
#
# Attribute considered and rejected:
# - Safety_check_in
# - Safety_check_out
#
# 3. Method purpose (needs_safety_check):
# - Anwers the question with simple true or flase
# - Why I would reach for it first: To instantly catch power tools that need a safety check 
# after being returned, ensuring borrower safety.
#
# 4. What I got stuck on:
# - I got stuck on an empty JSON file error (JSONDecodeError) when trying to load 
# my tools data. Working through it taught me how important it is to ensure external 
# data files are correctly formatted and saved before running the Python file.
