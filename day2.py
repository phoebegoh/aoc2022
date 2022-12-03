# AOC2022
# Day 2: Calculate the final score of the strategy guide.
# Column 1: A = rock, B = paper, C = scissors
# Column 2: X = rock (1), Y = paper (2), Z = scissors (3)
# Outcome:
  # Win:  [A,Y] | [C,X] | [B,Z] = 6
  # Draw: [B,Y] | [A,X] | [C,Z] = 3
  # Loss: [C,Y] | [B,X] | [A,Z] = 0
# Score = Shape score (1,2,3) + outcome score (0, 3 or 6)
  
# Step 1: Get inputs
data = []
with open('day2_input','r') as f:
  data = [line.split() for line in f.read().splitlines()]

#print(data)

# Step 2: For each round, determine outcome
score = 0
for round in data:
  
  # Get shape score and outcome score
  if (round[0] == 'C' and round[1] == 'X'): score += 7
  if (round[0] == 'A' and round[1] == 'Y'): score += 8
  if (round[0] == 'B' and round[1] == 'Z'): score += 9
  if (round[0] == 'A' and round[1] == 'X'): score += 4
  if (round[0] == 'B' and round[1] == 'Y'): score += 5
  if (round[0] == 'C' and round[1] == 'Z'): score += 6
  if (round[0] == 'B' and round[1] == 'X'): score += 1
  if (round[0] == 'C' and round[1] == 'Y'): score += 2
  if (round[0] == 'A' and round[1] == 'Z'): score += 3
    
  
print("Day 2 Solution 1:", score)



# Part 2:
# round[0] = A (rock), B (paper), C (scissors)
# round[1] = X (lose), Y (draw), Z (win)
# rock (1), paper (2), scissors (3)
# So we need to determine the shape + its corresponding score.
  # Win:  [A,Z] | [B,Z] | [C,Z] 
  # Draw: [A,Y] | [B,Y] | [C,Y] 
  # Loss: [A,X] | [B,X] | [C,X] 

score = 0
for round in data:
  if (round[1] == 'X' and round[0] == 'A'): score += 3
  if (round[1] == 'X' and round[0] == 'B'): score += 1
  if (round[1] == 'X' and round[0] == 'C'): score += 2
  if (round[1] == 'Y' and round[0] == 'A'): score += 4
  if (round[1] == 'Y' and round[0] == 'B'): score += 5
  if (round[1] == 'Y' and round[0] == 'C'): score += 6
  if (round[1] == 'Z' and round[0] == 'A'): score += 8
  if (round[1] == 'Z' and round[0] == 'B'): score += 9
  if (round[1] == 'Z' and round[0] == 'C'): score += 7


print("Day 2 Solution 2:",score)
