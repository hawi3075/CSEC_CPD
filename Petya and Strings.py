def compare_strings(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Read input
s1 = input().strip()
s2 = input().strip()

# Output the result
print(compare_strings(s1, s2))
