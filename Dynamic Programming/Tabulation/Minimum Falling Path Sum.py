class Solution:
    def minFallingPathSum(self, matrix) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[n - 1] = matrix[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j], dp[i + 1][j - 1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1])

        return min(dp[0])