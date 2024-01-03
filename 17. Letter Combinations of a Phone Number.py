class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Initialize an empty list to store the resulting letter combinations
        res = []
        
        # Define a dictionary mapping digits to their corresponding letters
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Define a recursive function to generate letter combinations
        def back(i, curstr):
            # If the current string has the same length as the input digits, it's a valid combination
            if len(curstr) == len(digits):
                res.append(curstr)
                return

            # Iterate through the letters corresponding to the current digit
            for c in digitToChar[digits[i]]:
                # Recursively call 'back' to append the current letter to the combination
                back(i + 1, curstr + c)

        # Check if the input 'digits' is not empty
        if digits:
            # Start the recursive process with index 0 and an empty string
            back(0, "")

        # Return the list of generated letter combinations
        return res
