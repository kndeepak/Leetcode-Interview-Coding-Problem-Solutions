class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

       
        result = 0
        
        for char in columnTitle:
            # Convert the character to its corresponding integer value
            value = ord(char) - ord('A') + 1
            
            # Update the result by multiplying it by 26 and adding the new value
            result = result * 26 + value
        
        return result
