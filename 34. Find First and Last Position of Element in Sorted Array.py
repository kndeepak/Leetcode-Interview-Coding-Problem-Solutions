class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize left and right pointers for the binary search
        l, r = 0, len(nums) - 1
        
        # Initialize an empty list to store the output
        output = [-1, -1]  # Default values for not found

        # Binary search for the left boundary of the target
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                output[0] = mid  # Update left boundary index
                r = mid - 1  # Continue searching on the left side
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # Reset left and right pointers
        l, r = 0, len(nums) - 1

        # Binary search for the right boundary of the target
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                output[1] = mid  # Update right boundary index
                l = mid + 1  # Continue searching on the right side
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return output
