class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        return max(nums[0],self.houserobber_1(nums[1:]), self.houserobber_1(nums[:-1]))

        
        
        
        # Iterate through each house in the nums list
    def houserobber_1(self,nums):
        rob1 = 0  # Represents the maximum amount robbed two houses back
        rob2 = 0  # Represents the maximum amount robbed from the previous house


        for n in nums:
        # Calculate the maximum amount that can be robbed up to the current house
        # Either rob the current house plus the amount robbed two houses back,
        # or do not rob the current house and keep the amount robbed from the previous house
            temp = max(n + rob1, rob2)

            # Update rob1 and rob2 for the next iteration
            rob1 = rob2  # Previous maximum becomes the two-house-back maximum
            rob2 = temp  # Current maximum becomes the previous maximum

    # Return the maximum amount that can be robbed up to the last house
        return rob2

