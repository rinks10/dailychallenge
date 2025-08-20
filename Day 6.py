def find_zero_sum_subarrays(nums):
    """
    Finds all subarrays with a zero sum in a given integer array.

    Args:
        nums: A list of integers.

    Returns:
        A list of tuples, where each tuple contains the starting and ending 
        indices of a zero-sum subarray.
    """
    sum_map = {0: [-1]}
    current_sum = 0
    result = []
    
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum in sum_map:
            for prev_index in sum_map[current_sum]:
                result.append((prev_index + 1, i))
        
        if current_sum in sum_map:
            sum_map[current_sum].append(i)
        else:
            sum_map[current_sum] = [i]
            
    return result


print(f"Test Case 1: [4, 1, -3, 1, 2, -1] -> {find_zero_sum_subarrays([4, 1, -3, 1, 2, -1])}")
print(f"Test Case 2: [1, 2, 3, 4] -> {find_zero_sum_subarrays([1, 2, 3, 4])}")
print(f"Test Case 3: [0, 0, 0, 0, 0] -> {find_zero_sum_subarrays([0, 0, 0, 0, 0])}")
