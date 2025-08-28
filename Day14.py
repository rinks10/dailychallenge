def count_substrings_with_k_distinct(s: str, k: int) -> int:
    """
    Counts the number of substrings with exactly k distinct characters.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The integer representing the number of distinct characters.

    Returns:
        The total number of substrings with exactly k distinct characters.
    """
    
    def count_at_most_k(s, k):
        """
        Helper function to count substrings with at most k distinct characters.
        """
        if k < 0:
            return 0
        
        count = 0
        left = 0
        freq = {}
        for right
