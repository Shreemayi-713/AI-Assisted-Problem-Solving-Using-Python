def sum_to_n(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Input from user
num = int(input("Enter a number: "))
print("Sum of first", num, "numbers is:", sum_to_n(num))
