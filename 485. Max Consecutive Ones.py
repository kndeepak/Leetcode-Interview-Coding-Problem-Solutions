class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the maximum consecutive ones (output) and the current consecutive ones (temp).
        output = 0 
        temp = 0
        
        # Loop through the input list 'nums'.
        for i in range(len(nums)):
            if nums[i] == 1:
                # If the current element is 1, increment the 'temp' variable to count consecutive ones.
                temp += 1
                # Update the 'output' variable with the maximum of its current value and 'temp'.
                output = max(output, temp) 
            elif nums[i] == 0:
                # If the current element is 0, reset the 'temp' variable to 0 as consecutive ones are broken.
                temp = 0
        
        # Return the maximum consecutive ones found in the 'nums' list, which is stored in the 'output' variable.
        return output
