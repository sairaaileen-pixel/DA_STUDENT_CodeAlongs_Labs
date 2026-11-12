#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# Assign `names` and `bikes` to two empty lists
names = []
bikes = []
# Loop over `stations`; append each one's "name" to `names`
for station in stations:
    names.append(station["name"])
# Append the same station's "bikes_available" to `bikes`
    bikes.append(station["bikes_available"])
names.pop(2)

print("stations in the file:", len(stations))
# Loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):

 print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
# The data file contains 10 records representing different bike-share stations. 
# Each record is a dictionary. The fields "station_id" and "name" are text strings, 
# "capacity" and "bikes_available" are whole numbers (integers), and "needs_maintenance" 
# is a boolean. What looks wrong in the old report model is that keeping separate 
# parallel lists for names and counts makes them fragile; deleting or shifting an item 
# in one list immediately desynchronizes both.

# Step 1, answer 2:
# .pop(2) removes the element at index 2 ("W 52 St & 11 Ave") from the `names` list, 
# returns that string, and shifts all next elements in `names` one position to 
# the left, reducing the total length of `names` to 9.

# Step 1, answer 3:
# Because `names` shrank by 1 while `bikes` stayed at length 10, every station starting 
# from index 2 gets paired with the bike count of the station immediately after it. 
# "W 52 St & 11 Ave" completely disappears from the names list, and its original 
# bike count is quietly misattributed to "Cooper Square & Astor Pl".

# OOP Exceeds Note:
# If using parallel lists instead of objects, adding a new station requires manually 
# inserting the new value at the exact same index across 5 separate lists. 
# If an index gets out of sync, all data points mismatch, breaking the system.


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # Add __init__ with name (str), capacity and bikes_available (int)
    # In __init__, assign each parameter to self.<same name>
    # Add a parameter and self.<name> for each extra field you agreed

    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
           self.station_id = station_id
           self.name = name
           self.capacity = capacity
           self.bikes_available = bikes_available
           self.needs_maintenance = needs_maintenance
   
    # Add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
       return self.bikes_available < (self.capacity/4)
          
       


# Assign `fleet` to []; loop over `stations` as `s`
fleet = []
for s in stations:
    station_obj = Station (
# TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
        s["station_id"],
        s["name"],
        s["capacity"],
        s["bikes_available"],
        s["needs_maintenance"]
    ) 
    fleet.append(station_obj)

# Assign `busy`, `quiet` to two stations with equal needs_restock()
busy = fleet[1]
quiet = fleet[3]
# Print both needs_restock() answers
print("Before change:")
print(f"{busy.name}, needs restock:", busy.needs_restock())
print(f"{quiet.name}, needs restock:", quiet.needs_restock())
# Set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0

print("After change:")
print(f"{busy.name} needs restock:", busy.needs_restock())
print(f"{quiet.name} needs restock:", quiet.needs_restock())


# Step 2, answer 1:
# - self.name ("station names")
# - self.station_id ("bikes identification numbers")
# - self.capacity ("station capacity to hold bikes")
# - self.bike_available ("bikes available in each station")
# - self.needs_maintenance("stations that need help")

# Step 2, answer 2:
# In my list the order of "station id" and "name" did not match the order of the original data file.
# I decided to change it to make my code is more organized.

# Step 2, answer 3:
# If we had to drop one field first, it would be `station_id`, because the dispatcher 
# never mentions ID codes—they only talk about directing vans and mechanics to station names. 
# However, we kept it in our system to ensure we could uniquely identify records in case 
# two stations ever share the same name.

# Step 2, answer 4:
# We tested Flatbush Ave and Cooper Square. Before any changes, both printed False 
# because they had plenty of bikes. When we dropped Flatbush Ave's bike count to 0, 
# its restock status flipped to True, but Cooper Square stayed False. This proves 
# that our two stations are completely independent because changing the data on one 
# object didn't affect the other object at all.


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# Copy your Station class from Step 2 here
class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
        
    def needs_restock(self):
           return self.bikes_available < (self.capacity/4)
              
# Add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
    def __str__(self):
        return (f"{self.name}: {self.bikes_available} of {self.capacity} bikes")

# Build it from self.name, self.bikes_available and self.capacity
# Rebuild `fleet` from this class with the same loop as Step 2
fleet = []
for s in stations:
    fleet.append(Station(
        s["station_id"],
        s["name"],
        s["capacity"],
        s["bikes_available"],
        s["needs_maintenance"]
    ))


print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
# 1: Memory adress.
# 2: Memory adress
# 3: Clean formatted sensence.
# 4: Something readable for humans.

# Step 3, answer 2:
# Prediction #4 was wrong. Lists ignore `__str__` and use `__repr__` instead, 
# which is why list prints still showed memory addresses.


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# Copy your Station class from Step 3 here
# Add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# Rebuild `fleet` from this class with the same loop as Step 2
# Assign `van_list` to []; loop over `fleet`
# Append each station whose needs_restock() returns True to `van_list`

class Station:
    def __init__(self, station_id, name, capacity, bikes_available, needs_maintenance):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < (self.capacity / 4)

    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"

    fleet = []
for s in stations:
    fleet.append(Station(
        s["station_id"],
        s["name"],
        s["capacity"],
        s["bikes_available"],
        s["needs_maintenance"]
    ))

    van_list = []

    for station in fleet:
        if station.needs_restock():
            van_list.append(station)

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# 4 stations, Python will use the "__repr__" method because it's printing a list.

# Step 4, answer 2:
# "__str__" gives readable text for everyday users/dispatchers, while "__repr__" gives developer-friendly details for code and lists.

# Step 4, answer 3:
# We would hand the dispatcher the printout using the human-readable `__str__` format. 
# Dispatchers need clear, plain-English information (like station names and exact bike counts) 
# to quickly plan their routes, rather than developer code or constructor syntax like `Station('Name', 4)`.
