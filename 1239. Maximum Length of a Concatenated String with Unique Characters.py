class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Helper function for backtracking
        def backtrack(index, current_string):
            # Base case: if we've considered all strings
            if index == len(arr):
                return len(current_string)

            # Initialize max_length for this path
            max_length = 0

            # Option 1: Skip the current string
            # Continue with the next string without adding the current string
            max_length = max(max_length, backtrack(index + 1, current_string))

            # Option 2: Include the current string, if it's safe to do so
            # Check if adding current string causes duplicate characters
            if len(set(arr[index]) - set(current_string)) == len(arr[index]):
                # If safe, add the length of current string to total length and continue
                max_length = max(max_length, backtrack(index + 1, current_string + arr[index]))

            # Return the maximum length found in this path
            return max_length

    
        # Start the backtracking process from the first string
        return backtrack(0, "")
