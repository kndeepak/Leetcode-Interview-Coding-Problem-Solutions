class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append a zero at the end of the cost array to represent the top of the stairs
        cost.append(0)

        # Iterate backwards through the cost array, starting from the third-last element
        for i in range(len(cost) - 3, -1, -1):
            # Update the cost at the current step by adding the minimum cost of the next two steps
            # This represents the minimum cost to climb to the top from this step
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum cost of the first two steps, as we can start from either of them
        return min(cost[0], cost[1])
