#!/usr/bin/env python3
"""Day 3 code-along: Functions, Parameters & Return.... Run: python3 <file>"""

# ===== 1. Define and Call, Live =====
# Build a reusable greeting: one function, called twice, prints it twice.
print('----- 1. Define and Call, Live -----')
# TODO: define greet() to print a welcome message, then call it twice

def greet():
    print("Welcome")
greet()
greet()


# ===== 2. Parameters, Live =====
# Make greet work for anyone: pass in a name, then greet Jordan and Amara.
print('----- 2. Parameters, Live -----')
# TODO: add a name parameter to greet
# TODO: print a personal welcome for each of 2 names

<<<<<<< HEAD
def greet(user_name):
    #print("Welcome" + user_name)

    print("Welcome", user_name)

    #print (f"Welcome {user_name"})

greet("Heather")
greet("Michael")



# DISCUSS: The code is def double(n): print(n * 2), then double(5). Put the
#          steps of that call in order. A: n becomes 5. B: the body runs. C:
#          double gets called with 5.
=======
# DISCUSS: Order double(5): A: n becomes 5. B: body runs. C: it gets called.
>>>>>>> upstream/main
# Your answer:
#
# PREDICT before you run: If double(n) prints n * 2, what does double(5) print?
# Your answer:
#


# ===== 3. Return, Live =====
# Send a value back with return to use it in math. double(5) + 1 prints 11.
print('----- 3. Return, Live -----')
<<<<<<< HEAD
# TODO: write double(n) using return (not print), then use
# its result in an expression - add 1 to it and print that
  
def double(n):
    return n * 2

result = double(7)
print(result + 1)
print(double(7) + 1)
=======
# TODO: write double(n) using return (not print)
# TODO: add 1 to its result and print that
>>>>>>> upstream/main

# DISCUSS: A doubling function's result + 1 raises TypeError. Likely cause?
# Your answer:
#
