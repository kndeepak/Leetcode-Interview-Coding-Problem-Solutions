
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (for the smaller half of the numbers, will store negatives)
        self.large = []  # Min heap (for the larger half of the numbers)

    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large
        
        # Always start by adding to small (max heap), then rebalance
        heapq.heappush(small, -num)  # Push negated num to small to maintain it as a max heap
        
        # Ensure every num in small is less than every num in large
        if small and large and (-small[0] > large[0]):
            val = -heapq.heappop(small)
            heapq.heappush(large, val)
        
        # Balance the heaps if necessary
        if len(small) + 1 < len(large):
            val = heapq.heappop(large)
            heapq.heappush(small, -val)
        elif len(large) + 1 < len(small):
            val = -heapq.heappop(small)
            heapq.heappush(large, val)

    def findMedian(self) -> float:
        small = self.small
        large = self.large
        
        if len(small) > len(large):
            return -small[0]  # For max heap, invert the sign to get the actual value
        elif len(large) > len(small):
            return large[0]
        else:
            # If equal, take the average of the two middle values
            return (-small[0] + large[0]) / 2
