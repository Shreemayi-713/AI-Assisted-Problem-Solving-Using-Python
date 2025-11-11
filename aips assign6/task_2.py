def print_multiples(num):
    print(f"First 10 multiples of {num} are:")
    for i in range(1, 11):
        print(num * i)

# Input from user
number = int(input("Enter a number: "))
print_multiples(number)
