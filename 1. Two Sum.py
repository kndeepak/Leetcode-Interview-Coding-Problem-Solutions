class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i,j in enumerate(nums):
            tmp = target - j
            if tmp in hashmap:
                return [hashmap[tmp],i]
            hashmap[j] = i
        
