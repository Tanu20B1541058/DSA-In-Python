import math
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        def solve(row, col, matrix, dp):
            if col < 0 or col >= len(matrix):
                return 10001
            if row == len(matrix)-1:
                return matrix[row][col]
            if dp[row][col] != -1:
                return dp[row][col]
            ans1 = matrix[row][col] + solve(row + 1, col - 1, matrix, dp)
            ans2 = matrix[row][col] + solve(row + 1, col, matrix, dp)
            ans3 = matrix[row][col] + solve(row + 1, col + 1, matrix, dp)
            dp[row][col] =  min(ans1, ans2, ans3)
            return dp[row][col]

        n = len(matrix)
        min_path = math.inf
        dp = [[-1]*n for _ in range(n)]
        for col in range(n):
            path = solve(0, col, matrix, dp)
            min_path = min(min_path, path)
        return min_path