class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(row, col, dp):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = solve(row +1, col, dp) + solve(row, col+1, dp)
            return dp[row][col]
        dp = [[-1]*n for i in range(m)]
        return  solve(0,0, dp)
       