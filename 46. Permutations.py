class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Base case: if there's only one element, return it as the only permutation
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            # Remove the first element and generate permutations of the remaining list
            n = nums.pop(0)
            perms = self.permute(nums)

            # Add the removed element back to each generated permutation
            for perm in perms:
                perm.append(n)

            # Add the new permutations to the result list
            result.extend(perms)

            # Append the removed element back to nums for the next iteration
            nums.append(n)

        return result
