    n = len(arr)
        # Count the number of zeros in the original array.
        zero_count = arr.count(0)

        # Start from the end of the array and iterate backwards.
        for i in range(n - 1, -1, -1):
            # If the current element is zero, duplicate it and decrement the zero count.
            if arr[i] == 0:
                if i + zero_count < n:
                    arr[i + zero_count] = 0
                zero_count -= 1

            # Shift the elements to the right to make space for the duplicated zeros.
            if i + zero_count < n:
                arr[i + zero_count] = arr[i]
