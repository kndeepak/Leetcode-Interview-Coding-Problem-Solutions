class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        
        
        # Define the word "balloon" and the required frequency of each character
        word = "balloon"
        required_char_count = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        
        char_count = {}
        
        # Initialize the character count dictionary
        for char in word:
            char_count[char] = 0


        # Count the frequency of each character in the input text
        for char in text:
            if char in char_count:
                char_count[char] += 1
            
         # Find the maximum number of instances that can be formed
        min_instances = float('inf')  # Initialize with positive infinity
        
        for char, count in required_char_count.items():
            if count > 0:
                min_instances = min(min_instances, char_count[char] // count)
                
        return min_instances
