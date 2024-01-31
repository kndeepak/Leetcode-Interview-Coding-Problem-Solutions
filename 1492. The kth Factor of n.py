class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors = []
        
        # Find factors up to the square root of n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # Check to avoid adding a square root twice
                    factors.append(n // i)
        
        # Sort factors to ensure they are in ascending order
        factors.sort()
        
        if len(factors) < k:
            return -1
        return factors[k - 1]

                
