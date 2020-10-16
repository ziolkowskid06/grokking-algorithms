def findSmallest(arr):
    """Finds the smallest element in a array"""
    smallest = arr[0]       # stores the first value
    smallest_index = 0      # stores the index of the first value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]       # stores the smallest value
            smallest_index = i      # stores the index of the smallest value
    return smallest_index


def selectionSort(arr):
    """Sorts the array"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)        # finds the index of the smallest element
        newArr.append(arr.pop(smallest))    # add the smallest element to the new array
    return newArr


arr = [5, 3, 6, 2, 10]
print(selectionSort(arr))
print(arr)
