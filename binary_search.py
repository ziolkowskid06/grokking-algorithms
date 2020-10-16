def binary_search(list, item):
    """Binary search algorithm displays index of a guessed number"""
    low = 0                   # lower limit (first index)
    high = len(list) - 1      # upper limit (last index)
    while low <= high:
        mid = int((low + high)//2)
        guess = list[mid]       # check middle element
        if guess == item:       # item found
            return mid
        if guess > item:        # guess is too high
            high = mid - 1
        else:                   # guess is too low
            low = mid + 1
    return None                 # item doesn't exist


my_list = [1, 4, 5, 6, 7, 9]
print(binary_search(my_list, 7))
