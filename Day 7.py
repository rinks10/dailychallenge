def trap(height: list[int]) -> int:
    """
    Calculates the amount of rainwater that can be trapped.
    
    Args:
        height: A list of non-negative integers representing an elevation map.
    
    Returns:
        The total units of water that can be trapped.
    """
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    while left <= right:
        if height[left] <= height[right]:
            # The water level is limited by the left side
            if height[left] > left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            # The water level is limited by the right side
            if height[right] > right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1

    return total_water

# Example Test Cases from the image:
print(f"Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], Output: {trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])}") # Expected: 6
print(f"Input: [4, 2, 0, 3, 2, 5], Output: {trap([4, 2, 0, 3, 2, 5])}") # Expected: 9
print(f"Input: [1, 1, 1], Output: {trap([1, 1, 1])}") # Expected: 0
print(f"Input: [5], Output: {trap([5])}") # Expected: 0
print(f"Input: [2, 0, 2], Output: {trap([2, 0, 2])}") # Expected: 2
