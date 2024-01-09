import heapq

def findKthLargest(nums, k):
    # Create a min heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Iterate through the remaining elements in the array
    for num in nums[k:]:
        # If the current element is greater than the smallest element in the min heap
        # (i.e., the root of the heap), replace the root with the current element
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    # The min heap now contains the k largest elements, with the smallest among them
    # at the root. So, the root is the kth largest element.
    return min_heap[0]
