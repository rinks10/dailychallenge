class Solution:
    def isValid(self, s: str) -> bool:
        """
        Solves the Valid Parentheses with Multiple Types problem.

        This function checks if a string containing '(', ')', '{', '}', '[' and ']'
        is valid. A string is considered valid if:
        1. Every opening bracket has a corresponding closing bracket of the same type.
        2. The brackets are closed in the correct order.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                # It's an opening bracket, push it to the stack
                stack.append(char)
            elif char in mapping.keys():
                # It's a closing bracket
                if not stack or mapping[char] != stack.pop():
                    # If the stack is empty or the top of the stack
                    # doesn't match the closing bracket, it's invalid.
                    return False
            else:
                # The character is not a bracket, could be a problem
