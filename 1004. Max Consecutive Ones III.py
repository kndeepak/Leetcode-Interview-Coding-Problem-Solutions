class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_length = 0
        zero_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                
            # If zero count exceeds k, move the start pointer
            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            # Update the maximum length
            max_length = max(max_length, i - start + 1)
            
        return max_length
