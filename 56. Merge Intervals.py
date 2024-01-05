class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals by their start values
        intervals.sort(key=lambda i: i[0])

        # Initialize the output list with the first interval
        output = [intervals[0]]

        # Iterate through the sorted intervals
        for start, end in intervals[1:]:
            # Get the end value of the last interval in the output list
            lastEnd = output[-1][1]

            # Check if the current interval overlaps with the last interval
            if start <= lastEnd:
                # Merge the intervals by updating the end value of the last interval
                output[-1][1] = max(lastEnd, end)
            else:
                # If there is no overlap, add the current interval to the output list
                output.append([start, end])

        return output
