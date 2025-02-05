def gravity_flip(n, columns):
    # Sort the columns in ascending order to simulate the gravity switch
    columns.sort()
    return columns

# Read input
n = int(input())
columns = list(map(int, input().split()))

# Get the result after gravity switch
result = gravity_flip(n, columns)

# Output the result
print(" ".join(map(str, result)))
