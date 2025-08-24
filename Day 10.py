def solve():
    """
    Solves the Group Anagrams problem.
    """

    def group_anagrams(strs: list[str]) -> list[list[str]]:
        """
        Groups anagrams from a list of strings.

        Args:
            strs: A list of strings containing lowercase English letters.

        Returns:
            A list of lists, where each sublist contains strings that are anagrams of each other.
            The order of the output groups does not matter.
        """
        anagram_groups = {}  # Using a dictionary to store anagram groups
        for s in strs:
            # Sort the string to create a canonical key for anagrams.
            # For example, "eat", "tea", and "ate" all become "aet" when sorted.
            # This sorted string serves as the key for our dictionary.
            sorted_s = "".join(sorted(s))

            # If the key is not in the dictionary, create a new list for it.
            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []

            # Append the original string to the list associated with its sorted key.
            anagram_groups[sorted_s].append(s)

        # The values of the dictionary are the lists of grouped anagrams.
        return list(anagram_groups.values())

    # --- Test Cases from the Problem Description ---
    # Example 1
    input_strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output1 = group_anagrams(input_strs1)
    print(f"Input: {input_strs1}")
    print(f"Output: {output1}")
    print("-" * 20)

    # Test Case 1
    input_strs2 = [""]
    output2 = group_anagrams(input_strs2)
    print(f"Input: {input_strs2}")
    print(f"Output: {output2}")
    print("-" * 20)

    # Test Case 2
    input_strs3 = ["a"]
    output3 = group_anagrams(input_strs3)
    print(f"Input: {input_strs3}")
    print(f"Output: {output3}")
    print("-" * 20)

    # Additional Test Cases from the Problem Description
    input_strs4 = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
    output4 = group_anagrams(input_strs4)
    print(f"Input: {input_strs4}")
    print(f"Output: {output4}")
    print("-" * 20)

    input_strs5 = ["abc", "def", "ghi"]
    output5 = group_anagrams(input_strs5)
    print(f"Input: {input_strs5}")
    print(f"Output: {output5}")
    print("-" * 20)

# Run the solution
solve()
