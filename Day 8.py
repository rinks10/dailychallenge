def reverse_words(s: str) -> str:
    """
    Reverses the order of words in a string.

    The function handles leading, trailing, and multiple spaces
    between words, reducing them to a single space.

    Args:
        s: The input string.

    Returns:
        The string with the words reversed and formatted as specified.
    """
    # Split the string by spaces. This handles multiple spaces and removes leading/trailing spaces.
    words = s.split()

    # Reverse the list of words.
    words.reverse()

    # Join the reversed words with a single space.
    return " ".join(words)

# Example Usage:
# Example 1: Basic case
input1 = "the sky is blue"
output1 = reverse_words(input1)
print(f"Input: '{input1}'")
print(f"Output: '{output1}'")
print("-" * 20)

# Example 2: Leading/trailing spaces and multiple spaces between words
input2 = "  hello world  "
output2 = reverse_words(input2)
print(f"Input: '{input2}'")
print(f"Output: '{output2}'")
print("-" * 20)

# Example 3: Multiple spaces
input3 = "a good   example"
output3 = reverse_words(input3)
print(f"Input: '{input3}'")
print(f"Output: '{output3}'")
print("-" * 20)

# Example 4: Single word
input4 = "word"
output4 = reverse_words(input4)
print(f"Input: '{input4}'")
print(f"Output: '{output4}'")
print("-" * 20)

# Edge Case 1: Only spaces
input5 = "   "
output5 = reverse_words(input5)
print(f"Input: '{input5}'")
print(f"Output: '{output5}'")
print("-" * 20)

# Edge Case 2: Empty string
input6 = ""
output6 = reverse_words(input6)
print(f"Input: '{input6}'")
print(f"Output: '{output6}'")

