# Program to calculate sum of odd and even numbers in a list

# Sample list of numbers
numbers = [10, 15, 22, 33, 40, 55, 60]

# Initialize sums
sum_even = 0
sum_odd = 0

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        sum_even += num    # Add to even sum
    else:
        sum_odd += num     # Add to odd sum

# Display the results
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

