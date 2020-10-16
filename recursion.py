def fact(x):
    """Calculate the factorial of a number"""
    if x == 1:
        return 1
    else:
        return x * fact(x-1)    # recusive function call stack


x = 5
print(f"The factorial of {x} is {fact(x)}\n")


def countdown(i):
    """Countdown functon"""
    print(i)
    if i <= 0:              # base case
        return
    else:
        countdown(i-1)      # recursive case


i = 6
print(f"\nLet's countdown from {i}:")
countdown(i)
