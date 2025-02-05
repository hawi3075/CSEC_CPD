# Read input
n = int(input())
s = input().strip()

# Initialize counters
anton_wins = 0
danik_wins = 0

# Count wins for Anton and Danik
for char in s:
    if char == 'A':
        anton_wins += 1
    elif char == 'D':
        danik_wins += 1

# Determine the result
if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
