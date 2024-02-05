class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Initialize the character count dictionary
        char_count = {}

        # First pass: count the characters
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
        # Second pass: find the index of the first unique character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no unique character is found, return -1
        return -1

        
