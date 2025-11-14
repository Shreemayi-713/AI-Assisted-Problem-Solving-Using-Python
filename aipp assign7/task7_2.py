def count_down(n):
    while n > 0:
        print(n)
        n -= 1  # Fixed: decrement n by 1 each iteration

# Take input from user
n = int(input("Enter a number to count down from: "))
count_down(n)

