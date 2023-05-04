class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                if row >= m or col >= n:
                    return 
                if row == m-1 and col == n-1:
                    return 1
                
                dp[row][col] = dp[row+1][col] + dp[row][col+1]
        
        
        return dp[0][0]

        
       