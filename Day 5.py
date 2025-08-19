def find_leaders(arr):
    """
    Finds all leader elements in an array.
    An element is a leader if it's greater than all elements to its right.
    The rightmost element is always a leader.
    
    Args:
        arr (list): A list of integers.
        
    Returns:
        list: A list containing the leader elements in the order they appear.
    """
    
    if not arr:
        return []

    n = len(arr)
    leaders = []
    
    # The rightmost element is always a leader
    max_right = arr[n - 1]
    leaders.append(max_right)

    # Iterate from the second-to-last element to the first
    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            leaders.append(max_right)
    
    # Reverse the leaders list to get the correct order
    leaders.reverse()
    
    return leaders

# --- Test Cases ---

# Test case 1 from the prompt
arr1 = [16, 17, 4, 3, 5, 2]
print(f"Input: {arr1}")
print(f"Output: {find_leaders(arr1)}")  # Expected Output: [17, 5, 2]

print("-" * 20)

# Test case 2 from the prompt
arr2 = [1, 2, 3, 4, 0]
print(f"Input: {arr2}")
print(f"Output: {find_leaders(arr2)}")  # Expected Output: [4, 0]

print("-" * 20)

# Test case 3 from the prompt
arr3 = [10, 4, 10, 6, 5, 2]
print(f"Input: {arr3}")
print(f"Output: {find_leaders(arr3)}")  # Expected Output: [10, 6, 5, 2]

print("-" * 20)

# Test case 4 from the prompt
arr4 = [5]
print(f"Input: {arr4}")
print(f"Output: {find_leaders(arr4)}") # Expected Output: [5]

print("-" * 20)

# Edge case: Sorted in descending order
arr_desc = [100, 50, 20, 10]
print(f"Input: {arr_desc}")
print(f"Output: {find_leaders(arr_desc)}") # Expected Output: [100, 50, 20, 10]

print("-" * 20)

# Edge case: All elements are the same
arr_same = [7, 7, 7, 7]
print(f"Input: {arr_same}")
print(f"Output: {find_leaders(arr_same)}") # Expected Output: [7]
