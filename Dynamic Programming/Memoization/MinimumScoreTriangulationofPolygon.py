import math
class Solution:
    def minScoreTriangulation(self, values) -> int:
        def solve(i, j, arr, dp):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_cost = math.inf
            for k in range(i, j):
                cost = solve(i, k, arr, dp) + solve(k+1, j, arr, dp) + arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
            return dp[i][j]
        dp = [[-1]*(len(values)) for _ in range(len(values))]
        return solve(1, len(values)-1, values, dp)