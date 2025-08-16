def find_missing_number(arr):
    """
    Finds the missing number in an array of distinct integers from 1 to n.
    The array contains n-1 elements.
    
    Args:
        arr: A list of integers.
    
    Returns:
        The missing integer.
    """
    n = len(arr) + 1  # Since the array has n-1 elements, the total count is n
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2  # Using integer division
    
    # Calculate the sum of the elements in the given array
    actual_sum = sum(arr)
    
    # The difference is the missing number
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Test Cases:
# Test Case 1
arr1 = [1, 2, 4, 5]
print(f"Input: {arr1}, Missing number: {find_missing_number(arr1)}")

# Test Case 2
arr2 = [2, 3, 4, 5]
print(f"Input: {arr2}, Missing number: {find_missing_number(arr2)}")

# Test Case 3
arr3 = [1, 2, 3, 4]
print(f"Input: {arr3}, Missing number: {find_missing_number(arr3)}")

# Test Case 4
arr4 = [1]
print(f"Input: {arr4}, Missing number: {find_missing_number(arr4)}")

# Test Case 5
arr5 = list(range(1, 1000000))
arr5.remove(500000)
print(f"Input: [1, 2, ..., 999999] (missing 500000), Missing number: {find_missing_number(arr5)}")

# Test Case 6 (Edge Case - Smallest possible array)
arr6 = [1]
print(f"Input: {arr6}, Missing number: {find_missing_number(arr6)}")

# Test Case 7 (Edge Case - The missing number can be 1 or 2)
arr7 = [2]
print(f"Input: {arr7}, Missing number: {find_missing_number(arr7)}")
