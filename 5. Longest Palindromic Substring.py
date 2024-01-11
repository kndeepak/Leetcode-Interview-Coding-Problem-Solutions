class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        def expandAroundCenter(left: int, right: int) -> str:
            """
            Expand around the center to find the longest palindrome.
            Update the longest palindrome found.
            """
            nonlocal res
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Use max() to keep the longer palindrome
                if len(res) < (right - left + 1):
                    res = s[left:right+1]
                left -= 1
                right += 1

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check for odd length palindromes (centered at i)
            expandAroundCenter(i, i)

            # Check for even length palindromes (centered between i and i + 1)
            expandAroundCenter(i, i + 1)

        # Return the longest palindrome found in the entire string
        return res
