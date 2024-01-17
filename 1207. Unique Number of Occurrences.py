class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Create a hashmap to store the frequency of each element in arr
        hashmap = {}
        for i in range(len(arr)):
            # If the element is not in the hashmap, add it with a count of 1
            if arr[i] not in hashmap:
                hashmap[arr[i]] = 1
            # If the element is already in the hashmap, increment its count
            elif arr[i] in hashmap:
                hashmap[arr[i]] += 1

        # Create a list to store the frequencies of elements
        values_list = []
        for value in hashmap.values():
            values_list.append(value)  # Append each frequency to the values_list

        # Create a set to store unique frequencies
        final = set()
        for i in range(len(values_list)):
            # If the frequency is not in the set, add it
            if values_list[i] not in final:
                final.add(values_list[i])
            else:
                # If the frequency is already in the set, return False
                # as it means there are duplicate occurrences
                return False

        # If all frequencies are unique, return True
        return True
