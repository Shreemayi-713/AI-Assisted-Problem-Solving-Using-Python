def print_multiples(num):
    print(f"First 10 multiples of {num} are:")
    i = 1
    while i <= 10:
        print(num * i)
        i += 1

# Input from user
number = int(input("Enter a number: "))
print_multiples(number)
