#!/usr/bin/env python3
"""Local vs. Global Variables & Scope
Module 1: Python Foundations

HOW TO RUN
    Open a terminal in the folder that holds this file (and any data
    file the code reads), then run:
        python3 Module1_Lesson4_local-vs-global-variables-scope_STUDENT.py
    Or make the file executable once:
        chmod +x Module1_Lesson4_local-vs-global-variables-scope_STUDENT.py
    and from then on run it directly:
        ./Module1_Lesson4_local-vs-global-variables-scope_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work: it names the program that runs this file.
    python3 <file> treats that line as a comment and ignores it.

Follow along: type each section as it comes up, then save and run the
file again after each section. Each section prints its own heading,
so you can tell which output belongs to which step.

Complete each TODO as you go. A ____ blank is not valid Python, so
fill it in before you run the file again.
"""

# ===== 1. Local Scope, Live =====
# Find out whether a variable made inside a function still exists outside of
# it.
# This is supposed to raise NameError: run it, read the traceback, then comment
# out the raising line so the rest of the file runs.
#
# DISCUSS: Before you run the Local Scope code, put these in the order they
#          happen. A: total stops existing. B: make_total() is called. C: total
#          is created and set to 100.
# Your answer:
#
#
print('----- 1. Local Scope, Live -----')
#  define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens


num_val = 0 # global variable

def make_total():
    total = 100 # local variable
    # print(total * 100)
    # return total
    # print(total)
    return total * num_val
    print(total)

# make_total()


# DISCUSS: Now try a new function. set_x() runs and sets x = 5 inside it, but
#          print(x) outside raises NameError. Why?

x = make_total()
#print(x)
#print make_total
# Your answer:
# Becuase we never defined our variable.
#


# ===== 2. Reading a Global, Live =====
# Work out the price of a $100 item with 8% tax, using a tax rate stored
# outside the function.
print('----- 2. Reading a Global, Live -----')
# define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter

tax_rate = 0.8

def price_with_tax(price):
    x = price + (price * tax_rate)
    return x

print(price_with_tax(5.00))
print(price_with_tax(100.00))

                
# DISCUSS: Copy the price_with_tax function from the Reading a Global code into
#          a new file, without the tax_rate = 0.08 line. It worked here. Why
#          does it break there?
# Your answer:
# Because of the variable scope (local/ global)
# It secretly depends on a missing global.


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter, so the function only uses what it is
# given. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
# rewrite price_with_tax so tax_rate is a parameter
# instead of a global it secretly reads

tax_rate = 0.08

def price_with_tax(price, c_tax_rate):
     return price + (price * c_tax_rate)


print(price_with_tax(20, tax_rate))
#print(price_with_tax(100.00))



"""def add():
    count = 0
    count = count + 1
    return count
print(add)"""