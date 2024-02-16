class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the occurrences of each number
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        # Sort the items by their counts (ascending order)
        sorted_items = sorted(count_map.items(), key=lambda item: item[1])

        # Remove elements to minimize the number of unique integers
        for key, value in sorted_items:
            if k >= value:
                k -= value
                del count_map[key]
            else:
                break

        # The remaining number of unique integers
        return len(count_map)
