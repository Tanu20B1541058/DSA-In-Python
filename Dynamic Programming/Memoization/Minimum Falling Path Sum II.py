import math

class Solution:
    def minFallingPathSum(self, grid) -> int:
        def solve(row, col, grid, dp):
            if row == len(grid) - 1:
                dp[row][col] = grid[row][col]
                return dp[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            minPath = math.inf
            for c in range(len(grid)):
                if c != col:
                    minPath = min(minPath, grid[row][col] + solve(row+1, c, grid, dp))
            dp[row][col] = minPath
            return dp[row][col]
        
        n = len(grid)
        dp = [[-1] * n for _ in range(n)]
        minPathSum = math.inf
        for col in range(n):
            pathsum = solve(0, col, grid, dp)
            minPathSum = min(minPathSum, pathsum)
        return minPathSum