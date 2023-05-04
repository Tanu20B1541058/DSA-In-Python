import math 
class Solution:
    def minFallingPathSum(self, grid) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]

        
        dp[n-1] = grid[n-1]

        for row in range(n - 2, -1, -1):
            for col in range(n):
                min_path = math.inf
                for c in range(n):
                    if c == col:
                        continue
                    min_path = min(min_path, grid[row][col] + dp[row+1][c])
                dp[row][col] = min_path

        return min(dp[0])