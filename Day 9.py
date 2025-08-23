def longestCommonPrefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix, or "" if none exists.
    """
    # Edge Case: If the list is empty, return an empty string
    if not strs:
        return ""

    # Start with the first string as the initial prefix
    prefix = strs[0]

    # Iterate through the rest of the strings
    for i in range(1, len(strs)):
        current_str = strs[i]
        
        # While the current string does not start with the prefix,
        # shorten the prefix by one character from the end
        while not current_str.startswith(prefix):
            prefix = prefix[:-1]
            
            # If the prefix becomes empty, there is no common prefix
            if not prefix:
                return ""
    
    return prefix

# Test Cases (provided in the image)
# Example 1
print(f"Input: [\"flower\", \"flow\", \"flight\"]")
print(f"Output: \"{longestCommonPrefix([\"flower\", \"flow\", \"flight\"])}\"")
print("-" * 20)

# Example 2
print(f"Input: [\"dog\", \"racecar\", \"car\"]")
print(f"Output: \"{longestCommonPrefix([\"dog\", \"racecar\", \"car\"])}\"")
print("-" * 20)

# Test Case 3
print(f"Input: [\"apple\", \"ape\", \"april\"]")
print(f"Output: \"{longestCommonPrefix([\"apple\", \"ape\", \"april\"])}\"")
print("-" * 20)

# Edge Case 1: Empty array
print(f"Input: []")
print(f"Output: \"{longestCommonPrefix([])}\"")
print("-" * 20)

# Edge Case 2: Array with one string
print(f"Input: [\"alone\"]")
print(f"Output: \"{longestCommonPrefix([\"alone\"])}\"")
