class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initial sum of the first 'k' elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Sliding the window
        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, window_sum)

        # Calculating the maximum average
        return max_sum / k
