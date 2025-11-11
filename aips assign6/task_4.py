def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Input from user
num = int(input("Enter a number: "))
print("Sum of first", num, "numbers is:", sum_to_n(num))

