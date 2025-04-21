import sys

# Read all input at once from standard input
data = sys.stdin.read().split()

# Convert input to integers
user_values = list(map(int, data))

# Safely check for correct input length
if len(user_values) != 10:
    print("Error: Expected 10 integers.")
    sys.exit()

# Initialize min, max, sum
min_val = user_values[0]
max_val = user_values[0]
sum_vals = 0

for num in user_values:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    sum_vals += num

# Compute average using float division
average = sum_vals / 10.0

# Print result
print(f"{min_val} {max_val} {average}")
