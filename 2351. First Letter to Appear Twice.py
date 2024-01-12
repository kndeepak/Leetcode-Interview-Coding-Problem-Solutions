class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Initialize an empty set to store the unique characters encountered
        hashset = set()

        # Iterate over each character in the string
        for string in s:
            # Check if the current character is already in the hashset
            if string in hashset:
                # If it is, that means we've encountered it before, so return it as the first repeated character
                return string 
            else:
                # If it's not in the hashset, add it to the set for future reference
                hashset.add(string)
