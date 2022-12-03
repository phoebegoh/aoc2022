# AOC2022
# Day 1, Part 1: find the largest sum of sequential numbers separated by a newline

# Step 1: Split input file into sets of elf weights
data = []
with open('day1_input','r') as f:
  data = f.read().split('\n\n')

# Step 2: Convert sets into integers
data = [d.split() for d in data]
calories = [list(map(int,d)) for d in data]

# Step 3: Find the sums of calories, then find the max
calories = [sum(c) for c in calories]

print("Solution 1:", max(calories))

# Day 1, Part 2: Find the top 3 maximum values in the list
calories.sort()
calories.reverse()
print("Solution 2:", calories[0] + calories[1] + calories[2])
