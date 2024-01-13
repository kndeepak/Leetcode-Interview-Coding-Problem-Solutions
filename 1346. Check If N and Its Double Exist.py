class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        seen = set()
        
        for num in arr:
            # Check if either the double or half of the current number exists in the set.
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            # Add the current number to the set.
            seen.add(num)
        
        # If no such pair is found, return False.
        return False
