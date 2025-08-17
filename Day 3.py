def find_duplicate(nums):
    """
    Finds the duplicate number in an array without modifying the array.

    Args:
        nums: A list of integers where there is exactly one duplicate number.

    Returns:
        The duplicate integer.
    """
    # Initialize the tortoise and hare pointers
    tortoise = nums[0]
    hare = nums[0]

    # Phase 1: Find the intersection point of the two pointers
    # This loop will run at least once and is guaranteed to find an intersection
    while True:
        tortoise = nums[tortoise]  # Tortoise moves one step
        hare = nums[nums[hare]]    # Hare moves two steps

        if tortoise == hare:
            break

    # Phase 2: Find the entrance to the cycle
    # Reset one pointer and move both at the same speed to find the start of the cycle
    ptr1 = nums[0]
    ptr2 = tortoise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

# Test Cases
print(f"Test Case 1: [1, 3, 4, 2, 2] -> {find_duplicate([1, 3, 4, 2, 2])}")
print(f"Test Case 2: [3, 1, 3, 4, 2] -> {find_duplicate([3, 1, 3, 4, 2])}")
print(f"Test Case 3: [1, 1] -> {find_duplicate([1, 1])}")
print(f"Test Case 4: [1, 4, 4, 2, 3] -> {find_duplicate([1, 4, 4, 2, 3])}")
print(f"Test Case 5: [1, 2, ..., 99999, 50000] -> {find_duplicate(list(range(1, 100000)) + [50000])}")

