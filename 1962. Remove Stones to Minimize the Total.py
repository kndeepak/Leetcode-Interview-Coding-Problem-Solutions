class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Convert the piles to a max heap (negate the values to use it as a max heap)
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            # Pop the pile with the maximum number of stones
            max_pile = -heapq.heappop(max_heap)
            
            # Remove half of the stones from the pile and push it back
            new_pile = max_pile - (max_pile // 2)
            heapq.heappush(max_heap, -new_pile)
            
            
        # Calculate the total number of stones remaining
        total_stones = sum([-pile for pile in max_heap])                
        return total_stones
