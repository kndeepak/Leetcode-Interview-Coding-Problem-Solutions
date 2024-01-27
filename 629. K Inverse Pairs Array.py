def kInversePairs(n, k):
    MOD = 10**9 + 7  # Define the modulo constant
    
    # Initialize a 2D array dp to store the number of arrays with i elements and j inverse pairs
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: There is one way to have 0 inverse pairs with an empty array.
    dp[0][0] = 1
    
    # Loop through the number of elements from 1 to n
    for i in range(1, n + 1):
        dp[i][0] = 1  # There is one way to have 0 inverse pairs with any array of size i
        
        # Loop through the number of inverse pairs from 1 to k
        for j in range(1, k + 1):
            # Calculate dp[i][j] using the recurrence relation:
            # dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - i]
            # Take modulo to prevent integer overflow
            
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
            
            # If j is greater than or equal to i, subtract dp[i - 1][j - i]
            if j >= i:
                dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + MOD) % MOD
    
    return dp[n][k]
