class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to facilitate skipping duplicates
        nums.sort()
        perm = []
        result = []
        count = {n: 0 for n in nums}
        
        # Count the frequency of each number
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            # Iterate through each unique number
            for n in count:
                if count[n] > 0:
                    # Add the number to the current permutation
                    perm.append(n)
                    count[n] -= 1

                    # Continue with DFS
                    dfs()

                    # Backtrack
                    count[n] += 1
                    perm.pop()

        dfs()
        return result
