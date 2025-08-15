def sort_0s_1s_2s(arr):
    """
    Sorts an array containing only 0s, 1s, and 2s in-place.
    Uses the Dutch National Flag Algorithm.
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example Usage:
# Test Case 1:
arr1 = [0, 1, 2, 1, 0]
print(f"Input: {arr1}")
sort_0s_1s_2s(arr1)
print(f"Output: {arr1}")

# Test Case 2:
arr2 = [2, 0, 1, 2, 2]
print(f"Input: {arr2}")
sort_0s_1s_2s(arr2)
print(f"Output: {arr2}")

# Test Case 3:
arr3 = [1, 0, 1, 0, 0]
print(f"Input: {arr3}")
sort_0s_1s_2s(arr3)
print(f"Output: {arr3}")

# Test Case 4:
arr4 = [1, 1, 1, 1]
print(f"Input: {arr4}")
sort_0s_1s_2s(arr4)
print(f"Output: {arr4}")

# Test Case 5:
arr5 = [0, 0, 1, 1]
print(f"Input: {arr5}")
sort_0s_1s_2s(arr5)
print(f"Output: {arr5}")

# Test Case 6:
arr6 = []
print(f"Input: {arr6}")
sort_0s_1s_2s(arr6)
print(f"Output: {arr6}")
