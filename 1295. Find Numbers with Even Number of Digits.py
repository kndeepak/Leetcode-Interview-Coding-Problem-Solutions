class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def countDigits(num):
        # Helper function to count the number of digits in a number.
            count = 0
            while num > 0:
                count += 1
                num //= 10
            return count

        even_digits_count = 0  # Initialize a counter for numbers with even digits.

        for num in nums:
            if countDigits(num) % 2 == 0:
                even_digits_count += 1

        return even_digits_count
