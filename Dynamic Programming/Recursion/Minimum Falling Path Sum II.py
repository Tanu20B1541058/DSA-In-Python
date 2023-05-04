import math
class Solution:
    def minFallingPathSum(self, grid) -> int:
        def solve(row, col, grid):
            if row == len(grid) - 1 :
                return grid[row][col]
            minPath = math.inf
            for c in range(len(grid)):
                if c != col:
                    minPath = min(minPath, grid[row][col] + solve(row+1, c, grid))
            return minPath
        n = len(grid)
        minPathSum = math.inf
        for col in range(n):
            pathsum = solve(0, col, grid)
            minPathSum = min(minPathSum, pathsum)
        return minPathSum
        
       