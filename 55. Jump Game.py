class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the goal as the last index of the list
        goal = len(nums) - 1

        # Traverse the list in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # If we can jump from the current position to or beyond the goal
            if i + nums[i] >= goal:
                # Update the goal to the current position
                goal = i

        # After the loop, if the goal is at the start (index 0), it means we can jump to the end
        if goal == 0:
            return True
        else:
            return False

