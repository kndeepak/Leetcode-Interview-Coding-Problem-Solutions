class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Manually create a frequency map
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        count = 0
        for t in freq_map.values():
            if t == 1:  # If any number occurs only once, return -1
                return -1
            count += t // 3  # Add the count of triplet operations
            if t % 3:  # If there's a remainder, add an operation for a pair or a single element
                count += 1

        return count
