class Solution:
    def countAndSay(self, n: int) -> str:

    
        # Base case: If n is 1, return "1" as the first term of the sequence
        if n == 1:
            return "1"
        
        # Recursively compute the (n-1)th term of the sequence
        prev = self.countAndSay(n - 1)
        
        # Initialize variables to build the current term
        res = ""    # The current term being built
        count = 1   # Counter for the current digit's occurrences
        
        # Iterate through the (n-1)th term to generate the nth term
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                # If the current digit is the same as the previous one, increment the counter
                count += 1
            else:
                # If the current digit is different, append the count and digit of the previous group
                res += str(count) + prev[i - 1]
                count = 1  # Reset the counter for the new group
        
        # Append the count and digit of the last group
        res += str(count) + prev[-1]
        
        return res
