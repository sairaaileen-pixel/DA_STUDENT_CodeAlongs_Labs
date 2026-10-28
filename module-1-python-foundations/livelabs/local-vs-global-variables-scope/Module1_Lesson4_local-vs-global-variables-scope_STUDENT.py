#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
#
print('----- 1. Local Scope, Live -----')
<<<<<<< HEAD
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
=======
# TODO: define make_total(): set a local total to 100 and return it
# TODO: print total outside the function and see what happens

# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
# Your answer:
>>>>>>> upstream/main
#


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
<<<<<<< HEAD
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
=======
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
#
>>>>>>> upstream/main


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
<<<<<<< HEAD
# rewrite price_with_tax so tax_rate is a parameter
# instead of a global it secretly reads

=======
# TODO: rewrite price_with_tax to take tax_rate as a parameter
>>>>>>> upstream/main
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