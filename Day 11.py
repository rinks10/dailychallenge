from itertools import permutations

def get_unique_permutations(s):
    """
    Generates all unique permutations of a string.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        A list of strings, where each string is a unique permutation
        of the input string.
    """
    # Use the permutations function from the itertools library
    # to generate all possible permutations of the string.
    # The result is a list of tuples.
    all_permutations = permutations(s)

    # Convert the list of tuples into a list of strings and
    # use a set to automatically handle unique permutations.
    unique_permutations = set([''.join(p) for p in all_permutations])

    # Convert the set back to a list and sort it for a consistent output.
    # The order of permutations in the output does not matter as per the prompt.
    # However, sorting provides a deterministic result.
    return sorted(list(unique_permutations))

# --- Test Cases ---
print("Test Case 1:")
input_str_1 = "abc"
output_1 = get_unique_permutations(input_str_1)
print(f"Input: '{input_str_1}'")
print(f"Output: {output_1}\n")

print("Test Case 2:")
input_str_2 = "aba"
output_2 = get_unique_permutations(input_str_2)
print(f"Input: '{input_str_2}'")
print(f"Output: {output_2}\n")

print("Test Case 3:")
input_str_3 = "aaa"
output_3 = get_unique_permutations(input_str_3)
print(f"Input: '{input_str_3}'")
print(f"Output: {output_3}\n")

print("Test Case 4:")
input_str_4 = "a"
output_4 = get_unique_permutations(input_str_4)
print(f"Input: '{input_str_4}'")
print(f"Output: {output_4}\n")

print("Test Case 5:")
input_str_5 = "abcd"
output_5 = get_unique_permutations(input_str_5)
print(f"Input: '{input_str_5}'")
print(f"Output: {output_5}\n")

