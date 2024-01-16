import random

class RandomizedSet:

    def __init__(self):
        # Initialize an empty list to store the numbers and a dictionary to store their indices.
        self.numList = []  # List to store numbers.
        self.numMap = {}   # Dictionary to store the mapping of numbers to their indices.

    def insert(self, val: int) -> bool:
        # Check if the value is not in the dictionary (not already inserted).
        res = val not in self.numMap
        if res:
            # If not inserted, add it to the dictionary with its index in numList.
            self.numMap[val] = len(self.numList)
            # Append the value to numList.
            self.numList.append(val)
        
        return res

    def remove(self, val: int) -> bool:
        # Check if the value is in the dictionary (exists).
        res = val in self.numMap
        if res:
            # If it exists, get its index in numList.
            idx = self.numMap[val]
            # Get the last value in numList.
            lastVal = self.numList[-1]
            # Update the value at idx with the last value.
            self.numList[idx] = lastVal
            # Remove the last value from numList.
            self.numList.pop()
            # Update the index of lastVal in the dictionary.
            self.numMap[lastVal] = idx
            # Delete the value from the dictionary.
            del self.numMap[val]
        
        return res

    def getRandom(self) -> int:
        # Return a random value from numList using random.choice.
        return random.choice(self.numList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)    # Insert a value into the set, returns True if successful, False if it already exists.
# param_2 = obj.remove(val)    # Remove a value from the set, returns True if successful, False if it doesn't exist.
# param_3 = obj.getRandom()    # Get a random value from the set.
