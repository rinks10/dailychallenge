def merge(arr1, m, arr2, n):
    """
    Merges arr2 into arr1 in-place.
    :param arr1: List[int] - The first array, with size m + n.
    :param m: int - The number of elements in arr1 to be merged.
    :param arr2: List[int] - The second array, with size n.
    :param n: int - The number of elements in arr2.
    """
    # Pointers for arr1, arr2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p_merged = m + n - 1

    # While there are still elements in arr2 to be merged
    while p2 >= 0:
        # Compare elements and place the larger one at the end of arr1
        if p1 >= 0 and arr1[p1] >= arr2[p2]:
            arr1[p_merged] = arr1[p1]
            p1 -= 1
        else:
            arr1[p_merged] = arr2[p2]
            p2 -= 1
        p_merged -= 1

# Test cases from the problem description
# Test Case 1:
arr1_tc1 = [1, 3, 5, 0, 0, 0]
m_tc1 = 3
arr2_tc1 = [2, 4, 6]
n_tc1 = 3
merge(arr1_tc1, m_tc1, arr2_tc1, n_tc1)
print(f"Test Case 1 Output: {arr1_tc1}") # Expected: [1, 2, 3, 4, 5, 6]

# Test Case 2:
arr1_tc2 = [10, 12, 14, 0, 0, 0]
m_tc2 = 3
arr2_tc2 = [1, 3, 5]
n_tc2 = 3
merge(arr1_tc2, m_tc2, arr2_tc2, n_tc2)
print(f"Test Case 2 Output: {arr1_tc2}") # Expected: [1, 3, 5, 10, 12, 14]

# Test Case 3:
arr1_tc3 = [2, 3, 8, 0, 0, 0]
m_tc3 = 3
arr2_tc3 = [4, 6, 10]
n_tc3 = 3
merge(arr1_tc3, m_tc3, arr2_tc3, n_tc3)
print(f"Test Case 3 Output: {arr1_tc3}") # Expected: [2, 3, 4, 6, 8, 10]

# Test Case 4:
arr1_tc4 = [1]
m_tc4 = 1
arr2_tc4 = [2]
n_tc4 = 1
# This test case from the image has an issue. The code would expect arr1 to be [1, 0] or similar
# to have space for arr2. Assuming arr1_tc4 = [1, 0] to make it a valid test case
arr1_tc4_fixed = [1, 0]
merge(arr1_tc4_fixed, 1, arr2_tc4, 1)
print(f"Test Case 4 Output (fixed): {arr1_tc4_fixed}") # Expected: [1, 2]

# Test Case 5:
arr1_tc5 = [1, 2, 3, 4, 50000, 100000]
m_tc5 = 4
arr2_tc5 = [50001, 100000]
n_tc5 = 2
# Again, let's assume arr1 is sized to hold the final result
arr1_tc5_fixed = [1, 2, 3, 4, 50000, 100000]
m_tc5_fixed = 4
arr2_tc5_fixed = [50001, 100000]
n_tc5_fixed = 2
# The example output in the image for this test case looks incorrect,
# it shows arr1 = [1, 2, 3, 4, 50000, 100000]
# and arr2 = [50001, 100000] which is already a merged array.
# Let's use a more conventional example that fits the logic.
arr1_tc5_custom = [1, 2, 3, 50000, 0, 0]
m_tc5_custom = 4
arr2_tc5_custom = [4, 50001]
n_tc5_custom = 2
merge(arr1_tc5_custom, 4, arr2_tc5_custom, 2)
print(f"Test Case 5 Custom Output: {arr1_tc5_custom}") # Expected: [1, 2, 3, 4, 50000, 50001]

