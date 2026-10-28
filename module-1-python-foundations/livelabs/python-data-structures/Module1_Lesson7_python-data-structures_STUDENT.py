#!/usr/bin/env python3
"""Day 7 code-along: Python Data Structures. Run: python3 <file> or ./<file>"""

# ===== 1. Lists Let You Change Anything, Anytime =====
# Build a list of order IDs, add one, rename the first, and print the results.
print('----- 1. Lists Let You Change Anything, Anytime -----')
# TODO: create a list called pending_orders
# TODO: put "ORD-1001", "ORD-1002" and "ORD-1003" in it


# TODO: append "ORD-1004" to pending_orders


# TODO: change pending_orders[0] to "ORD-1001-R" (lists are mutable)


# TODO: print pending_orders, its length, and its last item (use [-1])


# ===== 2. Once Locked In, a Tuple Can't Be Changed =====
# Store a log entry in a tuple, unpack it, then try to change it.
# TODO: run it, read the TypeError, then comment out the raising line
print("----- 2. Once Locked In, a Tuple Can't Be Changed -----")
# TODO: create a tuple called log_entry: timestamp, level, status code
# TODO: use any timestamp string, "ERROR" and 500


# TODO: unpack log_entry into timestamp, level, status


# TODO: print an f-string showing level, timestamp, and status


# TODO: try log_entry[0] = a new timestamp (this SHOULD raise an error)


# ===== 3. Only Hashable Values Can Be Dict Keys =====
# Add and update products in a dict, then print each SKU and its stock.
# TODO: fill in each ____ blank
print('----- 3. Only Hashable Values Can Be Dict Keys -----')
product_stock = {"SKU-1001": 92, "SKU-2002": 34}
product_stock["SKU-3003"] = 8
product_stock["SKU-1001"] = 89

for sku, count in product_stock.____():
    print(f"{sku}: {count}")


# ===== 4. Sets Make Membership Checks Instant =====
# Track IDs in a set, add a duplicate, and check if an ID is in the set.
print('----- 4. Sets Make Membership Checks Instant -----')
# TODO: create a set called seen_ids with 101, 102, and 103


# TODO: add 102 again - what happens? (sets have no duplicates)


# TODO: add a new id, 104


# TODO: print seen_ids, then check if 103 is in seen_ids


# ===== 5. The Cost of Checking a List Adds Up =====
# This code times a search for one number in a list of 2 million numbers.
# TODO: run this and read the output
print('----- 5. The Cost of Checking a List Adds Up -----')
import time

user_id_list = list(range(2_000_000))

start = time.time()
found = 1_999_999 in user_id_list
elapsed = time.time() - start

print(f"Found: {found}")
print(f"Took {elapsed:.4f} sec to check membership")
